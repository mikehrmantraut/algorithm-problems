int numberOfSteps(int num){
    int steps = 0;
    while (0 < num){
        if (num%2==0){
            num = num/2;
            steps+=1;
        }
        else if (num%2==1)
        {
            num -= 1;
            steps += 1;
        }
    }
    return steps;
}
