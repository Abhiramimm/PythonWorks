# program to count occurance of letters in a string (strings = "sample questions" output s:3)

text="sample questions"

wc={txt:text.count(txt) for txt in set(text)}
print(wc)