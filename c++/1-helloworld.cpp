#include <iostream>
using namespace std; //std(c++ 표준 라이브러리) name space 에 정의된 모든 것들을 header:: 없이 사용하겠다. 

int main()
{
    std::cout << "Hello, World!!" << std::endl;
    cout << "Hello, World" << endl; ///cout 은 iostream class의 객체, 표준출력 담당
    std::cout << "iostream class object " << "stdout in c programming " << "hi" << std::endl;
    std::cout << "test " ; // 공백 (한줄 띄어쓰기) 없이 출력

    std::cout << "hi" << std::endl //endl 은 공백(한줄 띄어쓰기) 를 포함하여 출려해준다. 
              << "my name is "
              << "Psi " << std::endl;
    return 0;
}

