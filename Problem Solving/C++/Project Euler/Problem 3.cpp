#include <iostream>
#include <cmath>

using namespace std;

bool is_prime(int num){
    for(int i=2; i < sqrt(num)+1; i++){
        if(num == 2){
            return true;
        }

        else if(num % i == 0){
            return false;
        }
        
    }
    return true;
}

int gen_prime_factors(long long int num){
    int max_factor;
    for(int i = 2; i < num; i++){
        if(num % i == 0 && is_prime(i) && i > 0){
            cout << i << endl;
            max_factor = i;
        }
    };
    return max_factor;
}

int main(){
    cout << gen_prime_factors(600851475143) << endl;
    return 0;
}