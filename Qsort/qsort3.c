#include<stdio.h>
#include<stdlib.h>
#include<string.h>
typedef struct
{
    int id;
    char name[10];
    int marks;
}st;
int cmpStruct(const void *p1,const void *p2)
{
   const st *a=p1;             
    const st *b=p2;
   // return a->marks - b->marks;
    //return a->id-b->id;
    return strcmp(a->name,b->name);
    
}
void main()
{
    st st1[]={
        {3,"Vineeth",98},{23,"Udhaya",99},{32,"Sai",80},{12,"Dd",100},{26,"Piggy",0},
        {1,"Half",86},{-1,"Giri",86}
            };
    int n=sizeof(st1)/sizeof(st);
    qsort(st1,n,sizeof(st),cmpStruct);
    for(int i=0;i<n;i++)
     printf("%d  %s %d\n",st1[i].id,st1[i].name,st1[i].marks);
}