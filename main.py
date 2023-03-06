with open('readme.txt') as f:
    con = f.read()

Pword = con
Pwordinput = input('What is the password: ')

while Pwordinput != Pword:
    Pwordinput = input('Wrong! What is the password: ')

print('You are in.')
print('Rules: put all your answers in lowercase, do not say bad things to him, and do not call him a funny guy!')

while True:
    ASK = input('What do you want to know: ')
    
    if 'joke' in ASK:
        print('Why did the chicken cross the road?')
        if 'yes' in input('Would you like to hear the answer?'):
            print('Because he wanted to go to the other side.')
            print('Ha, Ha, Ha, Ha!!')
            print('Too much laughing')

    if 'ha' in ASK:
        print('What is funny. >:( ')

    if 'you are' in ASK:
        if 'funny' in ASK:
            FY = 'But I am funny.'
        if 'funny' not in ASK:
            FY = 'Hmph!'
        print('How dare you. I take that as an insult. >:( ', FY)

    if 'change' and 'password' in ASK:
        if 'yes' in input('would you like to view your current password: '):
            print('Your current password is', Pword)
            if 'yes' in input('Would you like to change the password: '):
                if 'yes' in input('Are you sure you want to continue: '):
                    if Pword in input('Old password: '):
                        CPword = input('What is the new password: ')
                        CCPword = input('Please confirm your password: ')
                        if CPword == CCPword:
                            with open('readme.txt', 'w') as f:
                                f.write(CPword)
                                print('Password saved.')
