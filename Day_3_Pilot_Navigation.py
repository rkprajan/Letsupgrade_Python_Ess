el=input('Emergency Landing for upcoming station: Y or N :').lower()
if el == 'y':
    while True:
        att=int(input('Enter your current Altitude(ft) :'))
        if att < 3000:
            print('\n')
            print('For landing here,You have to achieve 3000ft...')
            break
        elif att >= 3000 and att <= 6000:
            if att == 3000:
                print('\n')
                print('You can come and land here...')
                break
            else:
                print('\n')
                print('You have to come 3000ft and land here with pleasure...')
                break
        else:
            print('Your are more than 6000ft ,so have to request next station for landing...')
            print('Please Enter your Altitude below again ........... ')
else:
    print('Looks like your good....have a happy journey...!')