#include <iostream>
#include <math.h>
#include <time.h>

int main() {

    double a1 = 2;
    double a2 = 2.222222;
    double ans;
    double start1, stop1, durationTime1;
    double start2, stop2, durationTime2;
    // x = 2
    start1 = clock();
    for (int i = 0;i<pow(10,7);i++)
    {
        ans = 1 + 2 * pow(a1,3)+ 3 * pow(a1,7) + 4 * pow(a1,11) + 5 * pow(a1,15);
    }
    stop1 = clock();
    durationTime1 = double((stop1 - start1)/CLOCKS_PER_SEC);
    printf("x=2,直接计算所需总时间为:%.12fs\n",durationTime1);

    start2 = clock();
    for (int i = 0;i<pow(10,7);i++)
    {
        ans = ((((5 * pow(a1,4) + 4) * pow(a1,4)) + 3) * pow(a1,4) + 2) * pow(a1,3) + 1 ;
    }
    stop2 = clock();
    durationTime2 = double((stop2 - start2)/CLOCKS_PER_SEC);
    printf("x=2,优化算法后所需总时间为:%.12fs\n",durationTime2);

    // x = 2.222222
    start1 = clock();
    for (int i = 0;i<pow(10,7);i++)
    {
        ans = 1 + 2 * pow(a2,3)+ 3 * pow(a2,7) + 4 * pow(a2,11) + 5 * pow(a2,15);
    }
    stop1 = clock();
    durationTime1 = double((stop1 - start1)/CLOCKS_PER_SEC);
    printf("x=2.222222,直接计算所需总时间为:%.12fs\n",durationTime1);

    start2 = clock();
    for (int i = 0;i<pow(10,7);i++)
    {
        ans = ((((5 * pow(a2,4) + 4) * pow(a2,4)) + 3) * pow(a2,4) + 2) * pow(a2,3) + 1 ;
    }
    stop2 = clock();
    durationTime2 = double((stop2 - start2)/CLOCKS_PER_SEC);
    printf("x=2.222222,优化算法后所需总时间为:%.12fs\n",durationTime2);

    return 0;

}