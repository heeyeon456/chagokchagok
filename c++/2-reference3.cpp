#include <iostream>

int function() {
    int a = 2;
    return a;
}

int& function2() {
    int a = 2;
    return a; // return type int&
}

int& function3(int& a) {
    a = 5;
    return a; // reference 를 리턴 ( 인자로 받은 reference 를 그대로)
}

int main() {
    //int b = function(); // function 안에 정의된 a라는 변수의 value 가 b에 복사됨
    //int b = function2(); // function이 a를 reference -> a가 사라짐 (dangling reference)
    
    //int b = 2;
    //int c = function3(b); // a는 main의 b를 참조하고 있음 ( 아직 살아있는 변수인 b를 계속 참조)
    //std::cout << b << std::endl;
    // 참조자를 그냥 리턴하는 경우 장점
    // c에서 엄청나게 큰 구조체가 있을 때, 해당 구조체 변수를 그냥 리턴하면 시간이 오래 걸리지만,
    // 해당 구조체를 가리키는 포인터를 리턴하면 포인터 주소 한번 복사로 빨리 끝남
    // 레퍼런스 역시 레퍼런스가 참조하는 타입의 크기와 상관없이 딱 한번의 주소값 복사로 전달이 끝나게 됨

    const int& c = function(); // const 를 참조자로 받았떠니 문제 없이 컴파일 됨
    std::cout << "c : " << c << std::endl;
    // 함수의 리턴 value 는 해당 문장이 끝나면 소멸하는 것이 정상, 예외적으로 상수 레퍼런스로 리터값을 받게 되면 해당 리턴 value 의 생명이 연장됨
    


    return 0;
}