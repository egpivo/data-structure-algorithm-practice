#include<iostream>

using namespace std;

class Solution {
/*
Complexity
----------
- TC: O(n)
- SC: O(1)
*/
public:
    bool isRobotBoundedInCircle(string instructions) {
        int x = 0, y = 0, direction = 0;

        for (char c : instructions) {
            if (c == 'G') {
                go(direction, x, y);
            }
            else if (c == 'R') {
                direction = (direction + 90) % 360;
            }
            else if (c == 'L') {
                direction = ((direction - 90) + 360) % 360;
            }
        }
        return (x == 0 and y == 0) or (direction != 0);
    }

    void go(int direction, int& x, int& y) {
        if (direction == 0) {
            y ++;
        }
        else if (direction == 90) {
            x ++;
        }
        else if (direction == 180) {
            y --;
        }
        else if (direction == 270) {
            x --;
        }
    }
};

int main() {
    string instructions = "GLRLLGLL";
    Solution obj;
    cout << obj.isRobotBoundedInCircle(instructions) << endl;
}
