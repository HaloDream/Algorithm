// 欧几里德求最大公因子

#include <stdio.h>
unsigned long long gcd(unsigned long long num1,unsigned long long num2);
unsigned long long temp1,temp2;  //暂存2个被除数和除数值

int main(void){
    unsigned long long inputNum1,inputNum2;
    printf("请输入第1个整数值\n");
    scanf("%llu",&inputNum1);
    printf("请输入第2个整数值\n"); 
    scanf("%llu",&inputNum2);
    printf("%llu和%llu的最大公约数为：%llu",inputNum1,inputNum2,gcd(inputNum1,inputNum2));
    return 0;
}

unsigned long long gcd(unsigned long long num1,unsigned long long num2){  //num1为被除数，num2为除数

    // 被除数小于除数时交换两数位置
    if(num1 < num2){
        unsigned long long swp;
        swp = num1;
        num1 = num2;
        num2 = swp;
    }

    
    while (num2 != 0){  //当除数不为0时执行while循环

        /*除数能够整除被除数时，除数即为最大公约数*/
        if((num1 % num2) ==0){  
            return num2;
        }

        /*除数不能整除被除数*/
        temp1 = num1;    //暂存本轮被除数
        temp2 = num2;    //暂存本轮除数
        num1 = num2;      //除数作为下一轮计算中的被除数
        num2 = temp1 % num2; //余数作为下一轮计算中的除数
        
        /*while循环执行到余数为0时，上一轮计算中的除数为最大公约数*/
        if(num2 == 0){
            return temp2;
        }
        
    }
}