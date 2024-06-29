students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

scores = []
names = []

for student in students:
    scores.append(student[-1])
    
sec_lowest = sorted(scores)[1]

for name, score in students:
    if score == sec_lowest:
        names.append(name)
        names.sort()
        
print("\n".join(names))