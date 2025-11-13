#include <stdio.h>

// Function to find the n-th Fibonacci number recursively
int fibonacciRecursive(int n) {
    if (n <= 1) {
        return n;
    }
    // F(n) = F(n-1) + F(n-2)
    return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2);
}

int main() {
    int n = 10;
    int result = fibonacciRecursive(n);
    printf("The %d-th Fibonacci number is: %d\n", n, result); // The 10th term is 55
    return 0;
}