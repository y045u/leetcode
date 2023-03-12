class Solution:
    def singleNumber(self, nums) -> int:
        """
        ・"a ^= b"とは
            排他的論理和。a = a ^ bと同じ。
            同じ数字を排他的論理和を行うと0になるため
            最後まで処理をすると、今回のペアのない数字が浮かび上がる
        """
        ans = 0
        for i in nums:
            ans ^= i
        return ans
    
a = Solution
nums = [4,1,2,1,2]
a.singleNumber(a, nums)