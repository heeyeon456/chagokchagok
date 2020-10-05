#include <iostream>

class Animal {
    // member variable
    //private : 아래 씌여진 것들은 모두 객체 내에서 보호되고  있다.
    // 자기 객체 안에서만 접근할 수 있을 뿐 객체 외부에서는 접근할 수 없다. 
    // 기본 명시를 안하면 default 는 private
    private:
    int food;
    int weight;

    // member function
    public:
    void set_animal(int _food, int _weight) {
        food = _food;
        weight = _weight;
    }
    void increase_food(int inc) {
        food += inc;
        weight += (inc / 3);
    }
    void view_stat() {
        std::cout << "이 동물의 food  : " << food << std::endl;
        std::cout << "이 동물의 weight  : " << weight << std::endl;
    }
}; // 세미콜론 필수 !!!!

int main() {
    Animal animal; // 클래스의 instance animal 생성
    // print(animal.food) // private 변수임으로 객체 밖에서 접근이 불가능하다. 
    animal.set_animal(100, 50);
    animal.increase_food(30);

    animal.view_stat();
    return 0;
}