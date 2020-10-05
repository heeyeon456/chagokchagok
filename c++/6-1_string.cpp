#include <iostream>
#include <string>

int main() {
    std::string s = "abc";
    std::string t = "def";
    std::string s2 = s;

    std::cout << s <<" 의 길이 : " << s.length() << std::endl; // 문자열 길이
    std::cout << s << " 뒤에 " << t << " 를 붙이면: " << s + t << std::endl;  // string 결합

    if (s == s2) { // c의 경우 strcmp 를 이용해야 함
        std::cout << s << " 와 " << s2 << " 는 같다 " << std::endl;
    }
    if (s != t) {
        std::cout << s << " 와 " << t << " 는 다르다 " << std::endl;
    }
    return 0;
}