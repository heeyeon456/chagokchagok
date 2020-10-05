#include <stdio.h>

// 프로그램이 실행될 때 프로그램인 RAM에 적재
// 코드 세그먼트, 데이터 세그먼트 로 분류할 수 있음!
// 스탭(지역변수) > 힙() > 데이터 (전역변수, 정적변수) > Read-Only Data (상수, 리터럴) > 코드(code segment)

int global=3;
int main() {
    int i;
    char *str = "Hello, Baby";
    char arr[20] = "WHATISIT";

    printf("global: %p \n", &global); // 전역변수 (데이터 영역) 0x56378c57c010 3
    printf("i : %p \n", &i); // 지역변수 (스택) 0x7fffddb532e 1
    printf("str : %p \n", str); // read only data (리터럴) 0x56378c37b7f4 4
    printf("arr : %p \n", arr); // 지역변수 (스택) 0x7fffddb532f0 2


}