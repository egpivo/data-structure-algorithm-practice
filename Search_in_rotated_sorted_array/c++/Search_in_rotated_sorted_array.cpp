//
//  Search_in_rotated_sorted_array.cpp
//  Binary search
//
//  Created by Wen-Ting Wang on 2018/10/30.
//

#include<iostream>
#include<vector>
using namespace std;




int main(){
    
   
    vector<int> num1;
// int temp1[] = {4, 5, 6, 7, 0, 1, 2};
//  num1.assign(temp1, temp1 + 7);
    
//   int temp1[] = {3,5,1};
 //   num1.assign(temp1, temp1 + 3);
    int temp1[] = {8, 1, 2, 3, 4, 5, 6, 7};
    num1.assign(temp1, temp1 + 8);
    int target = 6;
    
    //for (std::vector<int>::const_iterator i = num1.begin(); i != num1.end(); ++i)
    //std::cout << *i << ' ';
    
    //for (std::vector<int>::const_iterator i = num2.begin(); i != num2.end(); ++i)
    //    std::cout << *i << ' ';

    
    Solution ans;
    
    cout << "The index is " << ans.search(num1, target) <<endl;
    
    return 0;
}


