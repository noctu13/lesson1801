S1 = 'Andrey, Matvey, Dmitry'
S2 = '01.01.23 02.04.22 07.08.20'
message = 'Happy Birthday'
S1 = [item.strip(',') for item in S1.split()]
S2 = S2.split()
D1 = {'Andrey': '01.01.23',
      'Matvey': '02.04.23',
      'Dmitry': '07.08.23',}
D2 = {'01.01.23': 'Andrey', # нужен такой
      '02.04.23': 'Matvey',
      '07.08.23': 'Dmitry',}

D3 = {}
for ind in range(len(S1)): #range(3) = [0, 1, 2]
    D3[S2[ind]] = S1[ind]

D4 = {}
for ind, item in enumerate(S1): 
    D4[S2[ind]] = item

D5 = {S2[ind]: item for (ind, item) in enumerate(S1)}
print(D2, D5)
#input_str = input()
#if input_str in D2:
#    print(message, D2[input_str])