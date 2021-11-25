x=0;
y=0;

print('\nTo exit input direction "e"')

while True:
    while True:
        try:
            dir = input('\nInput direction (r, l, f, b): ')
            if not(['r', 'l', 'f', 'b', 'e'].__contains__(dir)):
                raise ValueError
            break
        except ValueError:
            print('direction can only be r, l, f or b (right, left, forward, back)')

    if (dir=='e'):
        break       

    while True:
        try:
            dis = input('Input distance: ')
            dis = float(dis)
            if (dis<0):
                raise ValueError
            break
        except ValueError:
            print('distance must be non-negative digit!')


    if (dir=='r'):
        x+=dis
    elif (dir=='l'):
        x-=dis
    elif (dir=='f'):
        y+=dis
    else:
        y-=dis

    print('Current location, x: '+str(x)+', y: '+str(y) )