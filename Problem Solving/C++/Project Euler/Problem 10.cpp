#include <iostream>
#include <cmath>

using namespace std;

bool is_prime(int num){
    if(num == 2){
        return true;
    }
    for(int i = 2; i < sqrt(num)+1; i++){
        if(num % i == 0){
            return false;
        }
    }
    return true;
}

int gen_primes(int max_val){
    unsigned long long sum = 0;
    for(int i = 2; i < max_val; i++){
        if(is_prime(i)){
            sum+=i;
        }
    }
    cout << sum << endl;
    return sum;
}

int main(){
    cout << gen_primes(2000000) << endl;
    return 0;
}
// Basically solved problem, but the value changes after return