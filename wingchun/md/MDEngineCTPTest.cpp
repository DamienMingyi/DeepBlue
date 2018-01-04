//
// Created by daiab on 18-1-3.
//

#include "MDEngineCTP.h"
#include "iostream"

using namespace kungfu::wingchun;

int main(int argc, const char* argv[]){
    std::cout << "MDEngineTest" << std::endl;
    MDEngineCTP engineCTP;
    string json("{\"FrontUri\": \"tcp://180.168.146.187:10010\", \"UserId\": \"110231\", \"BrokerId\": \"9999\", \"Password\": \"1073004628\"}");
    engineCTP.initialize(json);
//    vector<string> instruments = {"rb1805"};
//    vector<string> markets = {""};
//    engineCTP.subscribeMarketData(instruments, markets);
    std::cout << "==========" << std::endl;
    engineCTP.start();
    engineCTP.wait_for_stop();
    return 0;
}