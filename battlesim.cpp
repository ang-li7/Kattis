#include <stdio.h>
#include <iostream>
using namespace std;
int main(){
    string x, y;
    cin >> x;
    cout << x << "\n";
    for(int i = 0; i<x.length()-2; i++){
        if(x[i].compare(x[i+1])!=0 && x[i].compare(x[i+2])!=0 && x[i+1].compare(x[i+2])!=0){
            y = y + "C";
            i = i+2;
        }
        else{
            if(x.at(i)=="R"){
                y = y +"S";
            }
            else if (x.at(i)=="B"){
                y = y + "K";
            }
            else{
                y = y+"H";
            }
        }
    }
    cout << y << "\n";
}
