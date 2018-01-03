CMAKE_MINIMUM_REQUIRED(VERSION 3.7)
PROJECT(mytest)

#ADD_LIBRARY(${PROJECT_NAME} SHARED
#        DataConsumer.cpp
#        DataConsumer.h
#        MDEngineCTP.h
#        StrategyDataConsumer.cpp
#        StrategyDataConsumer.h)
#TARGET_LINK_LIBRARIES(${PROJECT_NAME} journal kflog
#        ${Boost_LIBRARIES} ${PYTHON_LIBRARIES})
#INSTALL(TARGETS ${PROJECT_NAME} DESTINATION "lib/wingchun")
#
#ADD_EXECUTABLE(wc_printer wc_strategy_data_printer.cpp)
#TARGET_LINK_LIBRARIES(wc_printer ${PROJECT_NAME} journal ${Boost_LIBRARIES})
#TARGET_LINK_LIBRARIES(wc_printer ${PYTHON_LIBRARY}/libpython3.6m.so)
#INSTALL(TARGETS wc_printer DESTINATION "bin")

ADD_EXECUTABLE(md_engine_test MDEngineTest.cpp ../md/MDEngineCTP.h ../md/MDEngineCTP.cpp)
TARGET_LINK_LIBRARIES(md_engine_test journal ${Boost_LIBRARIES} ${PYTHON_LIBRARIES} ctpmd)
#TARGET_LINK_LIBRARIES(td_pos_tool ${PYTHON_LIBRARY}/libpython3.6m.so)
