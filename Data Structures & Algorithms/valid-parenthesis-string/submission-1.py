class Solution:
    def checkValidString(self, s: str) -> bool:
        st = []
        cnt = Counter(s)
        star = []
        for i,c in enumerate(s):
            if c == '(' or c == '*':
                st.append(c)

            else:
                while st and st[-1] == '*':
                    star.append('*')
                    st.pop()
                    # print(st)
                if st and st[-1] == '(':
                    st.pop()
                    st.extend(star)
                    star = []
                elif not st and star:
                    star.pop()
                    st = star.copy()
                    star = []
                else:
                    return False
        # print(st)
        # print(star)
        while st:
            if st[-1] == '*':
                st.pop()
                star.append('*')
            else:
                if star:
                    st.pop()
                    star.pop()
                else:
                    return False
        return not st