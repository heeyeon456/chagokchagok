#include <iostream>
#include <list>

using namespace std;

template <typename T>
void print_list(std::list<T>& lst) {
  std::cout << "[ ";
  // 전체 리스트를 출력하기 (이 역시 범위 기반 for 문을 쓸 수 있습니다)
  for (const auto& elem : lst) {
    std::cout << elem << " ";
  }
  std::cout << "]" << std::endl;
}
int main() {
    std::list<int> lst;

    lst.push_back(10);
    lst.push_back(20);
    lst.push_back(30);
    lst.push_back(40);

    cout << "처음 리스트의 상태 " << endl;
    print_list(lst);

    for (std::list<int>::iterator itr = lst.begin(); itr != lst.end(); ++itr) {
        if (*itr == 20) {
            lst.insert(itr, 50);
        }
    }
    cout << " 값이 50인 원소를 20 뒤에 삽입한다. " << endl;
    print_list(lst);

    // vector 와 달리 삭제후에도 iterator loop 실행 가능
    for (std::list<int>::iterator itr = lst.begin(); itr != lst.end(); ++itr) {
        if (*itr == 30) {
            lst.erase(itr);
            break;
        }
    }
    cout << "값이 30 인 원소를 삭제한다." << endl;
    print_list(lst);

}