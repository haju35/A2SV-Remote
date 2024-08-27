class Solution {
public:
    int arithmeticTriplets(vector<int>& nums, int diff) {
        int result = 0;

        for(int i : nums){
            if(count(nums.begin(), nums.end(), i + diff) && count(nums.begin(),
            nums.end(), i + diff + diff)) result++;
        }
        return result;
        
    }
};