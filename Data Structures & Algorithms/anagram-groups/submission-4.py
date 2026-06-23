class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)  # Dictionary to hold grouped anagrams

        for word in strs:
            # Sort the word to use as a key
            key = ''.join(sorted(word))
            anagram_map[key].append(word)  # Group all words with the same sorted key

        return list(anagram_map.values())
        