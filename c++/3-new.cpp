#include <iostream>

// 메모리 관리 문제 
// 프로그램이 정확하게 실행되기 위해서는 컴파일 시에 모든 변수의 주소가 확정되어야 함
// 프로그램 실행시에 자유롭게 할당하게 해제할 수 있는 heap (힙) 공간이 있음
// compiler 에 의해 안정성이 보장되는 stack 과는 달리 사용자가 스스로 제어해야 하는 부분인 만큼 책임도 필요
// c에서는 malloc, free 함수를 지원하여 힙 상에서의 메모리 할당을 지원 
// c++ 에서는 new (malloc - 메모리 할당), delete (free - 메모리 해제)
int main() {
    int* p = new int;  // int 영역이 잘 할당!
    *p = 10; // p 가 할당된 공긴에 10이라는 value 를 집어넣음

    std::cout << *p << std::endl;

    delete p; // 할당된 공간 해제

    // 배열 할당하기
    int arr_size;
    std::cout << "array size: ";
    std::cin >> arr_size;
    int *list = new int[arr_size]; // 배열에 대한 공간 할당
    for (int i=0; i<arr_size; i++) {
        std::cin >> list[i];
    }
    for (int i=0; i<arr_size; i++) {
        std::cout << i << "th element of list: " << list[i] << std::endl;
    }
    delete[] list; // new[] 로 선언하였으면 delete[] 로 해제
    return 0;

}