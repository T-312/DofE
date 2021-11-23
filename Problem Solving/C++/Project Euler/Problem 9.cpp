#include <iostream>
#include <cmath>
#include <sstream>

using namespace std;

int p_trip(int max_num){
    int a,b,c,final;
    for(int a = 1; a <= max_num/2; a++){
    for(int b = 1; b <= max_num/2; b++){
        c = 1000-b-a;
            if(pow(a, 2) + pow(b, 2) == pow(c, 2)){
                if(a+b+c == max_num && a > 0 && b > 0 && c > 0){
                    cout << a << endl;
                    cout << b << endl;
                    cout << c << endl;
                    final=a*b*c;
                    return final;
                }
            }
        }
    }
    return 0;
}

int main(){
    cout << p_trip(1000) << endl;
    return 0;
}