class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        _dict = {}

        for i in range(len(nums)):
            if (target - nums[i]) in _dict:
                return [_dict[target - nums[i]], i]
            _dict[nums[i]] = i

        return None
        