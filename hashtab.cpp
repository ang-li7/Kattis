#include <iostream>
#include <fstream>
#include <math.h>
#include <cmath>
#include <string>
using namespace std;
bool isPrime(int n){
    if(n==2)
        return true;
    for(int i = 2; i<sqrt(n)+1; i++){
        if(n%i == 0){
            return false;
        }
    }
    return true;
}
int main(){
    int n;
    cin >> n;
    while(n != 0){
        bool f = false;
        if(isPrime(n)){
            f = true;
        }
        int nn = 2*n + 1;
        while (isPrime(nn) == false){
            nn = nn + 1;
        }
        cout << nn;
        if(f == false){
            cout << " (" << n << " is not prime)";
        }
        cout << "\n";
        cin >> n;
    }
    return 0;
}
