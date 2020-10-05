#include <stdio.h>
#include <stdlib.h>
// 동적 메모리 할당
// heap 은 사용자가 자유롭게 할당하거나 해제할 수 있음

int main(int argc, char **argv) {
    int SizeOfArray;
    int *arr;

    /*printf("만들고 싶은 배열 원소의 수: ");
    scanf("%d", &SizeOfArray);

    //memory allocation (malloc)
    //원래 리턴형이 (void*) 니깐 이것을 (int*)로 형변환 하여
    arr = (int*)malloc(sizeof(int) * SizeOfArray);

    // 할당했던 메모리를 다시 해제함
    // free를 제대로 하지 않으면 메모리 누수 (memory leak ) 현상이 일어남
    free(arr);*/

    // 2차원 배열 동적할당
    int i;
    int x, y;
    int **arr2; // 2차원 배열 만들것

    printf("arr[x][y] 를 만들 것입니다.\n");
    scanf("%d %d", &x, &y);

    arr2 = (int **)malloc(sizeof(int *) *x); // int* 형 원소를 x개 가지는 배열 생성)

    for (i = 0; i < x; i++) {
        arr2[i] = (int*)malloc(sizeof(int)*y); // 배열의 각 원소들에 메모리 공간 할당
    }
    printf("생성 완료! \n");

    for (i = 0; i < x; i++) {
        free(arr2[i]);
    }
    free(arr2);
    return 0;
}