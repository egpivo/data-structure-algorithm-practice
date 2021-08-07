//
//  Regular_expression_matching.cpp
//  
//
//  Created by Wen-Ting Wang on 2018/12/3.
//

#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    bool isMatch(string s, string p) {
        
        if(p.empty()){
            return s.empty();
        }
        // usgin substr to see if the position 2 to the end of p is match with s given `p[1] == '*'`
        if(p.size() > 1 && p[1] == '*'){
            return isMatch(s, p.substr(2)) || (!s.empty() && (s[0] == p[0] || p[0] == '.') && isMatch(s.substr(1), p));
            
        }
        // usgin substr to see if p and s is mathching after removing the first posisition given `p[1] != '*'` or length of p is less than 2
        else{
            return !s.empty() && (s[0] == p[0] || p[0] == '.') && isMatch(s.substr(1),p.substr(1));
        }
    }
};


int main(){
    string s = "aaa";
    string p = "ab*";
    
    Solution ans;
    
    cout << ans.isMatch(s, p) << endl;
    
    return 0;
}
