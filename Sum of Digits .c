#include<stdio.h>
int main(void)
{
    int n,t,ans,sum;
    scanf("%d",&t);
    while(t>0)
    {
        scanf("%d",&n);
        while(n>0)
        {
            ans=n%10;
            sum=sum+ans;
            n=n/10;
        }
    printf("%d\n",sum);
    sum=0;
    t--;
    }
}
