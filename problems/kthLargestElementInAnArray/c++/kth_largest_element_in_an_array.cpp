#include <iostream>
#include<vector>
#include <algorithm>
#include <queue>

using namespace std;

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        return nums[nums.size() - k];
    }
};

class SolutionHeapQ {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int, vector<int>, greater<int> > min_heap;
        for(int i = 0; i < nums.size(); i++) {
            min_heap.push(nums[i]);
            if (min_heap.size() > k){
                min_heap.pop();
            }
        }
        return min_heap.top();
    }
};


int main(){
    vector<int> num; //c++11 = {4,2,7,1,3,6,9};
    num.push_back(4);
    num.push_back(2);
    num.push_back(7);
    num.push_back(1);
    num.push_back(3);
    num.push_back(6);
    num.push_back(9);
    int k = 2;
    cout << "sorting - " << Solution().findKthLargest(num, k) << endl;
    cout << "priority Q - " << SolutionHeapQ().findKthLargest(num, k) << endl;
    return 0;
}