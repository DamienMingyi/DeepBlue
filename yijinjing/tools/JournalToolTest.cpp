//
// Created by daiab on 18-1-3.
//

#include "PageUtil.h"
#include "PageHeader.h"
#include "Timer.h"
#include <iostream>
using namespace kungfu::yijinjing;

int main(int argc, const char* argv[]){
    string folder = "/opt/kungfu/journal/MD/CTP/";
    string jname = "MD_CTP";
    vector<short> pageNums = PageUtil::GetPageNums(folder, jname);
    string format("%Y%m%d-%H:%M:%S");
    for (size_t idx = 0; idx < pageNums.size(); idx++)
    {
        PageHeader header = PageUtil::GetPageHeader(folder, jname, pageNums[idx]);
        std::cout << "[" << pageNums[idx] << "]"
                  << " (ST)" << (short)header.status
                  << " (JN)" << header.journal_name
                  << " (PN)" << header.page_num
                  << " (FN)" << header.frame_num
                  << " (LP)" << header.last_pos
                  << " (FV)" << header.frame_version
                  << " (SN)" << header.start_nano << "[" << parseNano(header.start_nano, format.c_str()) << "]"
                  << " (CN)" << header.close_nano << "[" << parseNano(header.close_nano, format.c_str()) << "]";
        std::cout << std::endl;
    }
}
