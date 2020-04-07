from .maxProfit import printResult

class Solution:
    @printResult
    def groupAnagrams(self, strs: list) -> list:
        if strs is None:
            return []

        d = {}
        for string in strs:
            chars = list(string)
            chars.sort()
            sortedString = ''.join(chars)

            if sortedString in d:
                d[sortedString].append(string)
            else:
                d[sortedString] = [string]

        results = []
        for key in d:
            results.append(d[key])

        return results

if __name__ == '__main__':
    scanner = Solution()
    scanner.groupAnagrams(None)
    scanner.groupAnagrams([])
    scanner.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    scanner.groupAnagrams(['pseudopseudohypoparathyroidism'
                           , 'pesudopseudohypoparathyroidism'
                           , 'pseudopseudohypoparathyroiidsm'])