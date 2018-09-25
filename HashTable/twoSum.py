#!/usr/bin/env python
#-*- coding:utf-8 -*-

class Solution(object):
    def twoSum_naive(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        朴素想法实现：
        1.先求得差值
        2.判断列表中是否有该值，若有则执行3，若无则继续循环
        3.判断其是否等于被减数，若相等则执行4，若不等则返回结果
        4.判断是否和被减数为同一个数，若否则返回结果，若是则继续循环
        """
        rlt = []
        for i in range(len(nums)):
            diff = target - nums[i]
            if not diff in nums:
                continue
            else:
                if diff != nums[i]:
                    rlt = [i, nums.index(diff)]
                    break
                elif nums.count(diff) == 1:
                    continue
                else:
                    nums.pop(i)
                    rlt = [i, nums.index(diff)+1]
                    break
        return rlt

    def twoSum_hash(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        1.建立字典存储差值和其对应位置
        2.若字典中存在该值，则返回其对应的value；若不存在，则将差值作为key，序号作为value存入字典。
        """
        diff_buff = {}
        for i in range(len(nums)):
            if nums[i] in diff_buff:
                return [diff_buff[nums[i]],i]
            else:
                diff_buff[target-nums[i]] = i
        return []
        
