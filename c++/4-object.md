### 4-1. object
---
* 객체(object): 변수들과 참고자료들로 이루어진 소프트웨어 덩어리
    - encapsulated entity with state and behavior
    - 객체가 현실 세계에서 존재하는 것들을 나타내기 위해서는 추상화(abstraction) 이라는 과정이 필요하다!
        - 추상화: 현실세계의 것들을 컴퓨터에서 처리할 수 있도록 바꾸는 것
       - 전화를 한다, 문자를 보낸다 -> 핸드폰을 하는 것 (추상화)
    - 객체 내의 변수들은 외부로부터 보호되어 있기 때문에, 외부에서 어떤 객체의 instance 변수 value 를 바꾸지 못한다. 
    - Encalsulation(캡슐화): 외부에서 인스턴스 변수를 바꿀 때 항상 인스턴스 메소드를 통하여 간접적으로 조절하는 것
        - 객체가 내부적으로 어떻게 작동하는지 몰라도 사용할 수 있게 된다.
    - objects must have externally observable behavior(주특기) as a result of performing operation
* entity: conceptual attribute that have uinque identities
* class
    - 객체의 설계도
    - repository for behaviro and the internal representation
    - cookie cutter that makes cookies 
* ood: 서로 독립적인 하나의 객들이 서로 폅력하여 문제를 해결해가는 형태의 프로세스 
* overloading (오버로딩): 같은 이름의 다른 method가 하나의 class에 존재할 때
    - compiler 가 함수를 오버로딩 하는 방법
    - 1 단계 :자신과 타입이 정확히 일치하는 함수를 찾는다.
    - 2 단계 : 정확히 일치하는 타입이 없는 경우 아래와 같은 형변환을 통해서 일치하는 함수를 찾아본다.
        - Char, unsigned char, short 는 int 로 변환된다.
        - Unsigned short 는 int 의 크기에 따라 int 혹은 unsigned int 로 변환된다.
        - Float 은 double 로 변환된다.
        - Enum 은 int 로 변환된다.
    - 3 단계: 위와 같이 변환해도 일치하는 것이 없다면 아래의 좀더 포괄적인 형변환을 통해 일치하는 함수를 찾는다.
        - 임의의 숫자(numeric) 타입은 다른 숫자 타입으로 변환된다. (예를 들어 float -> int)
        - Enum 도 임의의 숫자 타입으로 변환된다 (예를 들어 Enum -> double)
        - 0 은 포인터 타입이나 숫자 타입으로 변환된 0 은 포인터 타입이나 숫자 타입으로 변환된다
        - 포인터는 void 포인터로 변환된다.
    - 4 단계
    - 유저 정의된 타입 변환으로 일치하는 것을 찾는다 (이 부분에 대해선 나중에 설명!)(출처)
    - 만약에 컴파일러가 위 과정을 통하더라도 일치하는 함수를 찾을 수 없거나 같은 단계에서 두 개 이상이 일치하는 경우에 모호하다 (ambiguous) 라고 판단해서 오류를 발생하게 됩니다.