x = open('26(1).txt').read()
while '10' in x:
    x = x.replace('10', 'A')

HarrySum = 0
KimSum = 0

HarryStreak = 0
KimStreak = 0

for i in range(0, len(x), 4):
    val = int(x[i+3], 16)
    if x[i] == x[i+2]:
        HarryStreak += 1
        HarrySum += HarryStreak * val
    else:
        HarryStreak = 0

    if x[i+1] == x[i+2]:
        KimStreak += 1
        KimSum += KimStreak * val
    else:
        KimStreak = 0


print(max(HarrySum, KimSum))
