#include <iostream>

using namespace std;

int fibonacci(int n1, int n2){
    int current[] = {n1, n2};
    int result, sum = 0;

    while(result < 4000000){
        if (current[0] + current[1] > 4000000){
            break;
        }
        else{
            result = current[0] + current[1];
            current[0] = result;
            if (result%2==0){
                sum+=result;
            }

            result = current[0] + current[1];
            current[1] = result;
            if (result%2==0){
                sum+=result;
            }
        }
    }
    return sum;
}

int main(){
    cout << fibonacci(0, 1);
    return 0;
}