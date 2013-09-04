/*Problem 25 from Project Euler
Solution by Paul Barton

Here is the text of the problem:
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn1 + Fn2, where F1 = 1 and F2 = 1.

Hence the first 12 terms will be:
F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the first term in the Fibonacci sequence to contain 1000 digits?

This is simple enough to brute force*/
#include <stdio.h>
#include <math.h>
#include <gmp.h>

int main() {
    double LENGTH = 1000;
    double BASE = 10;
    double maxval = pow(BASE, LENGTH - 1);
    printf("%f\n", maxval);
    int a = 0;
    int b = 1;
    int h;  /* holder variable because I don't know a way around it in C yet */
    int x = 1;
    while (b < maxval) {
        h = b;
        b = a + b;
        a = h;
        x++;
    }
    printf("%d\n", x);
    return 0;
}
/* There are more intelligent ways of finding the answer, but I still need to
prove them to myself before I implement them. Look into Binet's formula. */