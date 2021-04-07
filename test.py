
def romanToInt( s):
    r = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    result = 0
    for x in range(0, len(s)):
        if x > 0 and r[s[x]] > r[s[x-1]]:
            take_away = r[s[x]] - r[s[x-1]]
            result += take_away - r[s[x-1]]
        else:
            result += r[s[x]]
    return result



romanToInt( "XVII")
romanToInt("LVIII")