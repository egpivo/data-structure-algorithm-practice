//
//  ZigZag_conversion.cpp
//  
//
//  Created by Wen-Ting Wang on 2018/11/23.
//

#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    string convert(string s, int numRows) {
        if(s.size() <= 1 || numRows == 1) return s;
        string ans;
        
        int step = 2*(numRows-1);
        
        for(int i = 0; i < numRows; ++i){
            for(int j = i; j < s.size(); j += step){
                ans += s[j];
                int temp = j + step - 2*i;
                if(i != 0 && i != numRows - 1 && temp < s.size())
                    ans += s[temp];
                
            }
        }
        return ans;
    }
};


int main(){
    string s = "PAYPALISHIRING";
    int numRows = 3;
    
    Solution ans;
    
    cout << ans.convert(s, numRows) << endl;
    
    return 0;
}
