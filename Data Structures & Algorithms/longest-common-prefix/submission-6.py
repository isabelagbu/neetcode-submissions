class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = []

        for i in range(len(strs[0])):
            for j in strs:
                if i == len(j) or strs[0][i] != j[i]:
                    return "".join(common)
            common.append(strs[0][i])
        return "".join(common)
        