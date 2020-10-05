#include <iostream>
#include <vector>

template <typename T>
void print_vector(std::vector<T>& vec) {
  // 전체 벡터를 출력하기
  for (typename std::vector<T>::iterator itr = vec.begin(); itr != vec.end();
       ++itr) {
    std::cout << *itr << std::endl;
  }
}

int main() {
    std::vector<int> vec;
    vec.push_back(10); // 맨 뒤에 10 추가
    vec.push_back(20);
    vec.push_back(30);
    vec.push_back(40);
    // 임의의 원소 접근
    std::cout << vec.at(1) << std::endl;

    for(std::vector<int>::size_type i=0; i < vec.size(); i++) {
        std::cout << "vec 의 " << i+1 << " 번쨰 원소 : " << vec[i] << std::endl;
    }

    // iterator 사용
    std::cout << "iterator 사용" << std::endl;
    for (std::vector<int>::iterator itr = vec.begin() ; itr!= vec.end(); ++itr) {
        std::cout << *itr << std::endl;
    }
    std::vector<int>::iterator itr = vec.begin() + 2;
    std::cout << "3번째 원소 :: " << *itr << std::endl;

    // insert and erase
    std::cout << "---------------------" << std::endl;
    vec.insert(vec.begin()+2, 15);
    print_vector(vec);
    
    std::cout << "----------------------" << std::endl;
    vec.erase(vec.begin()+3);
    print_vector(vec);

    // 역반복자 (reverse iterator)
    std::cout << "----------------------" << std::endl;
    std::cout << "역으로 vec 출력하기! " << std::endl;
    std::vector<int>::reverse_iterator r_iter = vec.rbegin();
    for(; r_iter != vec.rend(); r_iter++) {
        std::cout << *r_iter << std::endl;
    }

    // 범위 기반 for 문
    for (int elem : vec) { // 값 복사
        std::cout << "원소 : " << elem << std::endl;
    }

    for (const auto& elem : vec) { // vec 원소들의 상수 레퍼런스로 접근
        std::cout << elem << std::endl;
    }
    
    return 0;
}