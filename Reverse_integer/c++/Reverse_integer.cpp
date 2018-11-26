//
//  Reverse_integer.cpp
//  
//
//  Created by Wen-Ting Wang on 2018/11/26.
//

#include <iostream>
using namespace std;

class Solution {
public:
    int reverse(int x) {
        long long reverse = 0;
        
        while(x != 0){
            reverse = reverse * 10 + x % 10;
            x /= 10;
        }
        
        return (reverse > INT_MAX ||reverse <= INT_MIN) ? 0 : reverse;
        
        
    }
};


int main(){
    int x = 12345;
    
    Solution ans;
    
    cout << ans.reverse(x) <<endl;
    
}
