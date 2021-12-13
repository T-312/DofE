#include <iostream>

int gen_seq(unsigned long long num){
    int len = 0;
    while(num != 2){
    if(num%2==0){
        num/=2;
        }
    else if(num%2!=0){
        num = 3*num+1;
        }
    len++;
    }
    return len+2;
}

int main(){
    int length = 0;
    int val = 0;
    for(int i = 2; i < 1000000; i++){
        if(gen_seq(i) > length){
            length = gen_seq(i);
            val = i;
        }

    }
    std::cout << val << std::endl;
    return 0;   
}