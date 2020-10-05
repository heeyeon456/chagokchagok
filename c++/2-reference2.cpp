#include <iostream>

int change_val(int &p) { // 참조자를 인자로 전달
    p = 3;
    return 0;
}

int main() {
    int number = 5;
    //std::cout << number << std::endl;
    change_val(number); // number 변수에 대한 전달을 reference 변수 p 가 받으므로, p가 number 의 reference 변수가 됨
    //std::cout << number << std::endl;

    int x;
    int& y = x;
    int& z = y; // 참조자의 참조자는 존재할 수 없으므로 z 역시 x의 참조자가 됨

    x = 1;
    std::cout << "x : " << x << " y : " <<  y << " z : " << z << std::endl;

    y = 2;
    std::cout << "x : " << x << " y : " <<  y << " z : " << z << std::endl;

    z = 3;
    std::cout << "x : " << x << " y : " <<  y << " z : " << z << std::endl;
    
    // refernce 의 배열과 배열의 reference
    int a, b;
    // int& arr[2] = {a, b}; // 레퍼런스의 레퍼런스, 레퍼런스의 배열, 레퍼런스의 포인터는 존재할 수 없다.
    // 문법사 배열의 이름은 첫번째 원소의 주소값으로 변환될 수 있어야 한다. arr[1] <-> *(arr + 1)
    // 그러면 이는 해당 원소가 메모리 상에 존재한다는 의미가 되지만, reference 는 특별한 경우가 아닌 이상 메모리 상에서 공간을 차지하지 않음

    // 배열들의 reference
    int arr[3] = {1, 2, 3};
    int(&ref)[3] = arr; // reference 가 arr 를 참조함
    // 크기가 3 인 배열의 별명이 되어야 함 , int(&ref)[5] = arr 이런건 불가능

    ref[0] = 2;
    ref[1] = 3;
    ref[2] = 1;

    std::cout << arr[0] << arr[1] << arr[2] << std::endl;

    return 0;



}