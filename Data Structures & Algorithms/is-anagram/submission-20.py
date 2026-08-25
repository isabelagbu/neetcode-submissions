class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}

        for sc in s:
            if sc in s_dict:
                s_dict[sc] += 1
            else:
                s_dict[sc] = 1

        for tc in t:
            if tc in t_dict:
                t_dict[tc] += 1
            else:
                t_dict[tc] = 1

        if s_dict != t_dict:
            return False
        else:
            return True