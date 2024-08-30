class Solution {
public:
    int majorityElement(vector<int>& nums) {
        map<int , int> m;
        int M=0;
        int res;
        for(int i=0; i<nums.size();i++){
           m[nums[i]]++;
        }
        for(auto i = m.begin(); i!=m.end(); i++){
            if(i->second>M){
             M=i->second;
             res=i->first;
            }
        }
        return res;
    }
};