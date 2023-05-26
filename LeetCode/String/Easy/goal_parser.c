char * interpret(char * command){
    int size = strlen(command) + 1;
    char * res = (char*)malloc(size * sizeof(char));
    int x = 0;
    for(int i = 0; i < size; i++){
        if(command[i] == 'G') res[x++] = 'G';
        else if(command[i] == ')' && command[i-1] == '(') res[x++] = 'o';
        else if(command[i] == 'a') res[x++] = 'a';
        else if(command[i] == 'l') res[x++] = 'l';}
    res[x] = '\0';
    return res;
}
