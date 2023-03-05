#include <stdio.h>

int max_of_four(int a, int b, int c, int d)
{
    int max;
    max = a;
    if (a<b && c<b && d<b) max=b;
    if(a<c && b<c && d<c) max=c;
    if(a<d && b<d && c<d) max=d;

    return (max);     
}
int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);
    
    return 0;
}
