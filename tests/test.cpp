#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

// Template function
template <typename T>
T multiply(T a, T b) {
    return a * b;
}

// A simple class with methods
class Point {
public:
    int x, y;
    Point(int x_, int y_) : x(x_), y(y_) {}
    
    void move(int dx, int dy) {
        x += dx;
        y += dy;
    }

    int distanceSquared(const Point& other) {
        int dx = x - other.x;
        int dy = y - other.y;
        return dx*dx + dy*dy;
    }
};

// Function using STL
void manipulateVector() {
    vector<int> v = {5, 3, 9, 1};
    sort(v.begin(), v.end(), [](int a, int b){ return a > b; });
    for(auto& x : v) {
        cout << x << " ";
    }
    cout << endl;
}

int main() {
    Point p1(0,0), p2(3,4);
    p1.move(2,3);
    cout << "Distance squared: " << p1.distanceSquared(p2) << endl;
    
    cout << multiply<int>(3, 7) << endl;
    
    manipulateVector();
    return 0;
}
