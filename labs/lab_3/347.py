class Solution(object):
    def topKFrequent(self, nums, k):
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        sorted_items = sorted(freq.items(), key=lambda item: item[1], reverse=True)

        result = []

        for i in range(k):
            result.append(sorted_items[i][0])

        return result