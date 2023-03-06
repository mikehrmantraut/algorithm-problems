#include <stdio.h>
#define MAX_LEN 1000

int main() {
    char str[MAX_LEN];
    scanf("%s", str);
    int a=0,b=0,c=0,d=0,e=0,f=0,g=0,h=0,i=0,j=0,z=0;
    while (str[z])
    {
        if (str[z] == '0') a++;
        else if (str[z] == '1') b++;
        else if (str[z] == '2') c++;
        else if (str[z] == '3') d++;
        else if (str[z] == '4') e++;
        else if (str[z] == '5') f++;
        else if (str[z] == '6') g++;
        else if (str[z] == '7') h++;
        else if (str[z] == '8') i++;
        else if (str[z] == '9') j++;
        z++;          
    }
    printf("%d %d %d %d %d %d %d %d %d %d",a,b,c,d,e,f,g,h,i,j);   
    return 0;
}
