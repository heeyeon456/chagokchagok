computer 구조
- 메모리(반도체) : 반도체 한조각(bit-전기가 통하지 않으면 0, 통하면 1)
    - 반도체 조각을 이어 붙인 것 : 메모리
    - 8개 조각을 붙이면 1byte

    프로그램
    - 메모리 <-> cpu
- CPU
- 보조장치

- 하나의 process 에 대해서 cpu 가 다음과 같이 할당함
    - code segment
        - text area
        - string area (read-only)
    - data segment
        - global area (static)
        - heap
        - stack

- 1. loading
    - 기계어에 번역된(컴파일된) 코드를 code의 text area에 올려줌 - 함수메모리 할당)
    - binding ( 함수 호출 번지 결정, 함수 실행되는 데를 주소값으로 대치)
    - 전역변수나 static 변수를 global 영역에 할당
    - 지역변수를 stack 에 차곡차곡 쌓아 올려줌
    - 함수도 stack 에 올려주고, 복귀주소를 저장해줌
    - 함수가 다끝나면 메모리에서 차래로 해제

- 2. run
    - main부터 라인단위로 실행
