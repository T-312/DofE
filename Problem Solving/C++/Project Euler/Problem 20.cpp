#include <iostream>
#include <cmath>
#include <string>

int factorial(int n){
    unsigned long long int sum = 1;
    unsigned long long final = 0;
    for(n; n >= 1; n--){
        if(n > 0){
            sum*=n;
        }
        
    }
    std::string a = std::to_string(sum);
    for(int i = 0; i < a.length(); i++){
        char c = a[i];
        int ci = c - '0';
        std::cout << final << std::endl;
        final+=ci;
    }
    

    return final;
}

int main(){
    std::cout << factorial(100) << std::endl;

    return 0;
}