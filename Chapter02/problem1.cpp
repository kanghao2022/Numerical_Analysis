#include <iostream>
#include <math.h>
//C++实现
int main(){
    float a = 9.4;
    float b = 9;
    float c = 0.4;

    a = a - b - c;

    float ans = -13*pow(2,-25);

    std::printf("计算结果为：%.12e\n",a);
    std::printf("理论结果为：%.12e",ans);

    
    return 0;
}