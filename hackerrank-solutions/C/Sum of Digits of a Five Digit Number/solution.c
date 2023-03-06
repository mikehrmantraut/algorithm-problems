#include <stdio.h>

int main() {
	
    int n;
    int res;
    res = 0;
    scanf("%d", &n);
    
    for (int i=0;i<5;i++)
    {
        res += n%10;
        n /= 10;
    }
    printf("%d", res);
    return 0;
}
