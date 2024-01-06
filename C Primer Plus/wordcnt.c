// wordcnt.c --统计字符数、单词数、行数
#include <stdio.h>
#include <ctype.h>    //为isspace()函数提供原型
#include <stdbool.h>   //为bool、ture、false提供定义

#define STOP '|'

int main(void)
{
    char c;         //读入字符
    char prev;       //读入的前一个字符
    long n_chars = 0L;  //字符数
    int n_lines =0;    //行数
    int n_words = 0;   //单词数
    int p_lines = 0;   //不完整的行数（未以'\n'结尾）
    bool inword = false; //判断字符是否在单词中，在单词中为true

    printf("Enter text to be analyzed ( | to terminate):\n");
    prev = '\n';  //用于识别完整的行，判断结束符"|"前面是不是以"\n"结尾

    while ((c = getchar()) != STOP)
    {
        n_chars++;      //累加统计字符
        if (c == '\n')
        {
            n_lines++;  //累加统计行
        }

        if (!isspace(c) && !inword)
        {
            inword = true;  //开始一个新单词
            n_words++;     //统计单词
        }
        
        if (isspace(c) && inword)
        {
            inword = false;  //到达单词的末尾
        }

        prev = c;   //保存字符的值，关键是"|"前的词
        
    }
    
    if (prev != '\n')
    {
        p_lines = 1; //"|"前的词不是"\n"则这一行不完整
    }
    
    printf("characters = %ld, words = %d, lines = %d,",n_chars,n_words,n_lines);
    printf("partial lines = %d\n",p_lines);


    return 0;
}



