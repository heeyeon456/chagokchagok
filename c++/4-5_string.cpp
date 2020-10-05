#include <iostream>

class MyString {
    char* str;
    int str_length;
    public:
        MyString(char c);
        MyString(const char* string);
        MyString(const MyString& str);
        ~MyString();
        int strlen(const char* string) const;
        void println() const;
        char* concat(MyString* substr);
        char find(MyString* key);
        int strcmp(char* str1, char* str2);
        int strlen_cmp(char* str1, char* str2);
};
MyString::MyString(char c) {
    str = new char[1];
    str[0] = c;
    str_length = 1;
}
MyString::MyString(const char* string) {
    str_length = strlen(string);
    std::cout << str_length << std::endl;
    str = new char[str_length];
    for(int i=0; i<str_length; i++) str[i] = string[i];
}
MyString::MyString(const MyString& string) {
    str_length = string.str_length;
    str = new char[str_length];
    for (int i=0; i < str_length; i++) {
        str[i] = string.str[i];
    }
}
MyString::~MyString() { delete[] str; }
int MyString::strlen(const char* string) const {
    int i;
    for (i=0; string[i] != '\0'; ++i);
    return i;
}
void MyString::println() const {
    for(int i=0; i<str_length; i++) {
        std::cout << str[i] ;
    }
    std::cout << std::endl;
}

int main() {
    MyString str1("hello world");
    MyString str2(str1);

    str1.println();
    str2.println();

    return 0;   
}