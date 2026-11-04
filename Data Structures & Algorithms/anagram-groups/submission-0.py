class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}
        for wrd in strs:
            key = "".join(sorted(wrd))

            if key not in my_dict:
                my_dict[key] = []
            my_dict[key].append(wrd)

        return [v for _,v in my_dict.items()]


