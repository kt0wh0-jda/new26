x = open('26(0).txt').read()

HarrySum = 0
KimSum = 0
for i in range(0, len(x), 3):
    print(x[i], x[i+1], x[i+2])
    if x[i] == x[i+2]:
        HarrySum+=1
    if x[i+1] == x[i+2]:
        KimSum+=1

print(HarrySum, KimSum)
print(abs(HarrySum - KimSum))
