class Solution {
public:
    char repeatedCharacter(string s) {
        char ch;
        unordered_set<char> st;
        for(auto i : s){
            if(st.find(i) != st.end()){
                ch = i;
                break;
            }
            else{
                st.insert(i);
            }
        }
        return ch;
    }
};