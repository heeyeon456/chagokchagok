#!/bin/bash

# 4. 쉘 스크립트
# 산술계산
# 정수형 변수저장

echo "1)declare" 
declare -i x

x=2#1111  #2진수
echo $x   # 15

x=8#17  #8진수
echo $x #15

x=16#f
echo $x

echo "2)let"
let ret=1+1
echo "1+1="$ret

#공백을 사용하려면 큰 또는 작은 따옴표를 사용해야한다.
let 'ret = 1 + 1'
echo "1 + 1 = " $ret

#거듭제곱 연산자
let ret=2**10
echo "2 ** 10 = " $ret

#복합대입 연산자
num=0
let num+=2
echo $num

#단항연산자
num=0
let ret=++num
printf "num = %d, ret = %d\n" $num $ret

num=0
let ret=num__
printf "num = %d, ret = %d\n" $num $ret

# 비교 연산자도 사용 가능하다
let ret=2\>0
echo $ret

let ret 2'>='0
echo $ret


