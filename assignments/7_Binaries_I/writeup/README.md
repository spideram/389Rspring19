# Writeup 7 - Binaries I

Name: Ramsay Farah
Section: 0101

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Ramsay Farah

## Assignment Writeup

### Part 1 (90 Pts)

*Put your code here as well as in main.c*
#include <stdio.h>

int main () {
  int num1, num2, temp;

  num1 = 0x1ceb00da;
  num2 = 0xfeedface;
  printf ("%d\n", num1);
  printf ("%d\n", num2);

  temp = num1;
  num1 = num2;
  num2 = temp;

  printf ("%d\n", num1);
  printf ("%d\n", num2);
}

### Part 2 (10 Pts)

*Replace this text with your repsonse to our prompt for part 2!*
The assembly code is essentially trying to swap the place of two numbers while
using xor statements. This can be done quite easily in c with the use of a tewmp variable.
