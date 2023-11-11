de=int(input('Enter a number of decibel: '))
if de<40: print('40dB is the quietest noise in the table')
elif de==40: print('Noise: Quiet room')
elif de>40 and de<70:
    print(de,'dB is between Quiet room and Alarm room',sep='')
elif de==70: print('Noise: Alarm room')
elif de>70 and de<106: 
    print(de,'dB is between Alarm room and Gas lawnmover',sep='')
elif de==106: print('Noise: Gas lawnmover')
elif de>106 and de<130:
    print(de,'dB is between Gas lawnmover and Jackhammer',sep='')
elif de==130: print('Noise: Jackhammer')
else: print('130dB is the loudest in the table')
