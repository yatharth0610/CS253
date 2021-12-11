#include <iostream>

using namespace std;

int main(){
    int x, y;
    cin >> x >> y;
    if (x > 0) {
        cout << "a" << endl;
        if (y < 0) {
            cout << 1 << endl;
            if (y < -2000000000) {
                cout << 5 << endl;
            }
        } else {
            cout << 2 << endl;
        }
    }
    else {
        cout << "b" << endl;
        for (int i = 0; i < 5; i++) {
            if(x*y > 0){
                cout << 3 << endl;
            } else {
                cout << 4 << endl;
            }
        }
    }
    return 0;
}
