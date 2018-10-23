//
//  two_sum.hpp
// O(n^2)
//
//
//  Created by Wen-Ting Wang on 2018/10/23.
//

#ifndef two_sum_hpp
#define two_sum_hpp
using namespace std;  

class Solution{
    public:
        vector<int> twoSum1(vector<int> nums, int target){
            
            vector<int> index;
            for(int i = 0; i < nums.size(); i++){
                for(int j = i + 1; j < nums.size(); j++){
                    if(nums[i] + nums[j] == target){
                        index.push_back(i);
                        index.push_back(j);
                    }
                    
                }
            }
            return index;
        }
};
#endif /* two_sum_hpp */

