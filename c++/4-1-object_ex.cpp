#include <iostream>

class Date {
    int year_;
    int month_;  // 1 부터 12 까지.
    int day_;    // 1 부터 31 까지.
    public:
    void SetDate(int year, int month, int date) {
        year_ = year;
        month_ = month;
        day_ = date;
    }
    void AddDay(int inc){
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
    void AddMonth(int inc) {
        month_ = (month_+inc) % 13;
    }
    void AddYear(int inc) {
        year_ = year_ + inc;
    }
    void ShowDate() {
        std::cout << "오늘 날짜는 " << year_ << "년 " << month_ << "월 " << day_ << "일입니다." << std::endl;
    }
};

int main() {
    Date date;
    date.SetDate(2012, 2, 28);
    date.ShowDate();
    date.AddDay(3);
    date.AddMonth(3);
    date.AddYear(3);
    date.ShowDate();

}
