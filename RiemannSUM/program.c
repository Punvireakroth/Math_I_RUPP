/* Pun VireakRoth
* ITE M3
*
*/
#include <math.h>
#include <stdio.h>
int main() {
  double left_point, right_point, mid_point;
  double dx, a = 0, b = 2;
  int i = 0;
  printf("n\tleft point\t\t\tright point\t\t\t\tmid point\n");
  for (int n = 20; n <= 10000; n += 20) {
    dx = (b - a) / n;
    left_point = 0;
    right_point = 0;
    mid_point = 0;
    for (int i = 0; i < n; i++) {
      left_point += (pow((a + i * dx), 3) + 1) * dx;
      right_point +=(pow((a + (i + 1) * dx), 3) + 1) * dx;
      mid_point +=(pow((a + (2 * i + 1) * dx / 2), 3) + 1)*dx;
    }
    printf("\n%d\t\t", n);
    printf("%.10f\t\t\t", left_point);
    printf("%.10f\t\t\t", right_point);
    printf("%.10f\t\t\t", mid_point);
  }
  printf("\n");
  return 0;
}