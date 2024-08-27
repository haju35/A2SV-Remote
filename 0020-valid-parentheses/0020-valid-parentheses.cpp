class Solution {
    public:
     char getVal(char ch)
    {
        switch(ch)
        {
            case ']': return '[';
            case '}': return '{';
            case ')': return '(';
            default:return '\0';
        }
    }

    bool isValid(string s) {
        string opening = "({[";
        string closing = "]})";
        stack<char> st;

        for(char ch:s){
            if(opening.find(ch)!=-1)
            st.push(ch);
            else{
                if(st.empty()) return false;
                char tmp = st.top();
                st.pop();
                if(getVal(ch)!=tmp)
                return false;
            }
        }
        return st.empty();
        
    }
};