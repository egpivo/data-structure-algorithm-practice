//
//  Majority_element.cpp
//
//
//  Created by Wen-Ting Wang on 2018/11/6.
//

#include <iostream>
#include <vector>
#include <set>
using namespace std;

class Solution {
public:
    // moore voting (time: O(n); space: O(1))
    int majorityElement(vector<int>& nums) {
        int count = 1, mode = nums[0];
        for(int i = 1; i < nums.size(); ++i) {

            if(mode != nums[i]){
                count --;
            }
            else{
                if(!count){
                    mode = nums[i];
                    count = 1;
                }
                else
                    count ++;
            }
        }
        return mode;
    }
};

class Solution2 {
public:
    int majorityElement(vector<int>& nums) {

        for (vector<int>::const_iterator i = nums.begin(); i != nums.end(); ++i)
            if(count(nums.begin(), nums.end(), *i) > nums.size()/2) return *i;

        return -1;
    }
};



int main(){
    int input1[] = {3, 2, 3}, input2[] = {2, 2, 1, 1, 1, 2, 2};
    vector<int> nums1, nums2;
    nums1.assign(input1, input1 + 3);
    nums2.assign(input2, input2 + 7);

    Solution ans;

    cout << "input1 : " << endl;
    for (vector<int>::const_iterator i = nums1.begin(); i != nums1.end(); ++i)
        cout << *i << ' ';
    cout <<"\nanswer1: " << endl;
    cout << ans.majorityElement(nums1) << endl;

    cout << "input2 : " << endl;
    for (vector<int>::const_iterator i = nums2.begin(); i != nums2.end(); ++i)
        cout << *i << ' ';
    cout <<"\nanswer2: " << endl;
    cout << ans.majorityElement(nums2) << endl;


    Solution2 ans2;

    cout << "input1 : " << endl;
    for (vector<int>::const_iterator i = nums1.begin(); i != nums1.end(); ++i)
        cout << *i << ' ';
    cout <<"\nanswer1: " << endl;
    cout << ans2.majorityElement(nums1) << endl;

    cout << "input2 : " << endl;
    for (vector<int>::const_iterator i = nums2.begin(); i != nums2.end(); ++i)
        cout << *i << ' ';
    cout <<"\nanswer2: " << endl;
    cout << ans2.majorityElement(nums2) << endl;

}
