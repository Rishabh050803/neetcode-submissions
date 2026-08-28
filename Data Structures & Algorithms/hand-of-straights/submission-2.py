class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        mp = Counter(hand)
        hand.sort()

        for x in hand:
            if mp[x] <= 0:
                continue
            t = x
            s = groupSize
            while s > 0:
                if mp[t] > 0:
                    mp[t] -= 1
                else:
                    return False
                t += 1
                s -= 1

        return True