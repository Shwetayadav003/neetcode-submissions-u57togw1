class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x,y,z = target
        found = [False, False, False]

        for a, b, c in triplets:

            if a <= x and b <= y and c <= z:

                if a == x:
                    found[0] = True
                if b == y:
                    found[1] = True
                if c == z:
                    found[2] = True

        return all(found)
        
        