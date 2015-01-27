/**
    Project Euler. Problem 001.
    ---------------------------------------------------------------------
    If we list all the natural numbers below 10 that are multiples of 3
    or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
    Find the sum of all the multiples of 3 or 5 below 1000.

    @author: Mario Garcia
*/

#include <iostream>

using namespace std;

// Sum even numbers up to a value equal to 'a'
int sumevens(int a)
{
    int n, s=0;
    for (int n=0; n<a; n++){
        if ( n%3==0 || n%5==0 ){
            s += n;
        }
    }
    return s;
}

// ============= MAIN PROGRAM =============
int main()
{
    int a,r;            // Define integers
    cin >> a;           // Take value from user
    r = sumevens(a);    // Sum even numbers
    cout << r << endl;  // Display on command Window

    return 0;
}