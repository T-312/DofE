/*
Project Euler - Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
*/
#include <iostream>

using namespace std;

int main(){
    int nums[1000] = {};
    int main = 0;

    for(int i = 0; i <= 1000; i++){
        nums[i] = i;
    }

    for(int i = 3; i < 1000; i++){
        if(nums[i]%3==0 || nums[i]%5==0){
            main+=nums[i]; 
        }
    }
    cout << main;
    return 0;
}