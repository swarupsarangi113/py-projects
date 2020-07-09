import random
myList = []
n = int(input('How many times do you want to toss the coin : '))
i = 0
while i <= n :
    outcome = random.randint(0,1)
    if outcome == 0 :
        toss = 'H'
        myList.append(toss)
    elif outcome == 1 :
        toss = 'T'
        myList.append(toss)
    i += 1

print(myList)
headStreak = 0
total_H_Streak = 0

for i in myList :
    if i == 'H' :
        headStreak += 1
        if headStreak == 6 :
            total_H_Streak += 1
    else :
        headStreak = 0
print('The streak of 6 heads in a row is : ',total_H_Streak)
tailStreak = 0
total_T_Streak = 0
for j in myList :
    if j == 'T' :
        tailStreak += 1
        if tailStreak == 6 :
            total_T_Streak += 1
    else :
        tailStreak = 0
print('The Streak of 6 tails in a row is : ',total_T_Streak)
