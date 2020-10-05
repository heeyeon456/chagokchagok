#include <iostream>

int change_val(int *p) {
    *p = 3;
    return 0;
}
int main() {
    int number = 5;

    // 포인터를 이용해 value 를 바꾸는 예시
    std::cout << number << std::endl;
    change_val(&number); // c 에서는 포인터를 사용하여 value 를 바꿈
    std::cout << number <<std::endl;

    // reference (참조자)
    int a = 3;
    int& another_a = a; // a의 참조자 another_a 정의 (가리키고자 하는 타입뒤에 &)
    // another_a 에 어떤 작업을 하건 a에 작업을 하는 것
    // int& another a; 는 불가능 -> 누구의 참조자인지 명시해야 함
    // int* p;  -> 포인터는 이러한 포인터형 변수 선언 가능

    another_a = 5;
    std::cout << "a : " << a << std::endl;
    std::cout << "another_a : " << another_a << std::endl;

    // 어떤 변수의 참조자가 되어버리면, 다른 변수를 참조할 수 없게 됨!
    // int b = 3; another_a = b; // a에 b의 value 를 대입하라
    int b = 3;
    another_a = b;
    b = 5;
    std::cout << "b : " << b << std::endl;
    std::cout << "another_a :" << another_a << std::endl;

    // 레퍼런스는 메모리 상에 존재하지 않을 수도 있다.
    // 단순히 value 를 참조하고 있는 상황에서는 reference 를 굳이 메모리상에 할당할 필요가 없다. 
}