import numpy as np
import pandas as pd
from collections import deque

SOURCE_INDEX = SOURCE.CTP
M_TICKER = b'rb1805'
M_EXCHANGE = EXCHANGE.SHFE
TRADED_VOLUME_LIMIT = 500
SHORT_PERIOD = 5
LONG_PERIOD = 700
MIN_INTERVAL = 1

# ----- some utility functions or classes -----
class signal():
    pass

def rolling_max(arr, period):
    return pd.rolling_max(arr, window=period)

def rolling_min(arr, period):
    return pd.rolling_min(arr, window=period)

def delay(arr, period):
    # delay period
    res = np.zeros(arr.shape) * np.nan
    res[period:] = arr[:-period]
    return res


def compute_5_700(data):
    data = np.array(data)
    if len(data) > 0:
        volume, amount = np.split(data, [1], axis=1)
        ma_5 = None
        ma_700 = None
        if volume.shape[0] < SHORT_PERIOD:
            return ma_5, ma_700
        ma_5 = np.sum(amount[-SHORT_PERIOD:]) / np.sum(volume[-SHORT_PERIOD])
        if volume.shape[0] >= LONG_PERIOD:
            ma_700 = np.sum(amount[-LONG_PERIOD:]) / np.sum(volume[-LONG_PERIOD])
        return ma_5, ma_700


def initialize(context):
    print('initialize')
    context.add_md(source=SOURCE_INDEX)
    context.add_td(source=SOURCE_INDEX)
    context.register_bar(source=SOURCE_INDEX, min_interval=MIN_INTERVAL,
                         start_time="09:30:00", end_time="23:00:00")
    context.subscribe([M_TICKER], source=SOURCE_INDEX)
    # necessary initialization of internal fields.
    context.td_connected = False
    context.trade_completed = True
    context.md_num = 0
    context.traded_volume = 0
    #========= bind and initialize a signal ========
    context.signal = signal()
    context.signal.name = "sample_signal"
    context.signal.look_back = 1000
    context.signal.param1 = 200
    context.signal.param2 = 50
    context.signal.TickPrice = deque(maxlen=context.signal.look_back)
    context.signal.has_open_position = False
    context.signal.has_open_long_position = False
    context.signal.has_open_short_position = False
    context.signal.trade_size = 1


def on_pos(context, pos_handler, request_id, source, rcv_time):
    if request_id == -1 and source == SOURCE_INDEX:
        context.td_connected = True
        context.log_info("td connected")
        if pos_handler is None:
            context.set_pos(context.new_pos(source=source), source=source)
    else:
        context.log_debug("[RSP_POS] {}".format(pos_handler.dump()))


def on_bar(context, bars, min_interval, source, rcv_time):
    print('on bar')
    print('rcv_time', rcv_time)
    print('min_interval', context.parse_nano(min_interval))
    if min_interval == MIN_INTERVAL and source == SOURCE_INDEX:
        for ticker, bar in bars.items():
            if ticker == M_TICKER.decode():
                # context.signal.TickPrice.append((bar.))
                context.signal.TickPrice.append((bar.Volume, bar.Turnover))
                context.md_num += 1
                if context.md_num > SHORT_PERIOD:
                    print('ma_5_7', compute_5_700(context.signal.TickPrice))
                print('(TradingDay)', bar.TradingDay,
                      ' (InstrumentID)', bar.InstrumentID,
                      ' (UpperLimitPrice)', bar.UpperLimitPrice,
                      ' (LowerLimitPrice)', bar.LowerLimitPrice,
                      ' (StartUpdateTime)', bar.StartUpdateTime,
                      ' (StartUpdateMillisec)', bar.StartUpdateMillisec,
                      ' (EndUpdateTime)', bar.EndUpdateTime,
                      ' (EndUpdateMillisec)', bar.EndUpdateMillisec,
                      ' (Open)', bar.Open,
                      ' (Close)', bar.Close,
                      ' (Low)', bar.Low,
                      ' (High)', bar.High,
                      ' (Volume)', bar.Volume,
                      ' (StartVolume)', bar.StartVolume,
                      ' (Turnover)', bar.Turnover,
                      ' (StartTurnover)', bar.StartTurnover)


def on_error(context, error_id, error_msg, order_id, source, rcv_time):
    context.log_error("[ERROR] (err_id){} (err_msg){} (order_id){} (source){}".format(error_id, error_msg, order_id, source))

