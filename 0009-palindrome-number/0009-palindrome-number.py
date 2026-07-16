class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if x == x[::-1] :
          return True
        else:
          return False

        # x = str(x)
        # first, *all, last = x
        # if first == last:
        #   return True
        # else:
        #   return False