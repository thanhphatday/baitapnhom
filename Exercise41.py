x=int(input("Octave: "))
N=str(input("Note: "))
f1 = 261.63
f2 = 293.66
f3 = 329.63
f4 = 349.23
f5 = 392.00
f6 = 440.00
f7 = 493.88
if x==4:
    if N=="D":
        print(f2)
    if N=="E":
        print(f3)
    if N=="F":
        print(f4)
    if N=="G":
        print(f5)
    if N=="A":
        print(f6)
    if N=="B":
        print(f7)
if N=="C" and 0<=x<=8:
    
    F=(261.63)/(2**(4-x))
    print(F)
