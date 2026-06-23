class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create a hashmap where each key is the sorted version of a string

       group = defaultdict(list)
       for word in strs:
         key = ''.join(sorted(word))
         group[key].append(word)
       return list(group.values())



        