# rm -rf * ; /home/daiab/software/clion-2017.2/bin/cmake/bin/cmake ..
# sudo make install

sudo mkdir -p /opt/kungfu
sudo chown -R daiab:daiab /opt/kungfu
mkdir -p /opt/kungfu/log \
/opt/kungfu/journal \
/opt/kungfu/journal/system \
/opt/kungfu/socket \
/opt/kungfu/runtime \
/opt/kungfu/log/supervisor \
/opt/kungfu/journal/MD/CTP \
/opt/kungfu/journal/MD/CTP/ \
/opt/kungfu/journal/MD/XTP/ \
/opt/kungfu/journal/MD_RAW/CTP/ \
/opt/kungfu/journal/MD_RAW/XTP/ \
/opt/kungfu/journal/TD/CTP/ \
/opt/kungfu/journal/TD/XTP/ \
/opt/kungfu/journal/TD_SEND/CTP/ \
/opt/kungfu/journal/TD_SEND/XTP/ \
/opt/kungfu/journal/TD_RAW/CTP/ \
/opt/kungfu/journal/TD_RAW/XTP/ \
/opt/kungfu/journal/TD_Q/CTP/ \
/opt/kungfu/journal/TD_Q/XTP/ \
/opt/kungfu/journal/L2MD/CTP/ \
/opt/kungfu/journal/L2MD/XTP/ \
/opt/kungfu/journal/L2MD_RAW/CTP/ \
/opt/kungfu/journal/L2MD_RAW/XTP/ \
/opt/kungfu/journal/L2Index/CTP/ \
/opt/kungfu/journal/L2Index/XTP/ \
/opt/kungfu/journal/L2Index_RAW/CTP/ \
/opt/kungfu/journal/L2Index_RAW/XTP/ \
/opt/kungfu/journal/L2Order/CTP/ \
/opt/kungfu/journal/L2Order/XTP/ \
/opt/kungfu/journal/L2Order_RAW/CTP/ \
/opt/kungfu/journal/L2Order_RAW/XTP/ \
/opt/kungfu/journal/L2Trade/CTP/ \
/opt/kungfu/journal/L2Trade/XTP/ \
/opt/kungfu/journal/L2Trade_RAW/CTP/ \
/opt/kungfu/journal/L2Trade_RAW/XTP/ \

pushd /usr/local/bin/
sudo chmod +x  wingchun yjj kungfuctl journal_dumper
popd
sudo cp /usr/local/lib/wingchun/* /usr/local/lib/python3.5/dist-packages/kungfu/wingchun/


# sudo cat > /etc/ld.so.conf.d/ctp.conf <<EOF
# /usr/local/lib/yijinjing/
# /usr/local/lib/wingchun/
# EOF