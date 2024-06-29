def loweruppercount(text):
    lower=0
    upper=0
    for ch in text:
        if ch.islower():
            lower+=1
        else:
            upper+=1
    return(upper,lower)
print(f"(uppercase,lowercase):",loweruppercount("Python"))


# print(f"lowercase:{lower_case}",loweruppercount(text))






