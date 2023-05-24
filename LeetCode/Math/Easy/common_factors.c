int commonFactors(int a, int b){
    int i = 1;
    int j = 0;
    if (a >= b){
        while (i <= a){
            if (a%i == 0 && b%i==0) j += 1;
            i++;}}
    else{
        while (i <= b){
            if (a%i==0 && b%i==0) j+=1;
            i++;}}
    return (j);
}
