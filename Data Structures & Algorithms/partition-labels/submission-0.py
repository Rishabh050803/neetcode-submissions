class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        frq = Counter(s)
        # print(frq)
        ans = []
        cnt = 0

        def chcek(j,cnt):
            i = j - cnt + 1

            for k in range(i,j+1):
                if frq[s[k]] > 0:
                    return False
            return True
        for j,c in enumerate(s):
            cnt += 1
            frq[c]-=1
            # print(j,cnt,frq[c])
            if frq[c] <= 0:
                if chcek(j,cnt):
                    ans.append(cnt)
                    cnt = 0
        return ans

