def coder(s):
    i = 0
    a = ""
    while i < len(s):
        if i == len(s) - 1:
            a += s[i]
        else:
            a += s[i+1] + s[i]
        i += 2
    return a

print(coder("adem"))