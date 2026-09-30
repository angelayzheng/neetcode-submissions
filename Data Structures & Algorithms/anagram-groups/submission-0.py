class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = {}

        for s in strs:
            a = "".join(sorted(s))

            if a in anagrams:
                anagrams[a].append(s)

            else:
                anagrams[a] = [s]

        return list(anagrams.values())