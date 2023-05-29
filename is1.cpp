#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<iostream>


int main() {
    char str[] = "Shrihari Waykule";
    int i;
    int len = strlen(str);

    for(i=0; i<len; i++) {
        printf("%c", str[i] & 127);
    }
    printf("\n");
    for(i=0; i<len; i++) {
        printf("%c", str[i] ^ 127);
    }
    printf("\n");

    return 0;
}