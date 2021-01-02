class Solution:
    def twoSum(self, numList, target):
        hashmap = {}
        for index, ele in enumerate(numList):
            if target - ele in hashmap:
                return [hashmap[target-ele],index]
            else:
                hashmap[ele]=index
