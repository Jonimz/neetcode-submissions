class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map= defaultdict(list)

        for words in strs: 
            key = ''.join(sorted(words))
            if key in anagram_map:
                anagram_map[key].append(words) 
            else:
                anagram_map[key] = [words]

        return list(anagram_map.values())
          