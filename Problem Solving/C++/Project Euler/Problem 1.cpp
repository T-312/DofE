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