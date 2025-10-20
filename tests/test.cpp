#include <iostream>
#include<algorithm>
using namespace std;

int add(int a, int b) {
    return a + b;
}

class Point {
    public:
        int x, y;
        void move(int dx, int dy) {
            x += dx;
            y += dy;
        }
};

int main() {
    Point p;
    p.move(1, 2);
    cout << add(3, 4) << endl;
}