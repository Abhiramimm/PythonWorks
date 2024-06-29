def kangaroo(sourceword,targetword):
    wc={ch:sourceword.count(ch)for ch in set(sourceword)}
    for ch in targetword:
        if ch in wc and wc.get(ch)>0:
            wc[ch]-=1
        else:
            print("not kangaroo word")
            break
    else:
        print("kangaroo")
kangaroo("container","can")