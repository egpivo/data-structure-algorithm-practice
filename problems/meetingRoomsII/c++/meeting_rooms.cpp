#include<iostream>
#include<vector>
#include<queue>


using namespace std;

class Solution {
public:
    int minMeetingRooms(vector<vector<int> >& intervals) {
        sort(intervals.begin(), intervals.end());
        priority_queue<int, vector<int>, greater<int>> min_heap;
        min_heap.push(intervals[0][1]);

        for(int i = 1; i < intervals.size(); i++){
            if(min_heap.top() <= intervals[i][0])
                min_heap.pop();
            min_heap.push(intervals[i][1]);
        }
        return min_heap.size();
    }
};


int main(){
    vector<vector<int>> intervals{{0, 30}, {5, 10}, {15, 20}};
    Solution obj;
    cout << "The solution is " << obj.minMeetingRooms(intervals) << endl;
    return 0;
}
