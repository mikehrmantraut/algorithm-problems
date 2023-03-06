#include <stdio.h>
#include <stdlib.h>

int main() {
    
    int n, i = 0, sum = 0;
    scanf("%d", &n);
    int *arr = malloc(n*sizeof(int));
    
    while (i<n)
    {
        scanf("%d", &arr[i]);
        sum += arr[i];
        i++;
    }
    printf("%d", sum);
    free(arr);
    return 0;
}
