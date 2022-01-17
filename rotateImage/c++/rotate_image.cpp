#include<iostream>
#include<vector>
#include <cmath>

using namespace std;

class Solution{
public:
    void rotate(vector<vector<int>>& matrix) {
        transpose(matrix);
        reflect(matrix);
    }
    void transpose(vector<vector<int>>& matrix){
        for(int i = 0; i < matrix.size(); ++i){
            for(int j = i + 1; j < matrix[i].size(); ++j){
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }
    }
    void reflect(vector<vector<int>>& matrix){
        int mid_point = floor(matrix[0].size() / 2);
        for(int i = 0; i < matrix.size(); ++i){
            for(int j = 0; j < mid_point; ++j){
                int position = matrix[0].size() - j - 1;
                int temp = matrix[i][j];
                matrix[i][j] = matrix[i][position];
                matrix[i][position] = temp;
            }
        }
    }
};

int main(){
    vector<vector<int>> matrix{{1,2,3}, {4,5,6}, {7,8,9}};
    cout << "Before" << endl;
    for(int i = 0; i < matrix.size(); ++i) {
        for(int j = 0; j < matrix[i].size(); ++j)
            cout << matrix[i][j] << '\t';
        cout << endl;
    }
    Solution object;
    object.rotate(matrix);
    cout << "After" << endl;
    for(int i = 0; i < matrix.size(); ++i) {
        for(int j = 0; j < matrix[i].size(); ++j)
            cout << matrix[i][j] << '\t';
        cout << endl;
    }
}