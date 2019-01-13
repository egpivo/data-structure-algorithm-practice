//
//  Integer_to_Roman.cpp
//  
//
//  Created by Wen-Ting Wang on 2019/1/13.
//

#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    string intToRoman(int num) {
        string ans = "";
        char roman [] = {'M', 'D', 'C', 'L', 'X', 'V', 'I'};
        int integer [] = {1000, 500, 100, 50, 10, 5, 1};
        
        for(int i = 0; i < 7; i += 2){
            int x = num/integer[i];
            if(x < 4)
                for(int j = 1; j <= x; ++j) ans += roman[i];
            else if(x == 4)
                ans = ans + roman[i] + roman[i-1];
            else if (x > 4 && x < 9){
                ans += roman[i-1];
                for(int j = 6; j <= x; ++j) ans += roman[i];
            }
            else
                ans = ans + roman[i] + roman[i-2];
            
            num %= integer[i];
        }
        
        return ans;
    }
};

int main(){
    Solution ans;
    int input;
    cout << "Please enter an integer:" << endl;
    cin >> input;
    cout<< input <<" = " <<ans.intToRoman(input) << endl;
    return 0;
}
