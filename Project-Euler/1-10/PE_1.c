#include <stdio.h>
/* Problem 1 from Project Euler
Solution by Paul Barton

Here is the text of the problem:
If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Here is a naive solution in C, which I am starting to learn*/
int main () {
    int top = 1000;
    int sum = 0;
    int i;
    for (i = 1; i < top; i++) {
        if (!(i % 3) || !(i % 5)){
            sum = sum + i;
        }
    }
    printf("%d\n", sum);
}