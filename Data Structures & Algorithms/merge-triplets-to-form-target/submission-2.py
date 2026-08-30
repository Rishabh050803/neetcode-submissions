class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        valid = [0,0,0]
        for x,y,z in triplets:
            if x > target[0] or y > target[1] or z > target[2]:
                continue
            valid[0] = max(valid[0],x)
            valid[1] = max(valid[1],y)
            valid[2] = max(valid[2],z)
        
        return valid == target