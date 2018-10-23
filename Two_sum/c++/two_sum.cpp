//
//  two_sum.cpp
//  
//
//  Created by Wen-Ting Wang on 2018/10/23.
//
#include <iostream>
#include <vector>
#include "two_sum.hpp"

int main(){
    int num[] = {2, 7, 11, 15};
    vector<int> nums(num, num + 4);
    vector<int> index;
    int target = 9;
    
    Solution sol;
    // first solution
    index = sol.twoSum1(nums,target);
    cout << "index1= "<< index[0] << endl << "index2= "<< index[1] << endl;
    
    // 2nd solution
    index = sol.twoSum2(nums,target);
    cout << "index1= "<< index[0] << endl << "index2= "<< index[1] << endl;
    
    return 0;
}
