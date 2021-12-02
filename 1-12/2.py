with open('Input.txt','r') as inputFile:
    cMax=int(inputFile.readline())//2
    hMax=int(inputFile.readline())//6
    oMax=int(inputFile.readline())

    moleculeMax=cMax
    if (moleculeMax>hMax):
        moleculeMax=hMax
    if (moleculeMax>oMax):
        moleculeMax=oMax

    print('Maximum molecules count:'+str(moleculeMax))   

with open('Output.txt','w') as outputFile:
    outputFile.write(str(moleculeMax))   