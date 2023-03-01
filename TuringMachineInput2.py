
print('This turing machine will simulate a DFA with up to 8 states.')
print('How many states would you like to simulate?')
inputDFAstates = input()
numDFAstates = int(inputDFAstates)

inputList = []

if 0 < numDFAstates < 9:
    print("Get ready to input your DFA")
    for i in range(numDFAstates):
        print("Is state ", i, " an accept state (1) or reject state (0)? ")
        accOrRejState = input()
        inputList.append(int(accOrRejState))
        print("Where does the DFA state ", i, " go when it reads a 0?")
        zeroinputInt = input()
        zeroInputBin = bin(int(zeroinputInt))
        if int(zeroinputInt)>numDFAstates:
            quit()
        else:
            strTheBin = str(zeroInputBin).removeprefix('0b')
            lengthBin = len(strTheBin)
            if lengthBin == 1:
                listStrBin = list(strTheBin)
                inputList = inputList + [0, 0]
                inputList.append(int(listStrBin[0]))
            elif lengthBin == 2:
                listStrBin = list(strTheBin)
                inputList = inputList + [0]
                inputList.append(int(listStrBin[0]))
                inputList.append(int(listStrBin[1]))
            else: 
                listStrBin = list(strTheBin)
                inputList.append(int(listStrBin[0]))
                inputList.append(int(listStrBin[1]))
                inputList.append(int(listStrBin[2]))
        print("Where does the DFA state ", i, " go when it reads a 1?")
        oneinputInt = int(input())
        oneInputBin = bin(int(oneinputInt))
        if int(oneinputInt)>numDFAstates:
            quit()
        else:
            strTheBin = str(oneInputBin).removeprefix('0b')
            lengthBin = len(strTheBin)
            if lengthBin == 1:
                listStrBin = list(strTheBin)
                inputList = inputList + [0, 0]
                inputList.append(int(listStrBin[0]))
            elif lengthBin == 2:
                listStrBin = list(strTheBin)
                inputList = inputList + [0]
                inputList.append(int(listStrBin[0]))
                inputList.append(int(listStrBin[1]))
            else: 
                listStrBin = list(strTheBin)
                inputList.append(int(listStrBin[0]))
                inputList.append(int(listStrBin[1]))
                inputList.append(int(listStrBin[2]))
else:
    print("Wrong input")
inputList.append('.')

print('The input tape looks like this: ', str(inputList))

print("Now it's time to put in your input.")
print("It should be 0 or 1 and to end press any other key")
inputToDFA = input()
while inputToDFA == '0' or inputToDFA == '1':
    intTheInput = int(inputToDFA)
    inputList.append(intTheInput)
    inputToDFA = input()
print("The input tape is complete")
inputList.append('.')



'''
if (inputDFAstates == '4' or inputDFAstates == '5' or inputDFAstates =='6' or inputDFAstates =='7' or inputDFAstates =='8'):
    numDFAstates = int(inputDFAstates)
else:
    print('Wrong input. We\'re breaking now.')
    quit()
'''