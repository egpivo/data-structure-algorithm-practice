/* Usage with CLI on Mac
```bash
g++ -std=c++11 -o intersection intersection.cpp
./intersection
```
*/
#include<iostream>
#include<string>
#include<vector>
#include<unordered_set>

using namespace std;

class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        unordered_set<int> unique1(nums1.begin(), nums1.end());
        vector<int> result;
        for (auto num : nums2)
            if (unique1.erase(num) > 0)
                result.push_back(num);
        return result;
    }
};

int main() {
    vector<int> num1 = {1, 2, 3};
    vector<int> num2 = {2, 3, 4};
    Solution obj;

    vector<int> result = obj.intersection(num1, num2);

    cout << "The answer is: ";
    for (int num : result) {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}
