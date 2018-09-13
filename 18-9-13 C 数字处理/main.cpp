#include "header.h"
#include<stdio.h>
#include<math.h>
#define uint32_t unsigned int
#define uint8_t unsigned short
enum FilterAction {HIFIRST, LOFIRST};
uint32_t FilterDigits(uint32_t N, enum FilterAction action,  uint8_t pivot);

int main(){
 
    int test_n[] = {0, 54561559,54561559 ,236246306 ,236246306 ,111 ,111 , 842 , 842 , 58222212, 58222212};
    enum FilterAction test_action[] = {HIFIRST ,LOFIRST , HIFIRST,LOFIRST , HIFIRST,LOFIRST ,HIFIRST ,LOFIRST ,HIFIRST ,LOFIRST , HIFIRST};
    short test_pivot[] = {4 ,9 ,9 ,0 ,0 ,1 ,1 ,5 ,5 ,4 ,4 };

    uint32_t N = 58222212;
    uint8_t pivot = 4;
    for(int i = 0; i < 11; i++){
        FilterDigits(test_n[i], test_action[i], test_pivot[i]);
    }
    //FilterDigits(N, HIFIRST, pivot);
}
 
uint32_t FilterDigits(uint32_t N, enum FilterAction action,  uint8_t pivot){
    uint32_t left = 0; // Used to record the number should put at left of pivot 
    uint32_t right = 0;// // Used to record the number should put at right of pivot 
    uint32_t count = 0; // the length of an integer
    uint32_t pivot_num = 0; // Used to record the size of the number pivot 
    uint32_t pivot_len = 0; // Used to record the number of occurrences of pivot
    uint32_t ans = 0; // A temporary variable used to hold a number
    uint32_t tmp = N;// A temporary variable used to hold a number
    uint32_t right_num = 0; // The number of Numbers to the right of pivot
    
    while(tmp!=0){  // Used to get the length of an integer
        tmp/=10;
        count++;
    }
    
    for(int i = count - 1; i >= 0; i--){
        ans = N / (uint32_t)(pow(10, i));
        N %= (uint32_t)(pow(10, i));
        if(ans > pivot){
            if(action == HIFIRST){ // if the munber bigger than pivot should put at left
                left = left * 10 + ans;
            }
            else { // if the munber smaller than pivot should put at left
                right = right * 10 + ans;
                right_num++;
            }
        }
        else if(ans < pivot) {
            if(action == HIFIRST){ // if the munber bigger than pivot should put at left
                right = right * 10 + ans;
                right_num++;
            }
            else { // if the munber smaller than pivot should put at left
                left = left * 10 + ans;
            }
        }
        else { // if the
            pivot_num = pivot_num * 10 + pivot;
             pivot_len++;
        }
    }
    // Calculate the final output
    uint32_t result = left*(uint32_t)(pow(10, right_num+pivot_len)) + pivot_num*(uint32_t)(pow(10, right_num)) + right;
    printf("%d\n", result);
    return result;
}
