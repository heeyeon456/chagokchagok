// 레퍼런스를 리턴하는 함수
#include <iostream>

class A {
    int x;

    public:
    A(int c) : x(c) {}

    int& access_x() { return x; } // x의 reference 리턴
    int get_x() { return x; } // x 의 value 리턴
    void show_x() { std::cout << x << std::endl; }
};

int main() {
    A a(5);
    a.show_x();

    a.access_x() = 3; // a.x = 3;
    a.show_x();

    int &c = a.access_x(); // 렢퍼런스를 리턴하는 함수는 그 함수 부분을 원래의 변수로 치환했다고 생각해도 됨
    c = 4 ; // reference c는 x의 reference(별명)을 받음
    a.show_x();

    int d = a.access_x(); // 그냥 int 변수에 'x의 별명' 을 전달한 경우 -> 단순히 value 복사만 일어남
    d = 3; 
    a.show_x(); // x의 value 는 바뀌지 않고 그냥 4가 출력됨

    // int& e = a.get_x();
    // reference 가 아닌 int 를 리턴하는 경우에는 value 복사가 이루어지어 임시객체가 생성되는데, 임시 객체는 reference 를 가질 수 없다. 
    // e = 2;
    //a.show_x();

    int f = a.get_x();
    f = 1;
    a.show_x();
}