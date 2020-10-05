#include <iostream>

class Date {
    int year_;
    int month_;  // 1 부터 12 까지.
    int day_;    // 1 부터 31 까지.
    public:
    void SetDate(int year, int month, int date);
    void AddDay(int inc);
    void AddMonth(int inc);
    void AddYear(int inc);
    void ShowDate();

    // 생성자 오버로딩
    // 생성자
    Date(int year, int month, int day) {
        std::cout << " 인자 3 생성자 호출" << std::endl;
        year_ = year;
        month_ = month;
        day_ = day;
    }
    //디폴트(default) 생성자
    Date() {
        std::cout << "디폴트 생성자 호출" << std::endl;
        year_ = 2011;
        month_ = 2;
        day_ = 26;
    }
    // 명시적 디폴트 생성자
    // Date() = default;
};
void Date::SetDate(int year, int month, int date) {
    year_ = year;
    month_ = month;
    day_ = date;
}
void Date::AddDay(int inc){
    int div = 0;
    if (month_ == 4 || month_ == 6 || month_ == 9 || month_ == 11) {
        div = 31;
    }
    else if (month_ == 2) {
        div = 29;
    }
    else {
        div = 32;
    }
    month_ = month_ + (day_+inc)/div ;
    day_ = (day_+inc) % div;
}
void Date::AddMonth(int inc) {
    month_ = (month_+inc) % 13;
}
void Date::AddYear(int inc) {
    year_ = year_ + inc;
}
void Date::ShowDate() {
    std::cout << "오늘 날짜는 " << year_ << "년 " << month_ << "월 " << day_ << "일입니다." << std::endl;
}
int main() {
    // 생성자와 함께 정의
    Date date(2012, 2, 28); // implicit
    // Date date = Date(2012, 2, 28); // explicit

    // 아까처럼 생성자를 정의하지 않았을 때도 생성자가 호출될까? -> yes
    // Default Constructor 가 호출된다 (컴파일러가 자동으로 추가해주는 생성자)
    Date date2 = Date();
    date2.ShowDate();

    date.ShowDate();
    date.AddDay(3);
    date.AddMonth(3);
    date.AddYear(3);
    date.ShowDate();

}