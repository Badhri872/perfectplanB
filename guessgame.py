import random
import numpy as np

def word_selection(word_length):
    list = open('wordlist.txt')
    list1=[]
    list2=[]
    for words in list:
        words = words.strip().lower()
        list1.append(words)
    for word in list1:
        if len(word)>=word_length:
            list2.append(word)
        else:
            continue
    #print(list2)
    word_select = random.choice(list2)
    return word_select

i=True
j=True
s = ""
while i==True:
    Totalattempts = input('How many incorrect attempts do you want?[1-6]')
    try:
        attempts = int(Totalattempts)
        if 1<=attempts<=6:
            i=False
            break
        else:
            print("Please enter the attempts between 1 - 6")
            continue
    except:
        print('Please enter the valid attempt in integer')
        continue

while j==True:
    Max_word = input('What minimum word length do you want?[4-10]')
    try:
        word_length = int(Max_word)
        if 4<=word_length<=10:
            j=False
            break
        else:
            print('Please enter the word length between 4-10')
            continue
    except:
        print('Please enter the valid word length in integer')
        continue

print('Selecting a word...')
word_set_1 = word_selection(word_length)
word_set = word_set_1
guesses = ''
attempt_len = 0
guess = ['*'*len(word_set)]
judge = [False for i in range(len(word_set))]
#print(len(word_set))
finished = False
while attempts!=0 and finished==False:
    print('Word:{0}'.format(s.join(guess)))
    guess = []
    print('Attempts Remaining:{0}'.format(attempts))
    print('Previous Guesses:{0}'.format(guesses))
    guesses=input('Choose next letter:')
    for letter in range(len(word_set)):
        if word_set[letter]==guesses or judge[letter]==True:
            guess.append(word_set[letter])
            if judge[letter]!=True:attempt_len +=1
            judge[letter]=True
        else:
            guess.append('*')


    if attempt_len==0:
        attempts -=1
        print('Letter not present in the word')

    else:
        print('Letter present in the word')
        attempt_len=0

    if '*' not in guess:
        finished=True
        break


else:
    print('Sorry,Better luck next time')

if attempts!=0:print('Congrats you find the word')
