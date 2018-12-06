//
//  Container_with_most_water.cpp
//  
//
//  Created by Wen-Ting Wang on 2018/12/6.
//

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int maxArea(vector<int>& height) {
        int left = 0, right = height.size() - 1, area = 0;
        
        while(left < right){
            area = max(area, min(height[left], height[right]) * (right - left));
            height[left] < height[right] ? ++ left : -- right;
        }
        return area;
    }
};


int main() {
    int array[] = {1,8,6,2,5,4,8,3,7};
    vector<int> height;
    height.assign(array, array+9);
    
    int ret = Solution().maxArea(height);
    
    cout << ret << endl;
    return 0;
}
