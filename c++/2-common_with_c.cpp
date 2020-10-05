// 변수 정의
# include <iostream>

int main() {
    /*
    int i;
    char c;
    double d; 
    float f;

    int number_of_peeple; // 확실히 이해할 수 있는 변수 이름

    // 배열, 포인터 정의
    int arr[10];
    int *parr = arr;

    int i;
    int *pi = &i;

    //loop
    int i;
    for (i = 0; i < 10; i++) {
        std::cout << i << std::endl;
    }
     
    int sum = 0;
    for (int i = 0; i <= 10 ; i++) {
        sum += i;
    }
    std::cout << "합은 : " << sum << std::endl;

    int i = 1, sum = 0;
    while (i <= 10) {
        sum += i;
        i++;
    }
    std::cout << "합은: " << sum << std::endl;
    */
    //if else 문
    int lucky_number = 3;
    std::cout << "내 비밀 수를 맞추어 보세요~" << std::endl;
    
    int user_input;  // 사용자 입력
    
    while (1) {
        std::cout << "입력 : ";
        std::cin >> user_input;  // 표준 입력
        if (lucky_number == user_input) {
            std::cout << "맞추셨습니다~~" << std::endl;
            break;
        } 
        else {
            std::cout << "다시 생각해보세요~" << std::endl;
        }
  }
    return 0;
}