import random
name=input('heyy! whats ur name :')
print('good luck', name)

words=['python','cat','developer','english','watch','arduino','red','turquoise','cyan','programming','microsoft','ambassadors','error']
word=random.choice(words)
tries=15
guesses=''
while tries>0:
    fail=0
    for c in word:
        if c in guesses:
            print(c,end='')
        else:
            print('_',end=' ')
            fail+=1
    print()
    if fail == 0:
        print('you win\nthe word was {}'.format(word))
        break
    guess=input('guess a character :')
    if guess in guesses:
        print('you cant guess the same character again!')
        continue
    guesses+=guess
    
    if guess not in word:
        tries-=1
        print('wrong!\nyou have {} guesses left'.format(tries))
        if tries==0:
            print('you lose :( better luck next time!')
