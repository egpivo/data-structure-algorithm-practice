#include <iostream>
using namespace std;

class Solution {
public:
    int hammingWeight(uint32_t n) {
        int count = 0;
        while (n != 0) {
            count ++;
            n &= (n - 1);
        }
        return count;
    }

};

int main() {
    int n = 11;
    Solution ans;
    cout << "Answer:" << ans.hammingWeight(n) << endl;
    return 0;
}
