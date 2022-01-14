#include<iostream>
#include<string>

using namespace std;

class Solution{

public:
    string addStrings(string num1, string num2){
        int p1 = num1.size() - 1, p2 = num2.size() - 1, carry = 0;
        string answer;
        while(p1 >= 0 || p2 >= 0 || carry != 0){
            if(p1 >= 0)
                carry += num1[p1--] - '0';
            if(p2 >= 0)
                carry += num2[p2--] - '0';

            answer += (carry % 10) + '0';
            carry /= 10;
        }

        reverse(answer.begin(), answer.end());
        return answer;
    }
};


int main(){
    string num1 = "11", num2 = "123";
    Solution obj;

    cout << "The answer is " << obj.addStrings(num1, num2) << endl;

    return 0;
}
