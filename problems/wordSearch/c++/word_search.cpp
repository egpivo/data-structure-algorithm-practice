//
//  word_search.cpp
//
//  Created by Wen-Ting Wang on 2022/01/14
//
#include<iostream>
#include<vector>
#include<string>

using namespace std;


class Solution {
public:
    bool exist(vector<vector<char>>& board, string word){
        for(int row = 0; row < board.size(); row++){
            for(int col = 0; col < board[col].size(); col++){
                if(backtrack(board, row, col, 0, word))
                    return true;
            }
        }
        return false;
    }
    bool backtrack(vector<vector<char>>& board, int row, int col, int word_index, string word){
        if(word_index == word.size())
            return true;

        if(row < 0 || row >= board.size() || col < 0 || col >= board[row].size() ||board[row][col] != word[word_index])
            return false;

        board[row][col] = '#';
        bool does_exist = (
            backtrack(board, row - 1, col, word_index + 1, word) ||
            backtrack(board, row + 1, col, word_index + 1, word) ||
            backtrack(board, row, col + 1, word_index + 1, word) ||
            backtrack(board, row, col - 1, word_index + 1, word)
        );
        board[row][col] = word[word_index];
        return does_exist;
    }
};

int main()
{
    //single quotes for char; double quotes for string
    vector<vector<char>> board{
        {'A', 'B', 'C', 'E'},
        {'S', 'F', 'C', 'S'},
        {'A', 'D', 'E', 'E'}
    };
    string word = "ABCCED";

    Solution obj;
    cout << "The answer is " << obj.exist(board, word) << endl;

    return 0;
}
