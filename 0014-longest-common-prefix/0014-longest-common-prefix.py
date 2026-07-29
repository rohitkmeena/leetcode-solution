class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        fix = strs[0]

        for word in strs[1:]:
            while not word.startswith(fix):
                fix = fix[:-1]

                if fix == "":
                    return ""

        return fix
        
       
