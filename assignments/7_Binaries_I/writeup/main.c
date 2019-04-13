/*
 * Name: Ramsay Farah
 * Section: 0101
 *
 * I pledge on my honor that I have not given or received any unauthorized
 * assistance on this assignment or examination.
 *
 * Digital acknowledgement: Ramsay Farah
 */
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
