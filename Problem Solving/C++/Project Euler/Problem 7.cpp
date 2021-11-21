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

int list_primes(){
    int total = 0;
    int i = 2;
    while(total != 10001){
        if(is_prime(i)){
            cout << i << endl;
            total++;
        }
        i++;
    }
    return 0;
}


int main(){
    list_primes();
    
    return 0;
}