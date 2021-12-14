#include <iostream>
#include <cmath>

int f(){
    int count = 0;
    int nums[] = {};
    int id = 0;
    bool found;
    for(int a = 2; a <= 5; a++){
        for(int b = 2; b <= 5; b++){
            std::cout << pow(a, b) << std::endl;
            for(int i = 0; i < sizeof(nums)/sizeof(*nums); i++){
                if(nums[i] == pow(a, b)){
                    found = true;
                }
            }
            if(!(found)){
                count++;
            }
            found = false;
            nums[id] = pow(a, b);
            id++;
        }
    }
    std::cout << count << std::endl;
    return 0;
}

int main(){
    f();
    // std::cout <<  << std::endl;
    return 0;
}