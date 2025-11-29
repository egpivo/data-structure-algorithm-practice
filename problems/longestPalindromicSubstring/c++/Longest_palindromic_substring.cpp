//
//  Longest_palindromic_substring.cpp
//
//
//  Created by Wen-Ting Wang on 2018/11/21.
//

#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    string longestPalindrome(string s){
        int len = s.size();
        if(len < 2) return s;

        int start = 0, end = 0; // initialize the recording parameters

        for(int i = 0; i < len - 1; ++i){
            Solution::searchPalindrome(s, len, i, i, start, end); // for odd length
            Solution::searchPalindrome(s, len, i, i + 1, start, end); //for even length
        }
        return s.substr(start, end);
    }


    void searchPalindrome(const string s, const int len, int left, int right, int &start, int &end){

        while(left >= 0 && right < len && s[left] == s[right]){
            -- left;
            ++ right;
        }


        if(end < right - left - 1){
            start = left + 1;
            end = right - left - 1;
        }
    }
};


int main(){

    string example("babad");

    Solution ans;

    cout << "The output is " <<ans.longestPalindrome(example) << endl;

    return 0;
}
