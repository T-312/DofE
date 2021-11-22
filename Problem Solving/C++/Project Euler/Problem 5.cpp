#include <iostream>
#include <cmath>

using namespace std;

int func(int max_num){
    int current_val = 1;
    int stage = 1;
    while(stage <= max_num){
        if(current_val % stage == 0){
            stage++;
        } 
        else if(current_val % stage != 0){
            stage = 1;
            current_val++;
        }
    }
    return current_val;
}

int main(){
    cout << func(20) << endl;
    return 0;
}