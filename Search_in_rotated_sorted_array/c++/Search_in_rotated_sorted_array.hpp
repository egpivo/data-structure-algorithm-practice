//
//  Search_in_rotated_sorted_array.hpp
// O(n^2)
//
//
//  Created by Wen-Ting Wang on 2018/10/23.
//

#ifndef Search_in_rotated_sorted_array_hpp
#define Search_in_rotated_sorted_array_hpp

class Solution {
public:
    int search(vector<int>& nums, int target) {
        
        int n = nums.size();
        
        int start = 0;
        int end = n;
        
        while(start < end){
            int split = (end - start)/2;
            
            int minLeft = nums[start];
            int maxLeft = nums[start + split - 1];
            int minRight = nums[start + split];
            int maxRight = nums[end - 1];
            
            // cout <<"-------"<<endl;
            // cout <<"start="<<start<<endl;
            // cout <<"end="<< end<<endl;
            // cout <<"-------"<<endl;
            // cout <<"minLeft="<< minLeft<<endl;
            // cout <<"maxLeft="<< maxLeft<<endl;
            // cout <<"minRight="<< minRight<<endl;
            // cout <<"maxRight="<< maxRight<<endl;
            
            
            if((maxLeft - minLeft) >= 0 & (maxRight - minRight) >= 0){
                
                if(target < min(minLeft, minRight) | target > max(maxRight, maxLeft)){
                    cout << "gg1"<<endl;
                    return -1;
                }
                else if(target >= minLeft & target <= maxLeft){
                    if(target == minLeft)
                        return start;
                    else if(target == maxLeft)
                        return start + split - 1;
                    else
                        end = start + split;
                }
                else{
                    if(target == minRight)
                        return start + split;
                    else if(target == maxRight)
                        return end - 1;
                    else
                        start += split;
                }
            }
            else if((maxLeft - minLeft) >= 0){
                if(target >= minLeft & target <= maxLeft){
                    if(target == minLeft)
                        return start;
                    else if(target == maxLeft)
                        return start + split - 1;
                    else
                        end = start + split;
                }
                else{
                    start += split;
                }
            }
            else{
                if(target >= minRight & target <= maxRight){
                    if(target == minRight)
                        return start + split;
                    else if(target == maxRight)
                        return end - 1;
                    else
                        start += split;
                }
                else{
                    end = start + split;
                }
            }
        }
      //  cout << "gg3"<<endl;
        return -1;
    }
};



class Solution2 {
public:
    int search(vector<int>& nums, int target) {
        int n = nums.size();
        
        int start = 0;
        int end = n - 1;
        
        while(start <= end){
            int split = start + (end - start)/2;
        
            if(nums[split] == target)
                return split;
            else if(nums[split] <  nums[end])
                if(nums[split] < target && target <= nums[end])
                    start = split + 1;
                else
                    end = split - 1;
            else
                if(nums[split] > target && target >= nums[start])
                    end = split - 1;
                else
                    start = split + 1;
        }
        return - 1;
    }
};
#endif /* two_sum_hpp */


