//
//  Median_of_two_sorted_arrays.cpp
//  
//
//  Created by Wen-Ting Wang on 2018/10/30.
//
//  position: floor((m + n + 1)/2)
//  Found:
//   if(maxLeftA <= minRightB & maxLeftB <= minRightA)
//      return (m + n)%2 == 0 ? avg(max(maxLeftA, maxLeftB), min(minRightA, minRightB)) : max(maxLeftA, maxLeftB)
//  else if (maxLeftA > minRightB) {move toward left in A}
//  else {move to right in A}
//
#include <iostream>
#include <vector>

using namespace std;


class Solution {
public:
    /**
     * @param A: An integer array.
     * @param B: An integer array.
     * @return: a double whose format is *.5 or *.0
     */
    double findMedianSortedArrays(vector<int> A, vector<int> B) {
        
        int m = A.size();
        int n = B.size();
        
        if(m > n)
            return findMedianSortedArrays(B, A);
        
        int start = 0;
        int end = m;
        

        while(start <= end){
            int splitA = (start + end)/2;
            int splitB = (n + m + 1)/2 - splitA;
            
            int maxLeftA = (splitA == 0) ? -INT_MAX : A[splitA - 1];
            int minRightA = (splitA == m) ? INT_MAX : A[splitA];
            
            int maxLeftB = (splitB == 0) ? -INT_MAX : B[splitB - 1];
            int minRightB = (splitB == n) ? INT_MAX : B[splitB];
            
            //cout <<"-------"<<endl;
            //cout <<"start="<<start<<endl;
            //cout <<"end="<< end<<endl;
            //cout <<"-------"<<endl;
            //cout <<"maxLeftA="<< maxLeftA<<endl;
            //cout <<"minRightA="<< minRightA<<endl;
            //cout <<"maxLeftB="<< maxLeftB<<endl;
            //cout <<"minRightB="<< minRightB<<endl;
            //cout <<"-------"<<endl;
            
            if(maxLeftA <= minRightB && maxLeftB <= minRightA)
                return ((m + n) % 2 == 0) ? (max(maxLeftA, maxLeftB) + min(minRightA, minRightB))/2.0 :          max(maxLeftA, maxLeftB);
            
            else if(maxLeftA > minRightB)
                end = splitA - 1;
            else
                start = splitA + 1;
        }
        throw invalid_argument("Error");
    }
};




int main(){
    
    int temp2[] = {1, 2, 3, 4};
    int temp1[] = {5, 6, 7, 8};
    vector<int> num1;
    vector<int> num2;
    
    num1.assign(temp1, temp1 + 4);
    num2.assign(temp2, temp2 + 4);
    
    //for (std::vector<int>::const_iterator i = num1.begin(); i != num1.end(); ++i)
    //std::cout << *i << ' ';
    
    //for (std::vector<int>::const_iterator i = num2.begin(); i != num2.end(); ++i)
    //    std::cout << *i << ' ';
    
    Solution ans;
    
    cout << "The meidan is " << ans.findMedianSortedArrays(num1, num2) <<endl;
    
    return 0;
}

    
