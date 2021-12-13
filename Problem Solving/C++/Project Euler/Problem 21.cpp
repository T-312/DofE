#include <iostream>

int d(int num){
    int sum = 0;
    for(int i = 1; i <= num/2; i++){
        if(num%i == 0){
            sum+=i;
        }
    }
    return sum;
}

int main(){
    int sum = 0;
    for(int i = 1; i < 10000; i++){
        int a = i;
        int b = d(i);

        if(d(a) == b && d(b) == a && a != b){
            sum+=a+b;
        }
    }
    std::cout << sum/2 << std::endl;
    return 0;
}