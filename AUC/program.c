/* Pun VireakRoth 
*  ITE M3
*/ 
#include <stdio.h>
#include <math.h>
int main()
{
  int h, b, B;
  printf("Input h :",h); 
  scanf("%d",&h);
  printf("Input b :",b); 
  scanf("%d",&b);
  printf("Input B :",B); 
  scanf("%d",&B);
  printf("-----------------------------------------------\n");
  float Area;
  Area = (b+B)*h/2;
printf("Area :%.2f",Area);
return 0;
}