#include <stdio.h>

int main()
{
    int num1, num2;
    float num3, num4;
    scanf("%d %d\n", &num1, &num2);
    scanf("%f %f\n",&num3, &num4);
    
    printf("%d %d\n",num1+num2, num1-num2);
    printf("%0.1f %0.1f",num3+num4, num3-num4);

    return 0;
}
