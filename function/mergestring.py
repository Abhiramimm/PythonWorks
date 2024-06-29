def mergestring(string1,string2):
    s1_length=len(string1)
    s2_length=len(string2)
    sm_length=s1_length if s1_length<s2_length else s2_length
    output=""
    for i in range(0,sm_length):
        output+=string1[i]+string2[i]
    rem=string1[s2_length:] if s1_length>s2_length else  string2[s1_length:]
    output+=rem
    return output
print(mergestring("ab","cde"))