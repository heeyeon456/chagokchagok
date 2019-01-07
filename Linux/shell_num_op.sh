#!/bin/bash

result=$(expr 2 + 2)
echo $result

var1=2
var2=2
result=$(expr $var1 ₩* $var2)    # *가 와일드카드로 처리되지 않도록 백슬래쉬나 따옴표를 사용한다.
echo $result

# 쉘에서는 정수 연산만 가능
expr 1 + 1
expr 1 - 1
expr 9 ₩* 9

# 비교 연산은 1또는 0을 반환한다
# 꺽쇠가 리다이렉션 연산자로 해석되지 않도록 백슬래시나 따옴표를 사용해야 한다.
expr 2 ₩> 1
expr 2 ₩>= 1
expr 1 != 0
expr 1 == 1

#논리 연산은 1또는 0을 반환한다
expr 1 ₩| 0
expr 1 ₩& 0


