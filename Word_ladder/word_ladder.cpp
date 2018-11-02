//
//  word_ladder.cpp
//
// Graph: Breadth-First search (BFS)
//  Created by Wen-Ting Wang on 2018/11/2.
//

#include<iostream>
using namespace std;


// Use heatmap to record all possible paths to the end
class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        
        unordered_set<string> wordSet(wordList.begin(), wordList.end());
        unordered_map<string, int> pathCount({{beginWord, 1}});
        queue<string> wordBag{{beginWord}}; //create a container to store words
        
        while(!wordBag.empty()){ // test whether container is empty
            string term = wordBag.front(); // access the next word in wordBag
            wordBag.pop(); // remove the next element
            
            for(int i = 0; i < term.size(); ++i){
                string newWord = term;
                for(char letter = 'a'; letter < 'z'; ++letter){ // traversial 26 letters: a->z
                    newWord[i] = letter;
                    if(wordSet.count(newWord)){ // check if newWord exists in wordSet
                        if(newWord == endWord)
                            return pathCount[term] + 1; //return the total number
                        
                        if(!pathCount.count(newWord)){ // check if newWord does NOT exist in pathCount
                            wordBag.push(newWord); // insert the newWord
                            pathCount[newWord] = pathCount[term] + 1; //count one more
                        }
                        
                    }
                    
                }
                
            }
            
        }
        return 0;
    }
};

// Like a structure of tree, count the number of all layers
class Solution2 {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        
        unordered_set<string> wordSet(wordList.begin(), wordList.end());
        queue<string> wordBag{{beginWord}};
        int counter = 0;
        
        while(!wordBag.empty()){
            for(int k = wordBag.size(); k > 0; --k){
                string term = wordBag.front();
                wordBag.pop();
                
                if(term == endWord)
                    return counter ++;
                for(int i = 0; i < word.size(); ++i){
                    string newWord = term;
                    for(char letter = 'a'; ch <= 'z'; ++ch){
                        newWord[i] = letter;
                        if(wordSet.count(newWord) && newWord != term){// look up if the newWord existing in wordSet, except of the term
                            wordBag.push(newWord);  // add a newWord
                            wordSet.erase(newWord); // since each element in unordered_set is unique
                        }
                    }
                }
            }
            counter ++;
        }
        return 0;
    }
};




