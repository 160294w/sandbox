N = int(input())
S = list(input())
count = 0

for i in range(0, len(S)):
    if count % 2 == 0:
        if S[i] == ',':

            S[i] = '.'
        else:
            pass
    if S[i] == '"':
        count += 1

print(''.join(S))

