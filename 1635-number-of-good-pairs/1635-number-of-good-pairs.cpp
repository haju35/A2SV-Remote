class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
       int count = 0;
       vector<int> freq(101,0);
        for(int num:nums)
          count += freq[num]++;
         return count;
        
    }
};