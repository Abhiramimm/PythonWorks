def anagram(sourceword,targetword):
    srt_sourceword=sorted(sourceword)
    srt_targetword=sorted(targetword)
    if srt_sourceword==srt_targetword:
        print("anagram")
    else:
        print("not anagram")
anagram("listen","silent")