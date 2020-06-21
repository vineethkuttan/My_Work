#include<stdio.h>
#include<stdlib.h>
/*
int cmpInt(const void *p1,const void *p2)
{
    const int *a=p1;             //typecasting into integer
    const int *b=p2;
    return *a-*b;
}
*/
int cmpInt(const void *p1,const void *p2)
{
    return *p1-*p2;
    //return *p2-*p1; //for descending order
}
void main()
{
    int num[]={1,6,2,3,8,99};
    int n=sizeof(num)/sizeof(int);
    qsort(num,n,sizeof(int),cmpInt);
    for(int i=0;i<n;i++)
     printf("%d  ",num[i]);
}
