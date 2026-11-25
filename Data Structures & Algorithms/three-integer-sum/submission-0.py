class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()

        for i in range(len(nums) - 2):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            a = nums[i]
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[left] + nums[right]

                if total == -a:
                    output.append([a, nums[left], nums[right]])

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < -a:
                    left += 1

                else:
                    right -= 1

        return output