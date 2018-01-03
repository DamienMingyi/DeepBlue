//
// Created by daiab on 18-1-2.
//
#include "../md/MDEngineCTP.h"
#include <iostream>
using namespace kungfu::wingchun;

int main(int argc, const char* argv[]){
    std::cout << "MDEngineTest" << std::endl;
    MDEngineCTP engineCTP;
    string json("{\"FrontUri\": \"tcp://180.168.146.187:10010\", \"UserId\": \"110231\", \"BrokerId\": \"9999\", \"Password\": \"123456\"}");
    engineCTP.initialize(json);
    return 0;
}