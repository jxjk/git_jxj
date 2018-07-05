#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define PI 3.14
int main()
	{
	int radius;
	float circum;
	radius = 2;
	circum = 2 * PI * radius;
	printf("变量radius地址是%d\n",&radius);
	printf("半径开方值是%f\n",sqrt(radius));
	printf("半径是%d，周长是%f\n",radius,circum);
	system("pause");
	return 0;
	}
