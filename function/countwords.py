def countwords(string):
    wc={ch:string.count(ch) for ch in set(string)}
    return wc
string="hello"
print(countwords(string))