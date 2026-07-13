num=[1,2,45,33,54,66,55,76,87,97,73,21,45,79,89,36,18,-90]

max_score=0
for n in num:
    if n>max_score:
        max_score=n

print(max_score)

#------------------------------------------------------------------
min_score=0
for n in num:
    if n<min_score:
        min_score=n
print(min_score)

