#This is a Rock,Paper,Scissors game
import random , sys
print('ROCK, PAPER, SCISSORS')
win = 0
loss = 0
tie = 0
c_move = ''
while True :
    print(win,'Wins, ',loss,'Losses, ',tie,'Ties')
    h_move = input('Enter your move: (r)ock (p)aper (s)cissors or (q)uit ')
    if h_move == 'q' :
        sys.exit()
    r_num = random.randint(1,3)
    #display what human choose
    if h_move == 'r' :
        print('ROCK versus...')
    elif h_move == 'p' :
        print('PAPER versus...')
    elif h_move == 's' :
        print('SCISSORS versus...')

    #display what computer choose
    if r_num == 1 :
        c_move = 'r'
        print('ROCK')
    elif r_num == 2 :
        c_move = 'p'
        print('PAPER')
    elif r_num == 3 :
        c_move = 's'
        print('SCISSORS')

    if h_move == c_move :
        print('It is a tie! ')
        tie += 1
    #if human choose rock
    elif h_move == 'r' and c_move == 'p' :
        print('You Lose!')
        loss += 1
    elif h_move == 'r' and c_move == 's' :
        print('You Wins!')
        win += 1
    #if human choose paper    
    elif h_move == 'p' and c_move == 'r' :
        print('You Win!')
        win += 1
    elif h_move == 'p' and c_move == 's' :
        print('You Lose!')
        lose += 1
    #if human choose scissors
    elif h_move == 's' and c_move == 'r' :
        print('You Lose!')
        lose += 1
    elif h_move == 's' and c_move == 'p' :
        print('You Win!')
        win += 1
        
