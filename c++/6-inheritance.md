## inheritance
---
* 상속 : is-a and has-a
``` class Manager : public Employee ```
    - Manager 클래스는 Employee 의 모든 기능을 포함한다.
    - Manager 클래스는 Employee 클래스의 모든 기능을 수행할 수 있기 때문에 Manager를 Employee로 칭해도 무방하다.
    - Manager "is-a" Employee (모든 Manager는 Employee 다.)
    - up-casting 가능 (파생 클래스에서 기반 클래스로 캐스팅 하는 것)
        - 부모 클래스의 reference 변수에 자식 클래스 instance 를 대입할 수 있다.  
- 클래스가 파생될수록 좀 더 구체화된다 (specialize)
- 거슬로 올라갈수록 더 일반화된다 (generalize림
``` class EmployeeList ```
    - EmployeeList 는 Employee 와 has-a 관계이다. 
    - Employee를 포함하고 있다.

* 오버라이딩(overriding): 상속받은 클래스가 가지고 있는 클래스를 재정의해서 사용하는 것
- ( 오버로딩 : 한 클래스 내에서 같은 이름의 메서드를 여러개(인자를 달리하여) 가지고 있는 것)

* ** virtual 함수 ** : 컴파일러 상에서 어떤 함수가 실행될지 정해지지 않고 run time 시에 정해지게 하는 것 (동적 바인딩 - Dynamic Binding)
    - 모든 함수들을 virtual 로 만들면 안되나???? -> 자바의 경우는 모든 함수가 디폴트로 virtual 로 선언됨
    - 가상 함수를 사용하게 되면 overhead 가 생길 수 있음
    -> 가상함수 테이블을 만듬 -> 일일이 찾아야 하니깐 시간이 더 오래걸림
* 다형성 (polymorphism): 하나의 메소드를 호출했음에도 불구하고 여러가지 다른 작업들을 하는 것

* pure virtual function and abstract clas능
```
class Animal {
    public:
        Animal() {}
        virtual ~Animal()
        virtual void speak() = 0;
}
class Dog : public Animal {
    public:
        Dog() : Animal() {점
        void speak() override { std::cout << "왈왈" << std::endl; }
}
```
- 함수의 몸통이 정의되지 않고 단순히 =0; 으로 처리하는 가상함수
    -> 반드시 오버라이딩 되어야만 하는 함수
    -> 완전한 가상함수 (pure virtual function)
    -> 함수를 호출하는 것이 불능, animal 객체를 생성하는 것도 불가능
- 추상클래스(Abstract class)
    - 순수가상함수를 최소 한개이상 포함하고 있는 (반드시 상속되어야 하는 클래스)
    - 왜 사용? -> 설계도
    - 이 기능은 일반적인 상왕에서 만들기 힘드니 너가 직접 특수화되는 클래스에 맞추어서 만들어서 써라

* 다중상속 (multiple inheritance)
- 한 클래스가 다른 여러 개의 클래스를 상속 받는 것을 허용 (java와의 차이점)
- 주의해야 할 점
    - 같은 이름의 멤버 변수나 함수가 있는 경우 이에 접근할 떄 오류가 발생함
    - 다이아몬드 상속(diamond inheritance) -> virtual 로 정의하면 해결할 수 있음
- 다중 상속을 사용해야 하는 경우
    - ex) 차량에 관한 클래스를 생성한다고 생각할 때, 종류는 땅, 물, 하늘, 우주에서 다니는 차 / 동력원: 휘발유, 풍력, 전기
     - 해결책
        - 브리지 패턴: 한가지 카테고리를 멤버의 포인터로 만들기
            - Engine -> 땅, 물, 하늘, 우주, 휘발유, 풍력, 전기
            - N x M 케이스에 대한 섬세한 제어는 불가능함
        - 중첩된 일반화 방식: 최대 N x M  조합의 파생클래스를 생성함
            - 땅_휘발유, 물_우주 ..음
        - 다중상속
            - 땅_휘발유는 땅이랑 휘발유 클래스로부터 상속받음