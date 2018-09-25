class Solution(object):
    def threeSum_twoPointer(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        rlt = []
        nums.sort()
        if len(nums)<3 or nums[0]>0 or nums[-1]<0:
            return []
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            head, rear = i+1, len(nums)-1
            while head<rear:
                sum_ = nums[i] + nums[head] + nums[rear]
                if sum_ < 0:
                    head += 1
                elif sum_ > 0:
                    rear -= 1
                else:
                    rlt.append([nums[i], nums[head], nums[rear]])
                    while head<rear and nums[head] == nums[head+1]:
                        head += 1
                    while head<rear and nums[rear] == nums[rear-1]:
                        rear -= 1
                    head += 1
                    rear -= 1
        return rlt
        
        
    def threeSum_naive(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        朴素想法：
        1.每次pop最末端的元素
        2.剩下的列表是twoSum problem的变形（需返回全部结果）
        3.除去重复解
        rlt:10%
        """
        def twoSum(nums, target):
            diff_buff = {}
            rlt = {}
            for i in range(len(nums)):
                if nums[i] in diff_buff:
                    rlt[target-nums[i]] = nums[i]
                else:
                    diff_buff[target-nums[i]] = i
            return rlt
        rlt_buff = {}
        nums.sort(reverse = True)
        if (not nums) or nums[-1] > 0 or nums[0] < 0 or len(nums)<3:
            return []
        while len(nums)>=3:
            rear = nums.pop()
            if rear > 0:
                break
            temp = twoSum(nums, -rear)
            if not temp:
                continue
            if rear not in rlt_buff:
                rlt_buff[rear] = temp
            else:
                rlt_buff[rear].update(temp)
        rlt = []
        for k,v in rlt_buff.items():
            for key,val in v.items():
                rlt.append([k, key, val])
        return rlt
        
        
        
