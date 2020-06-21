#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int cmpStr(const void *p1,const void *p2)
{
    //return strcmp(p2,p1); //for descending order
    return strcmp(p1,p2);
}
void main()
{
    char name[][20]={"Vineeth","Udhaya","Sai","Dd","Piggy","Half","Giri"};
    int n=sizeof(name)/sizeof(name[0]);
    qsort(name,n,sizeof(name[0]),cmpStr);
    for(int i=0;i<n;i++)
     printf("%s  ",name[i]);
}