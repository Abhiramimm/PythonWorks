def vowelscount(string):
    vowels=["a","e","i","o","u"]
    wc={ch:string.count(ch) for ch in set(string) if ch in vowels}
    return wc
print(vowelscount("welcome python"))