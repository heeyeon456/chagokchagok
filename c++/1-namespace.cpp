#include <iostream>

namespace {
    // 이 함수는 이 파일 안해서만 사용할 수 있음
    // c의 static과 비슷한 기능
    // static int OnlyInThisFile() 과 동일
    int OnlyInThisFile() {}

    // static int x 와 동일
    int only_in_this_file = 0;
}

int main() {
    OnlyInThisFile();
    only_in_this_file = 3;
}
