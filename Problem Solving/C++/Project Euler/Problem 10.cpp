#include <iostream>
#include <cmath>

using namespace std;

bool is_prime(int num){
    if(num == 2){
        return true;
    }
    else if(num == 1){
        return false;
    }
    for(int i = 2; i < sqrt(num)+1; i++){
        if(num % i == 0){
            return false;
        }
    }
    return true;
}

unsigned long long gen_primes(int max_val){
    unsigned long long sum = 0;
    for(int i = 1; i < max_val; i+=2){
        if(is_prime(i)){
            sum+=i;
        }
    }
    return sum+2;
}

int main(){
    cout << gen_primes(2000000) << endl;
    return 0;
}