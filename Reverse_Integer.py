class Solution:
    def reverse(self, x: int) -> int:
        p = abs(x)
        a = [0]*len(str(x))
        count = 0
        while p != 0:
            a[count] = p % 10
            p = p // 10
            count += 1

        s = [str(i) for i in a]
        
        if int("".join(s)) % 10 == 0:
            s=s[:-1]

        if x == 0 or int("".join(s)) > 2**31 - 1:
            return 0
        else:
            if x < 0:
                return int('-' + "".join(s))
            else:
                return int("".join(s))
