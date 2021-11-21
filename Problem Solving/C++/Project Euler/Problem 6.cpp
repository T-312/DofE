#include <iostream>
#include <cmath>

using namespace std;

int sq_sum(int max_num){
    int sum1 = 0;
    int sum2 = 0;
    for(int i = 0; i <= max_num; i++){
        sum1+=i*i;
        sum2+=i;
    }
    return sum2*sum2-sum1;
}

int main(){
    cout << sq_sum(100) << endl;
    
    return 0;
}