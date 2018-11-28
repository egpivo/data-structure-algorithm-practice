//
//  String_to_integer.cpp
//  
//
//  Created by Wen-Ting Wang on 2018/11/28.
//
#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    int myAtoi(string str) {
        
        if(str.empty()) return 0;
        
        int ans = 0, len = str.size(), i = 0, sign = 1;
        
        while(i < len && str[i] == ' ') ++i;
        
        if(str[i] == '+' || str[i] == '-')
            sign = (str[i++] == '+') ? 1 : -1;
        
        while(str[i] >= '0' && str[i] <= '9' && i < len){
            
            if(ans  > INT_MAX / 10 || ( ans  == INT_MAX / 10 && str[i] - '0' > 7))
                return (sign == 1) ? INT_MAX : INT_MIN;
            
            ans = 10 * ans + (str[i++] - '0');
        }
        
        return ans * sign;
    }
};

int main(){
    string str = "4193 with words";
    
    Solution ans;
    
    cout << "Input: " << str << endl;
    cout << "Output: "<< ans.myAtoi(str) << endl;

}
