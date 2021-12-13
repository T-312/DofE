#include <iostream>

int f(int num){
    if(num%2==0){
        return num/2;
    }
    if(num%2!=0){
        return (3*num)+1;
    }
    return 1;
}

int main(){
    int max_vals[] = {0, 0};
    int length = 0;
    int current = 5;

    for(int i = 5; i <= 20; i++){
        if(length > max_vals[0]){
            max_vals[0] = length;
            max_vals[1] = i-1;
            std::cout << length << std::endl;
        }
        while(f(current) != 1){
            length++;
            current = f(current);
        }
    }
    std::cout << max_vals[1] << std::endl;
}