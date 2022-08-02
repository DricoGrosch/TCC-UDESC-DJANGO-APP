sus_array = [5,	1,	5,	1,	3,	1,	4	,1,	5,	1]
total = 0
for idx, answer in enumerate(sus_array, 1):
    if idx % 2 == 1:
        total += (answer - 1)
    else:
        total += (5 - answer)
total *= 2.5
print(total)



# 82.5
# 90
# 87.5
# 97.5
# 90