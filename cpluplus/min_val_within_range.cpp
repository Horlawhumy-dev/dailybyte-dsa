#include <bits/stdc++.h>

using namespace std;


int solution(vector<int> numbers, vector<int> nRange) {
    /* T(C) => O(n)
       S(C) => O(1)
    */
    if (numbers.empty() || nRange.size() < 2) {
        return 0;
    }
    
    int minValWithInRange = INT_MAX;
    int firstRangeNum = nRange[0];
    int lastRangeNum = nRange[1];
    
    for (int num: numbers) {
        
        if (firstRangeNum < num && num < lastRangeNum) {
            minValWithInRange = min(minValWithInRange, num);
        }
    }
    
    // guide against no minimum value
    if (minValWithInRange < INT_MAX) {
        return minValWithInRange;
    }
    
    return 0;
}