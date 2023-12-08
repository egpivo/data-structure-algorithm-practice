#include<iostream>
#include<vector>

using namespace std;

class Solution {
public:
    int numPairsDivisibleBy60(vector<int>& time) {
        int result = 0;
        vector<int> freq(60, 0);

        for(auto t:time){
            if(t % 60 == 0){
                result += freq[0];
            }
            else{
                result += freq[60 - t % 60];
            }
            freq[t % 60] += 1;
        }

        return result;
    }

};


int main() {
    Solution object;
    int array[] = {30, 20, 150, 100, 40, 60};
    vector<int> time;
    time.assign(array, array+ 6);
    cout << object.numPairsDivisibleBy60(time) << endl;


}
