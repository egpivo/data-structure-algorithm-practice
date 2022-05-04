#include<iostream>
#include<string>
#include<vector>

using namespace std;

class Solution {
public:
    vector<string> reorderLogFiles(vector<string>& logs) {
        vector<string> result;
        int count = 0;

        for (auto log: logs){
            if (log.back() <= 'z' and log.back() >= 'a') {
                result.insert(result.begin(), log);
                count ++;
            }
            else{
                result.push_back(log);
            }
        }
        sort(result.begin(), result.begin() + count, compare);
        return result;
    }
    static bool compare(string s1, string s2) {
        string a = s1.substr(s1.find(' '));
        string b = s2.substr(s2.find(' '));
        return a == b ? s1 < s2 : a < b;
    }
};

int main() {
    vector<string> logs;

    logs.insert(logs.end(), "dig1 8 1 5 1");
    logs.insert(logs.end(), "let1 art can");
    logs.insert(logs.end(), "dig2 3 6");
    logs.insert(logs.end(), "let2 own kit dig");
    logs.insert(logs.end(), "let3 art zero");

    Solution obj;
    vector<string> answer = obj.reorderLogFiles(logs);
    for (auto log: answer)
        cout << log << endl;
}