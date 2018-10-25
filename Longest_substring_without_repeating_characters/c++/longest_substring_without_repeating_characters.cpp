//
//  longest_substring_without_repeating_characters.cpp
//  
//
//  Created by Wen-Ting Wang on 2018/10/25.
//

#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        
        vector <int> temp(256, -1);
        int ans = 0, idx = -1;
        
        for(int i = 0; i < s.size(); i++){
            idx = max(idx, temp[s[i]]); //renew the position if repeated character occurs
            temp[s[i]] = i;
            ans = max(ans, i - idx);
        }
        
        return ans;
    }
};


int main(){
    
    string test1("abcabcbb");
    string test2("bbbbb");
    string test3("pwwkew");
    
    Solution detect;
    
    cout << "Given " << test1 << ", the length is " << detect.lengthOfLongestSubstring(test1) <<endl;
    cout << "Given " << test2 << ", the length is " << detect.lengthOfLongestSubstring(test2) <<endl;
    cout << "Given " << test3 << ", the length is " << detect.lengthOfLongestSubstring(test3) <<endl;
    
    return 0;
}
