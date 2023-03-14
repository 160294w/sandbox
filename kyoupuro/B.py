N, M = map(int,input().split())

people = []
for i in range(N):
     people.append(int(input().replace('o','1').replace('x','0'),2))

score = 0
#print(people)
for i in range(N):
     for j in range(i+1, N):
          if people[i] | people[j] == pow(2,M)-1:
#               print(people[i], people[j], people[i] | people[j])
               score += 1

print(score)               
               
     
