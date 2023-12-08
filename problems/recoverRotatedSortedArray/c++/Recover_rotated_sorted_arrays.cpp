//
//  Recover_rotated_sorted_arrays.cpp
//
//
//  Created by Wen-Ting Wang on 2018/10/30.
//

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    void recoverRotatedSortedArray(vector<int> &nums){

        if(nums.empty() || nums.size() == 1) return;

        for(int i = 0; i < nums.size(); i++){
            if(nums[i] > nums[i + 1]){
                reverse(nums, 0, i); // first part
                reverse(nums, i + 1, nums.size() - 1); // remaining part
                reverse(nums, 0, nums.size() - 1); // all
                return;
            }
        }
    }

private:
    void reverse(vector<int> &nums, int start, int end){
        for(int i = start, j = end; i < j; i++, j--){
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
        }
    }
};


int main(){

    vector<int> nums;
    int temp[] = {4, 5, 7, 1, 2, 3};
    nums.assign(temp, temp + 5);

    Solution ans;

    ans.recoverRotatedSortedArray(nums);

    for(int i=0; i< nums.size(); i++)
        cout << nums[i] << ' ';
    return 0;
}
