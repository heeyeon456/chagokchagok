#include <iostream>

//function overroading example
// 함수의 이름이 달라도 받는 인자에 따라서 컴파일러가 적합한 함수를 찾아 호출한다. 
void print(int x) { std::cout << "int: " << x << std::endl; }
void print(char x) { std::cout << "char: " << x << std::endl; }
void print(double x) { std::cout << "double: " << x << std::endl; }

int main() {
    int a = 1;
    char b = 'c';
    double c = 3.2f;

    print(a);
    print(b);
    print(c);

    return 0;
}