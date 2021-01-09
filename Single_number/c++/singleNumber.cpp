//
//  singleNumber.cpp
//
//  Created by Wen-Ting Wang on 2021/01/09.
//

#include<iostream>
#include<unordered_set>
#include<unordered_map>
#include<queue>
#include<string>
#include<vector>
using namespace std;

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        if(nums.size() == 1) return nums[0];

        unordered_map<int, int> numCount;
        for(int i = 0; i < nums.size(); ++i){
            if(numCount.find(nums[i]) == numCount.end()){
                numCount[nums[i]] = 1;
            }
            else {
                numCount[nums[i]] += 1;
            }
        }
        
        for(auto iter = numCount.begin(); iter != numCount.end(); ++iter){
           if (iter->second == 1) {
                return iter->first;
            }
        }
        return 0;
    }
};

int main()
{
    vector<int> numList;
    numList.push_back(2);
    numList.push_back(2);
    numList.push_back(1);

    Solution ans;

    cout << ans.singleNumber(numList) << endl;
    
    return 0;
}