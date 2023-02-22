#python single line comments are with the #
"""
multiline comments are with the triple quotation marks
"""
# the url for my github address is stored as window-git 
"""
how to run in fedora 35 terminal
first: fedora 35 comes with it already installed
second: navigate to correct directory
third: type python example.py and press enter
"""
from enum import Enum
class TuringState(Enum):
	END = 'end'
	ENCODFACOPYFLAG      = 'encoDFAcopyflag'
	C0READ1STBIT         = 'c0Read1stBit'
	C0ZEROREADREAD2ND   = 'c0zeroReadRead2nd'
	C0ZREADZREADREAD3RD = 'c0zRead0readRead3rd'
	C0ZREADUREADREAD3RD = 'c0zRead1readRead3rd'
	C0UNOREADREAD2ND    = 'c0unoReadRead2nd'
	C0UREADZREADREAD3RD = 'c0uRead0readRead3rd'
	C0UREADUREADREAD3RD = 'c0uRead1readRead3rd'
	C1READ1STBIT         = 'c1Read1stBit'
	C1ZEROREADREAD2ND   = 'c1zeroReadRead2nd'
	C1ZREADZREADREAD3RD = 'c1zRead0readRead3rd'
	C1ZREADUREADREAD3RD = 'c1zRead1readRead3rd'
	C1UNOREADREAD2ND    = 'c1unoReadRead2nd'
	C1UREADZREADREAD3RD = 'c1uRead0readRead3rd'
	C1UREADUREADREAD3RD = 'c1uRead1readRead3rd'
	SPLITSTATES          = 'splitstates'
	Q1FLAG		     = 'q1flag'
	Q1CZERO		     = 'q1c0'
	Q1CUNO		     = 'q1c1'
	Q2FLAG		     = 'q2flag'
	Q2CZERO		     = 'q2c0'
	Q2CUNO		     = 'q2c1'
	Q3FLAG		     = 'q3flag'
	Q3CZERO		     = 'q3c0'
	Q3CUNO		     = 'q3c1'
	Q4FLAG		     = 'q4flag'
	Q4CZERO		     = 'q4c0'
	Q4CUNO		     = 'q4c1'
	Q5FLAG		     = 'q5flag'
	Q5CZERO		     = 'q5c0'
	Q5CUNO		     = 'q5c1'
	Q6FLAG		     = 'q6flag'
	Q6CZERO		     = 'q6c0'
	Q6CUNO		     = 'q6c1'
	Q7FLAG		     = 'q7flag'
	Q7CZERO		     = 'q7c0'
	Q7CUNO		     = 'q7c1'
	Q8FLAG		     = 'q8flag'
	Q8CZERO		     = 'q8c0'
	Q8CUNO		     = 'q8c1'
	REWINDREENCO	     = 'rewindreEncoTape'
	REWINDTAPEQ1B2	     = 'rewindTapeq1b2'
	REWINDTAPESQ1THRUQ2  = 'rewindTapesQ1thruQ2'
	REWINDTAPESQ1THRUQ3  = 'rewindTapesQ1thruQ3'
	REWINDTAPESQ1THRUQ4  = 'rewindTapesQ1thruQ4'
	REWINDTAPESQ1THRUQ5  = 'rewindTapesQ1thruQ5'
	REWINDTAPESQ1THRUQ6  = 'rewindTapesQ1thruQ6'
	REWINDTAPESQ1THRUQ7  = 'rewindTapesQ1thruQ7'
	REWINDTAPESQ1THRUQ8  = 'rewindTapesQ1thruQ8'
	Q1FLAGSTART	     = 'q1flagStart'
	READ1STDFAINPUT      = 'read1stDFAinput'
	Q1C0START	     = 'q1c0start'
	Q1C0SKIPSTART	     = 'q1c0skipStart'
	Q1C1START	     = 'q1c1start'
	REWINDQ1	     = 'rewindQ1'
	REWINDQ2	     = 'rewindQ2'
	REWINDQ3	     = 'rewindQ3'
	REWINDQ4	     = 'rewindQ4'
	REWINDQ5	     = 'rewindQ5'
	REWINDQ6	     = 'rewindQ6'
	REWINDQ7	     = 'rewindQ7'
	REWINDQ8	     = 'rewindQ8'
	CHECKNEXTSTATE	     = 'checkNextState'
	Q1COPYFLAG	     = 'q1copyflag'
	Q2COPYFLAG	     = 'q2copyflag'
	Q3COPYFLAG	     = 'q3copyflag'
	Q4COPYFLAG	     = 'q4copyflag'
	Q5COPYFLAG	     = 'q5copyflag'
	Q6COPYFLAG	     = 'q6copyflag'
	Q7COPYFLAG	     = 'q7copyflag'
	Q8COPYFLAG	     = 'q8copyflag'
	Q1READINPUT	     = 'q1readInput'
	Q2READINPUT	     = 'q2readInput'
	Q3READINPUT	     = 'q3readInput'
	Q4READINPUT	     = 'q4readInput'
	Q5READINPUT	     = 'q5readInput'
	Q6READINPUT	     = 'q6readInput'
	Q7READINPUT	     = 'q7readInput'
	Q8READINPUT	     = 'q8readInput'
	COPYQ1C0	     = 'copyq1c0'
	SKIPQ1C0	     = 'skipQ1c0'
	COPYQ2C0	     = 'copyq2c0'
	SKIPQ2C0	     = 'skipQ2c0'
	COPYQ3C0	     = 'copyq3c0'
	SKIPQ3C0	     = 'skipQ3c0'
	COPYQ4C0	     = 'copyq4c0'
	SKIPQ4C0	     = 'skipQ4c0'
	COPYQ5C0	     = 'copyq5c0'
	SKIPQ5C0	     = 'skipQ5c0'
	COPYQ6C0	     = 'copyq6c0'
	SKIPQ6C0	     = 'skipQ6c0'
	COPYQ7C0	     = 'copyq7c0'
	SKIPQ7C0	     = 'skipQ7c0'
	COPYQ8C0	     = 'copyq8c0'
	SKIPQ8C0	     = 'skipQ8c0'
	COPYQ1C1	     = 'copyQ1c1'
	COPYQ2C1	     = 'copyQ2c1'
	COPYQ3C1	     = 'copyQ3c1'
	COPYQ4C1	     = 'copyQ4c1'
	COPYQ5C1	     = 'copyQ5c1'
	COPYQ6C1	     = 'copyQ6c1'
	COPYQ7C1	     = 'copyQ7c1'
	COPYQ8C1	     = 'copyQ8c1'
	CHECKLASTOUTPUT	     = 'checkLastOutput'
	ACCEPT				= 'accept'
	REJECT				= 'reject'

'''
print('Enter the encoded DFA you would like to run')
userDFAencoding=input()
print('you entered: ' + userDFAencoding)
print('now enter the input into the DFA')
userDFAinput = input()
userInputTape=['>']



for x in userDFAencoding:
	userInputTape.append(int(x))
	
print(userInputTape)
userInputTape.append('.')

for x in userDFAinput:
	userInputTape.append(int(x))

userInputTape.append('.')
'''
print('This turning machine will simulate a DFA with up to 8 states.')
print('How many states would you like to simulate?')
inputDFAstates = input()
numDFAstates = 0

if (inputDFAstates == '4' or inputDFAstates == '5' or inputDFAstates =='6' or inputDFAstates =='7' or inputDFAstates =='8'):
    numDFAstates = int(inputDFAstates)
else:
    print('Wrong input. We\'re breaking now.')
    quit()
    
binlist = ['0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '1', '1' ]    


if numDFAstates == 4:
    binlist = binlist + ['1', '0', '0', '0', '0', '1', '1']
else:
    binlist = binlist + ['0', '0', '0', '0', '1', '0', '0']
    i=4
    while i<9:
        print('The i is at ', str(i))
        if numDFAstates == i + 1:
            binlist = binlist + ['1', '0', '0', '0'] + list("{0:b}".format(i))
            i=10
            print('The i of the IF is at ', str(i))
        else:
            binlist = binlist + ['0', '0', '0', '0'] + list("{0:b}".format(i+1))
            i=i+1
        print('The i after the IF/ELSE is at ', str(i))
        print(str(binlist))


intBinList = []
for x in binlist:
    intBinList.append(int(x))


#userInputTape=['>', 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, '.',1,0,0,1,0,1,1,1,'.']
#userInputTape=['>', 1,0, 0, 0, 0, 0, 1, 0,0, 0, 1, 0, 1, 0, 0,0, 1, 0, 0, 1, 1, 0,0, 1, 1, 0, 0, 0, '.',1,0,1,1,0,1,'.']
#userInputTape=['>', 1,0, 0, 0, 0, 0, 1, 0,0, 0, 1, 0, 1, 0, 0,0, 1, 0, 0, 1, 1, 0,0, 1, 1, 1, 0, 0, 0,1, 0, 0, 0, 0, 0, '.', 1,1,0,0,0,1,1,0,1,1,1,1,1,0,1,0, '.' ]

userInputTape = ['>'] + intBinList + ['.', 1,1,1,1, 1,1,1,1, 1,0, '.' ]
print('The user input tape is ', str(userInputTape))

reEncoDFAtape = ['>']
inputTapeHead = 1

################################################
# BEGIN TAPES
################################################
#ALL THE DFA STATE TAPES
q1DFAstateTape = ['>']
q2DFAstateTape = ['>']
q3DFAstateTape = ['>']
q4DFAstateTape = ['>']
q5DFAstateTape = ['>']
q6DFAstateTape = ['>']
q7DFAstateTape = ['>']
q8DFAstateTape = ['>']

q1DFATapeIndex = 0
q2DFATapeIndex = 0
q3DFATapeIndex = 0
q4DFATapeIndex = 0
q5DFATapeIndex = 0
q6DFATapeIndex = 0
q7DFATapeIndex = 0
q8DFATapeIndex = 0

#NEXT DFA STATE TO GO TO TAPE
nextDFAstateTape = ['>']
nextDFAstateTapeIndex = 0

#OUTPUT OF DFA TAPE
outputTape = ['>']
outputTapeIndex = 0
################################################
# END TAPES
################################################

#print(int(userInputTape[inputTapeHead]))
print(userInputTape[inputTapeHead])

inputTapeHead = 1
reEncoDFAtapeHead = 0
tmState = TuringState('encoDFAcopyflag')

'''
While Loop Block 1:
End condition: the Turing State is 'encoDFAcopyflag' and the tape head reads '.'
Purpose: Convert the given DFA from base 2 to base 10
How: 
'''
while tmState != TuringState.REWINDREENCO: 
	match tmState:
		case TuringState.ENCODFACOPYFLAG:
		#Ends reading the DFA transition function or continues the process of translating the transition function into base 10
		#Continue outcome: Records the flag of the DFA state to the tape with the DFA transition function in base 10
			if userInputTape[inputTapeHead] == '.':
				tmState = TuringState('rewindreEncoTape')
			else:
				reEncoDFAtape.append(int(userInputTape[inputTapeHead]))
				reEncoDFAtapeHead += 1
				inputTapeHead += 1
				tmState = TuringState('c0Read1stBit')
	#Transition function for DFA state reading a 0
		case TuringState.C0READ1STBIT:
			#Reads the left most digit of binary representation
			if userInputTape[inputTapeHead] == 0:
				tmState = TuringState('c0zeroReadRead2nd')
			if userInputTape[inputTapeHead] == 1:
				tmState = TuringState('c0unoReadRead2nd')
			inputTapeHead += 1
	#Transition function for DFA state reading a 0
	####Links to DFA states with a binary label of 3 or less
		case TuringState.C0ZEROREADREAD2ND:
			#Read middle digit (and the left most digit was 0)
			if userInputTape[inputTapeHead] == 0:
				tmState = TuringState('c0zRead0readRead3rd')
			if userInputTape[inputTapeHead] == 1:
				tmState = TuringState('c0zRead1readRead3rd')
			inputTapeHead += 1
		case TuringState.C0ZREADZREADREAD3RD:
			#Read right most digit (after '00')
			if userInputTape[inputTapeHead] == 0:
				reEncoDFAtape.append(1)
			if userInputTape[inputTapeHead] == 1:
				reEncoDFAtape.append(2)
			tmState = TuringState('c1Read1stBit')
			inputTapeHead += 1
			reEncoDFAtapeHead += 1
		case TuringState.C0ZREADUREADREAD3RD:
			#Read right most digit (after '01')
			if userInputTape[inputTapeHead] == 0:
				reEncoDFAtape.append(3)
			if userInputTape[inputTapeHead] == 1:
				reEncoDFAtape.append(4)
			tmState = TuringState('c1Read1stBit')
			inputTapeHead += 1
			reEncoDFAtapeHead += 1
	#Transition function for DFA state reading a 0
	####Links to DFA states with a label of 4 or more
		case TuringState.C0UNOREADREAD2ND:
			#Read middle digit (and the left most digit was 1)
			if userInputTape[inputTapeHead] == 0:
				tmState = TuringState('c0uRead0readRead3rd')
			if userInputTape[inputTapeHead] == 1:
				tmState = TuringState('c0uRead1readRead3rd')
			inputTapeHead += 1
		case TuringState.C0UREADZREADREAD3RD:
			#Read right most digit (after '10')
			if userInputTape[inputTapeHead] == 0:
				reEncoDFAtape.append(5)
			if userInputTape[inputTapeHead] == 1:
				reEncoDFAtape.append(6)
			tmState = TuringState('c1Read1stBit')
			inputTapeHead += 1
			reEncoDFAtapeHead += 1
		case TuringState.C0UREADUREADREAD3RD:
			#Read right most digit (after '11')
			if userInputTape[inputTapeHead] == 0:
				reEncoDFAtape.append(7)
			if userInputTape[inputTapeHead] == 1:
				reEncoDFAtape.append(8)
			tmState = TuringState('c1Read1stBit')
			inputTapeHead += 1
			reEncoDFAtapeHead += 1	
	#Transition function for DFA state reading a 1
		case TuringState.C1READ1STBIT:
			if userInputTape[inputTapeHead] == 0:
				tmState = TuringState('c1zeroReadRead2nd')
			if userInputTape[inputTapeHead] == 1:
				tmState = TuringState('c1unoReadRead2nd')
			inputTapeHead += 1
	####Links to DFA states with a label of 3 or less (in binary)
		case TuringState.C1ZEROREADREAD2ND:
			if userInputTape[inputTapeHead] == 0:
				tmState = TuringState('c1zRead0readRead3rd')
			if userInputTape[inputTapeHead] == 1:
				tmState = TuringState('c1zRead1readRead3rd')
			inputTapeHead += 1
		case TuringState.C1ZREADZREADREAD3RD:
			if userInputTape[inputTapeHead] == 0:
				reEncoDFAtape.append(1)
			if userInputTape[inputTapeHead] == 1:
				reEncoDFAtape.append(2)
			tmState = TuringState('encoDFAcopyflag')
			inputTapeHead += 1
			reEncoDFAtapeHead += 1
		case TuringState.C1ZREADUREADREAD3RD:
			if userInputTape[inputTapeHead] == 0:
				reEncoDFAtape.append(3)
			if userInputTape[inputTapeHead] == 1:
				reEncoDFAtape.append(4)
			tmState = TuringState('encoDFAcopyflag')
			inputTapeHead += 1
			reEncoDFAtapeHead += 1
	####Links to DFA states with a label of 4 or more (in binary)
		case TuringState.C1UNOREADREAD2ND:
			if userInputTape[inputTapeHead] == 0:
				tmState = TuringState('c1uRead0readRead3rd')
			if userInputTape[inputTapeHead] == 1:
				tmState = TuringState('c1uRead1readRead3rd')
			inputTapeHead += 1
		case TuringState.C1UREADZREADREAD3RD:
			if userInputTape[inputTapeHead] == 0:
				reEncoDFAtape.append(5)
			if userInputTape[inputTapeHead] == 1:
				reEncoDFAtape.append(6)
			tmState = TuringState('encoDFAcopyflag')
			inputTapeHead += 1
			reEncoDFAtapeHead += 1
		case TuringState.C1UREADUREADREAD3RD:
			if userInputTape[inputTapeHead] == 0:
				reEncoDFAtape.append(7)
			if userInputTape[inputTapeHead] == 1:
				reEncoDFAtape.append(8)
			tmState = TuringState('encoDFAcopyflag')
			inputTapeHead += 1	
			reEncoDFAtapeHead += 1	



reEncoDFAtape.append('.')
print("The re-encoded tape says this: ", str(reEncoDFAtape))

'''
 Block 2- mini while loop block
 this rewinds the tape head for the reEncoDFA tape
'''
while tmState == TuringState.REWINDREENCO: 
	if reEncoDFAtape[reEncoDFAtapeHead] == '>':
		tmState = TuringState('splitstates')
	else:
		reEncoDFAtapeHead -= 1

#print('Tape head location after writing: ', reEncoDFAtapeHead)
#print('this is whats at index 0 ' + reEncoDFAtape[0])
#print('this is whats at index current spot ' + str(reEncoDFAtape[reEncoDFAtapeHead]))

# This if statement is block 2	
if tmState == TuringState.SPLITSTATES:
	tmState = TuringState('q1flag')
	reEncoDFAtapeHead += 1 #so the re encoded DFA tapehead is no longer reading the start symbol
	q1DFATapeIndex += 1
else:
	print('This Turing Machine has to go to split states at this point. Nothing else will run now.')
	
	

exitloop = 0
'''
This while loop has a bit of syntactic sugar.
Rather than have the while loop condition list every possible rewind state, 
the while loop simply looks for the exit loop integer to change.
When the tmState changes to any of the rewind tape states, the next iteration
of the while loop goes to the catch all statement and the exit loop integer changes
'''

while exitloop == 0:
	print(tmState.value)
	match tmState:
		case TuringState.Q1FLAG: 
			if reEncoDFAtape[reEncoDFAtapeHead] == 0 or reEncoDFAtape[reEncoDFAtapeHead] == 1:
				q1DFAstateTape.append(reEncoDFAtape[reEncoDFAtapeHead])
				tmState = TuringState('q1c0')
				reEncoDFAtapeHead += 1
				q1DFATapeIndex += 1
			else:
				tmState = TuringState('rewindTapeq1b2')
		case TuringState.Q1CZERO:
			q1DFAstateTape.append(reEncoDFAtape[reEncoDFAtapeHead])
			tmState = TuringState('q1c1')
			reEncoDFAtapeHead += 1
			q1DFATapeIndex += 1
		case TuringState.Q1CUNO:
			q1DFAstateTape.append(reEncoDFAtape[reEncoDFAtapeHead])
			tmState = TuringState('q2flag')
			reEncoDFAtapeHead += 1
		case TuringState.Q2FLAG: 
			if reEncoDFAtape[reEncoDFAtapeHead] == 0 or reEncoDFAtape[reEncoDFAtapeHead] == 1:
				q2DFAstateTape.append(reEncoDFAtape[reEncoDFAtapeHead])
				tmState = TuringState('q2c0')
				reEncoDFAtapeHead += 1
				q2DFATapeIndex += 1
			else:
				tmState = TuringState('rewindTapesQ1thruQ2')
		case TuringState.Q2CZERO:
			q2DFAstateTape.append(reEncoDFAtape[reEncoDFAtapeHead])
			tmState = TuringState('q2c1')
			reEncoDFAtapeHead += 1
			q2DFATapeIndex += 1
		case TuringState.Q2CUNO:
			q2DFAstateTape.append(reEncoDFAtape[reEncoDFAtapeHead])
			tmState = TuringState('q3flag')
			reEncoDFAtapeHead += 1
			q2DFATapeIndex += 1
		case TuringState.Q3FLAG: 
			if reEncoDFAtape[reEncoDFAtapeHead] == 0 or reEncoDFAtape[reEncoDFAtapeHead] == 1:
				q3DFAstateTape.append(reEncoDFAtape[reEncoDFAtapeHead])
				tmState = TuringState('q3c0')
				reEncoDFAtapeHead += 1
				q3DFATapeIndex += 1
			else:
				tmState = TuringState('rewindTapesQ1thruQ2')
		case TuringState.Q3CZERO:
			q3DFAstateTape.append(reEncoDFAtape[reEncoDFAtapeHead])
			tmState = TuringState('q3c1')
			reEncoDFAtapeHead += 1
			q3DFATapeIndex += 1
		case TuringState.Q3CUNO:
			q3DFAstateTape.append(reEncoDFAtape[reEncoDFAtapeHead])
			tmState = TuringState('q4flag')
			reEncoDFAtapeHead += 1
			q3DFATapeIndex += 1
		case TuringState.Q4FLAG: 
			if reEncoDFAtape[reEncoDFAtapeHead] == 0 or reEncoDFAtape[reEncoDFAtapeHead] == 1:
				q4DFAstateTape.append(reEncoDFAtape[reEncoDFAtapeHead])
				tmState = TuringState('q4c0')
				reEncoDFAtapeHead += 1
				q4DFATapeIndex += 1
			else:
				tmState = TuringState('rewindTapesQ1thruQ3')
		case TuringState.Q4CZERO:
			q4DFAstateTape.append(reEncoDFAtape[reEncoDFAtapeHead])
			tmState = TuringState('q4c1')
			reEncoDFAtapeHead += 1
			q4DFATapeIndex += 1
		case TuringState.Q4CUNO:
			q4DFAstateTape.append(reEncoDFAtape[reEncoDFAtapeHead])
			tmState = TuringState('q5flag')
			reEncoDFAtapeHead += 1
			q4DFATapeIndex += 1
		case TuringState.Q5FLAG: 
			if reEncoDFAtape[reEncoDFAtapeHead] == 0 or reEncoDFAtape[reEncoDFAtapeHead] == 1:
				q5DFAstateTape.append(reEncoDFAtape[reEncoDFAtapeHead])
				tmState = TuringState('q5c0')
				reEncoDFAtapeHead += 1
				q5DFATapeIndex += 1
			else:
				tmState = TuringState('rewindTapesQ1thruQ4')
		case TuringState.Q5CZERO:
			q5DFAstateTape.append(reEncoDFAtape[reEncoDFAtapeHead])
			tmState = TuringState('q5c1')
			reEncoDFAtapeHead += 1
			q5DFATapeIndex += 1
		case TuringState.Q5CUNO:
			q5DFAstateTape.append(reEncoDFAtape[reEncoDFAtapeHead])
			tmState = TuringState('q6flag')
			reEncoDFAtapeHead += 1
			q5DFATapeIndex += 1
		case TuringState.Q6FLAG: 
			if reEncoDFAtape[reEncoDFAtapeHead] == 0 or reEncoDFAtape[reEncoDFAtapeHead] == 1:
				q6DFAstateTape.append(reEncoDFAtape[reEncoDFAtapeHead])
				tmState = TuringState('q6c0')
				reEncoDFAtapeHead += 1
				q6DFATapeIndex += 1
			else:
				tmState = TuringState('rewindTapesQ1thruQ5')
		case TuringState.Q6CZERO:
			q6DFAstateTape.append(reEncoDFAtape[reEncoDFAtapeHead])
			tmState = TuringState('q6c1')
			reEncoDFAtapeHead += 1
			q6DFATapeIndex += 1
		case TuringState.Q6CUNO:
			q6DFAstateTape.append(reEncoDFAtape[reEncoDFAtapeHead])
			tmState = TuringState('q7flag')
			reEncoDFAtapeHead += 1
			q6DFATapeIndex += 1
		case TuringState.Q7FLAG: 
			if reEncoDFAtape[reEncoDFAtapeHead] == 0 or reEncoDFAtape[reEncoDFAtapeHead] == 1:
				q7DFAstateTape.append(reEncoDFAtape[reEncoDFAtapeHead])
				tmState = TuringState('q7c0')
				reEncoDFAtapeHead += 1
				q7DFATapeIndex += 1
			else:
				tmState = TuringState('rewindTapesQ1thruQ6')
		case TuringState.Q7CZERO:
			q7DFAstateTape.append(reEncoDFAtape[reEncoDFAtapeHead])
			tmState = TuringState('q7c1')
			reEncoDFAtapeHead += 1
			q7DFATapeIndex += 1
		case TuringState.Q7CUNO:
			q7DFAstateTape.append(reEncoDFAtape[reEncoDFAtapeHead])
			tmState = TuringState('q8flag')
			reEncoDFAtapeHead += 1
			q7DFATapeIndex += 1
		case TuringState.Q8FLAG: 
			if reEncoDFAtape[reEncoDFAtapeHead] == 0 or reEncoDFAtape[reEncoDFAtapeHead] == 1:
				q8DFAstateTape.append(reEncoDFAtape[reEncoDFAtapeHead])
				tmState = TuringState('q8c0')
				reEncoDFAtapeHead += 1
				q8DFATapeIndex += 1
			else:
				tmState = TuringState('rewindTapesQ1thruQ7')
		case TuringState.Q8CZERO:
			q8DFAstateTape.append(reEncoDFAtape[reEncoDFAtapeHead])
			tmState = TuringState('q8c1')
			reEncoDFAtapeHead += 1
			q8DFATapeIndex += 1
		case TuringState.Q8CUNO:
			q8DFAstateTape.append(reEncoDFAtape[reEncoDFAtapeHead])
			tmState = TuringState('rewindTapesQ1thruQ8')
			reEncoDFAtapeHead += 1
			q8DFATapeIndex += 1
		case _:
			exitloop = 1
			
'''

'''

# This switch statement rewinds the correct amount of tapes
# each case contains a while loop to rewind the tapes

match tmState: 
	case TuringState.REWINDTAPEQ1B2:
		while q1DFAstateTape[q1DFATapeIndex] != '>':
			q1DFATapeIndex -= 1
		tmState = TuringState('q1flagStart')
		q1DFATapeIndex += 1
	case TuringState.REWINDTAPESQ1THRUQ2:
		while q1DFAstateTape[q1DFATapeIndex] != '>':
			print(q1DFAstateTape[q1DFATapeIndex])
			q1DFATapeIndex -= 1
			q2DFATapeIndex -= 1
		tmState = TuringState('q1flagStart')
		q1DFATapeIndex += 1
	case TuringState.REWINDTAPESQ1THRUQ3:
		while q1DFAstateTape[q1DFATapeIndex] != '>':
			q1DFATapeIndex -= 1
			q2DFATapeIndex -= 1
			q3DFATapeIndex -= 1
		tmState = TuringState('q1flagStart')
		q1DFATapeIndex += 1
	case TuringState.REWINDTAPESQ1THRUQ4:
		while q1DFAstateTape[q1DFATapeIndex] != '>':
			q1DFATapeIndex -= 1
			q2DFATapeIndex -= 1
			q3DFATapeIndex -= 1
			q4DFATapeIndex -= 1
		tmState = TuringState('q1flagStart')
		q1DFATapeIndex += 1
	case TuringState.REWINDTAPESQ1THRUQ5:
		while q1DFAstateTape[q1DFATapeIndex] != '>':
			q1DFATapeIndex -= 1
			q2DFATapeIndex -= 1
			q3DFATapeIndex -= 1
			q4DFATapeIndex -= 1
			q5DFATapeIndex -= 1
		tmState = TuringState('q1flagStart')
		q1DFATapeIndex += 1
	case TuringState.REWINDTAPESQ1THRUQ6:
		while q1DFAstateTape[q1DFATapeIndex] != '>':
			q1DFATapeIndex -= 1
			q2DFATapeIndex -= 1
			q3DFATapeIndex -= 1
			q4DFATapeIndex -= 1
			q5DFATapeIndex -= 1
			q6DFATapeIndex -= 1
		tmState = TuringState('q1flagStart')
		q1DFATapeIndex += 1
	case TuringState.REWINDTAPESQ1THRUQ7:
		while q1DFAstateTape[q1DFATapeIndex] != '>':
			q1DFATapeIndex -= 1
			q2DFATapeIndex -= 1
			q3DFATapeIndex -= 1
			q4DFATapeIndex -= 1
			q5DFATapeIndex -= 1
			q6DFATapeIndex -= 1
			q7DFATapeIndex -= 1
		tmState = TuringState('q1flagStart')
		q1DFATapeIndex += 1
	case TuringState.REWINDTAPESQ1THRUQ8:
		while q1DFAstateTape[q1DFATapeIndex] != '>':
			q1DFATapeIndex -= 1
			q2DFATapeIndex -= 1
			q3DFATapeIndex -= 1
			q4DFATapeIndex -= 1
			q5DFATapeIndex -= 1
			q6DFATapeIndex -= 1
			q7DFATapeIndex -= 1
			q8DFATapeIndex -= 1
		tmState = TuringState('q1flagStart')
		q1DFATapeIndex += 1


# block 3
print('The input tape head is on cell ' + str(inputTapeHead) + ' and what it contains:')
print(userInputTape[inputTapeHead])
print('the state before block 3: ', str(tmState))

	
block3=1
print('input tape head before flag start and rewind ', userInputTape[inputTapeHead])
print('The DFA state tape pre block 3: ', str(nextDFAstateTape))
while tmState != TuringState.REWINDQ1:
	print(str(tmState))
	print('Block 3: User input tape head currently says: ', userInputTape[inputTapeHead])
	match tmState:
		case TuringState.Q1FLAGSTART:
			outputTape.append(q1DFAstateTape[q1DFATapeIndex])
			outputTapeIndex += 1
			tmState = TuringState('read1stDFAinput')
			inputTapeHead += 1
			q1DFATapeIndex += 1
		case TuringState.READ1STDFAINPUT:
			if (userInputTape[inputTapeHead] == 0):
				tmState = TuringState('q1c0start')
			else:
				tmState = TuringState('q1c0skipStart')
		case TuringState.Q1C0START:
			nextDFAstateTape.append(q1DFAstateTape[q1DFATapeIndex])
			nextDFAstateTapeIndex += 1
			tmState = TuringState('rewindQ1')
		case TuringState.Q1C0SKIPSTART:
			tmState = TuringState('q1c1start')
			q1DFATapeIndex += 1
		case TuringState.Q1C1START:
			nextDFAstateTape.append(q1DFAstateTape[q1DFATapeIndex])
			nextDFAstateTapeIndex +=1
			tmState = TuringState('rewindQ1')
print('The output state tape post block 3: ', str(outputTape))
# input tape head is currently on first input character 
# that is all the tape head has read
print('input tape head after flag start and rewind ', userInputTape[inputTapeHead])

print(str(q1DFAstateTape))
print(str(q2DFAstateTape))
print(str(q3DFAstateTape))
print(str(q4DFAstateTape))
print(str(q5DFAstateTape))
print(str(q6DFAstateTape))
print(str(q7DFAstateTape))
print(str(q8DFAstateTape))
safety = 1
print('The DFA state tape pre block 4: ', str(nextDFAstateTape))

block4=1
while block4 == 1:
	print('top block DFA state tape says ', nextDFAstateTape[nextDFAstateTapeIndex])
	print(str(nextDFAstateTape))
	print(str(tmState))
	if (tmState == TuringState.REWINDQ1):
		while tmState == TuringState.REWINDQ1:
			if q1DFAstateTape[q1DFATapeIndex] != '>': 
				tmState = TuringState('rewindQ1')
				q1DFATapeIndex -= 1
			else:
				tmState = TuringState('checkNextState')
	elif (tmState == TuringState.REWINDQ2):
		while tmState == TuringState.REWINDQ2:
			if q2DFAstateTape[q2DFATapeIndex] != '>': 
				tmState = TuringState('rewindQ2')
				q2DFATapeIndex -= 1
			else:
				tmState = TuringState('checkNextState')
	elif (tmState == TuringState.REWINDQ3):
		while tmState == TuringState.REWINDQ3:
			if q3DFAstateTape[q3DFATapeIndex] != '>': 
				tmState = TuringState('rewindQ3')
				q3DFATapeIndex -= 1
			else:
				tmState = TuringState('checkNextState')
	
	elif (tmState == TuringState.REWINDQ4):
		while tmState == TuringState.REWINDQ4:
			if q4DFAstateTape[q4DFATapeIndex] != '>': 
				tmState = TuringState('rewindQ4')
				q4DFATapeIndex -= 1
			else:
				tmState = TuringState('checkNextState')
				print(q4DFATapeIndex)
				
	elif (tmState == TuringState.REWINDQ5):
		while tmState == TuringState.REWINDQ5:
			if q5DFAstateTape[q5DFATapeIndex] != '>': 
				tmState = TuringState('rewindQ5')
				q5DFATapeIndex -= 1
			else:
				tmState = TuringState('checkNextState')
	
	elif (tmState == TuringState.REWINDQ6):
		while tmState == TuringState.REWINDQ6:
			if q6DFAstateTape[q6DFATapeIndex] != '>': 
				tmState = TuringState('rewindQ6')
				q6DFATapeIndex -= 1
			else:
				tmState = TuringState('checkNextState')
	
	elif (tmState == TuringState.REWINDQ7):
		while tmState == TuringState.REWINDQ7:
			if q7DFAstateTape[q7DFATapeIndex] != '>': 
				tmState = TuringState('rewindQ7')
				q7DFATapeIndex -= 1
			else:
				tmState = TuringState('checkNextState')
	
	elif (tmState == TuringState.REWINDQ8):
		while tmState == TuringState.REWINDQ8:
			if q8DFAstateTape[q8DFATapeIndex] != '>': 
				tmState = TuringState('rewindQ8')
				q8DFATapeIndex -= 1
			else:
				tmState = TuringState('checkNextState')
	print(str(tmState))
#########################################################################################################################################
	if (tmState == TuringState.CHECKNEXTSTATE):
	#	inputTapeHead += 1; 
		if nextDFAstateTape[nextDFAstateTapeIndex] == 1:
			tmState = TuringState('q1copyflag')
			q1DFATapeIndex += 1
		elif nextDFAstateTape[nextDFAstateTapeIndex] == 2:
			tmState = TuringState('q2copyflag')
			q2DFATapeIndex += 1
		elif nextDFAstateTape[nextDFAstateTapeIndex] == 3:
			tmState = TuringState('q3copyflag')
			q3DFATapeIndex += 1
		elif nextDFAstateTape[nextDFAstateTapeIndex] == 4:
			tmState = TuringState('q4copyflag')
			q4DFATapeIndex += 1
		elif nextDFAstateTape[nextDFAstateTapeIndex] == 5:
			tmState = TuringState('q5copyflag')
			q5DFATapeIndex += 1
		elif nextDFAstateTape[nextDFAstateTapeIndex] == 6:
			tmState = TuringState('q6copyflag')
			q6DFATapeIndex += 1
		elif nextDFAstateTape[nextDFAstateTapeIndex] == 7:
			tmState = TuringState('q7copyflag')
			q7DFATapeIndex += 1
		elif nextDFAstateTape[nextDFAstateTapeIndex] == 8:
			tmState = TuringState('q8copyflag')
			q8DFATapeIndex += 1
	if (tmState == TuringState.Q1COPYFLAG):
		outputTape.append(q1DFAstateTape[q1DFATapeIndex])
		tmState = TuringState('q1readInput')
		inputTapeHead += 1
		q1DFATapeIndex += 1
		print('q1flag')
	elif (tmState == TuringState.Q2COPYFLAG):
		outputTape.append(q2DFAstateTape[q2DFATapeIndex])
		tmState = TuringState('q2readInput')
		inputTapeHead += 1
		q2DFATapeIndex += 1
		print('q2flag')
	elif (tmState == TuringState.Q3COPYFLAG):
		outputTape.append(q3DFAstateTape[q3DFATapeIndex])
		tmState = TuringState('q3readInput')
		inputTapeHead += 1
		q3DFATapeIndex += 1
		print('q3flag')
	elif (tmState == TuringState.Q4COPYFLAG):
		outputTape.append(q4DFAstateTape[q4DFATapeIndex])
		tmState = TuringState('q4readInput')
		inputTapeHead += 1
		q4DFATapeIndex += 1
		print('q4flag')
		print('The tape is at: ', str(q4DFATapeIndex))
	elif (tmState == TuringState.Q5COPYFLAG):
		outputTape.append(q5DFAstateTape[q5DFATapeIndex])
		tmState = TuringState('q5readInput')
		inputTapeHead += 1
		q5DFATapeIndex += 1
		print('q5flag')	
	elif (tmState == TuringState.Q6COPYFLAG):
		outputTape.append(q6DFAstateTape[q6DFATapeIndex])
		tmState = TuringState('q6readInput')
		inputTapeHead += 1
		q6DFATapeIndex += 1
		print('q6flag')	
	elif (tmState == TuringState.Q7COPYFLAG):
		outputTape.append(q7DFAstateTape[q7DFATapeIndex])
		tmState = TuringState('q7readInput')
		inputTapeHead += 1
		q7DFATapeIndex += 1
		print('q7flag')	
	elif (tmState == TuringState.Q8COPYFLAG):
		outputTape.append(q8DFAstateTape[q8DFATapeIndex])
		tmState = TuringState('q8readInput')
		inputTapeHead += 1
		q8DFATapeIndex += 1
		print('q8flag')	
	print(str(tmState))
	
	if (tmState == TuringState.Q1READINPUT):
		if userInputTape[inputTapeHead] == 0:
			tmState = TuringState('copyq1c0')
			
		elif userInputTape[inputTapeHead] == 1:
			tmState = TuringState('skipQ1c0')
		else:
			tmState = TuringState('checkLastOutput')
	elif (tmState == TuringState.Q2READINPUT):
		if userInputTape[inputTapeHead] == 0:
			tmState = TuringState('copyq2c0')
		elif userInputTape[inputTapeHead] == 1:
			tmState = TuringState('skipQ2c0')
		else:
			tmState = TuringState('checkLastOutput')
	elif (tmState == TuringState.Q3READINPUT):
		if userInputTape[inputTapeHead] == 0:
			tmState = TuringState('copyq3c0')
		elif userInputTape[inputTapeHead] == 1:
			tmState = TuringState('skipQ3c0')
		else:
			tmState = TuringState('checkLastOutput')
	elif (tmState == TuringState.Q4READINPUT):
		if userInputTape[inputTapeHead] == 0:
			tmState = TuringState('copyq4c0')
		elif userInputTape[inputTapeHead] == 1:
			tmState = TuringState('skipQ4c0')
		else:
			tmState = TuringState('checkLastOutput')
	elif (tmState == TuringState.Q5READINPUT):
		if userInputTape[inputTapeHead] == 0:
			tmState = TuringState('copyq5c0')
		elif userInputTape[inputTapeHead] == 1:
			tmState = TuringState('skipQ5c0')
		else:
			tmState = TuringState('checkLastOutput')
	elif (tmState == TuringState.Q6READINPUT):
		if userInputTape[inputTapeHead] == 0:
			tmState = TuringState('copyq6c0')
		elif userInputTape[inputTapeHead] == 1:
			tmState = TuringState('skipQ6c0')
		else:
			tmState = TuringState('checkLastOutput')
	elif (tmState == TuringState.Q7READINPUT):
		if userInputTape[inputTapeHead] == 0:
			tmState = TuringState('copyq7c0')
		elif userInputTape[inputTapeHead] == 1:
			tmState = TuringState('skipQ7c0')
		else:
			tmState = TuringState('checkLastOutput')
	elif (tmState == TuringState.Q8READINPUT):
		if userInputTape[inputTapeHead] == 0:
			tmState = TuringState('copyq8c0')
		elif userInputTape[inputTapeHead] == 1:
			tmState = TuringState('skipQ8c0')
		else:
			tmState = TuringState('checkLastOutput')
	outputTapeIndex += 1
	if (tmState == TuringState.COPYQ1C0):
		tmState = TuringState('rewindQ1')
		nextDFAstateTape.append(q1DFAstateTape[q1DFATapeIndex])
		nextDFAstateTapeIndex += 1
	elif (tmState == TuringState.COPYQ2C0):
		tmState = TuringState('rewindQ2')
		nextDFAstateTape.append(q2DFAstateTape[q2DFATapeIndex])
		nextDFAstateTapeIndex += 1
	elif (tmState == TuringState.COPYQ3C0):
		tmState = TuringState('rewindQ3')
		nextDFAstateTape.append(q3DFAstateTape[q3DFATapeIndex])
		nextDFAstateTapeIndex += 1
	elif (tmState == TuringState.COPYQ4C0):
		tmState = TuringState('rewindQ4')
		nextDFAstateTape.append(q4DFAstateTape[q4DFATapeIndex])
		nextDFAstateTapeIndex += 1
	elif (tmState == TuringState.COPYQ5C0):
		tmState = TuringState('rewindQ5')
		nextDFAstateTape.append(q5DFAstateTape[q5DFATapeIndex])
		nextDFAstateTapeIndex += 1
	elif (tmState == TuringState.COPYQ6C0):
		tmState = TuringState('rewindQ6')
		nextDFAstateTape.append(q6DFAstateTape[q6DFATapeIndex])
		nextDFAstateTapeIndex += 1
	elif (tmState == TuringState.COPYQ7C0):
		tmState = TuringState('rewindQ7')
		nextDFAstateTape.append(q7DFAstateTape[q7DFATapeIndex])
		nextDFAstateTapeIndex += 1
	elif (tmState == TuringState.COPYQ8C0):
		tmState = TuringState('rewindQ8')
		nextDFAstateTape.append(q8DFAstateTape[q8DFATapeIndex])
		nextDFAstateTapeIndex += 1
	if (tmState == TuringState.SKIPQ1C0):
		tmState = TuringState('copyQ1c1')
		q1DFATapeIndex += 1
	elif (tmState == TuringState.SKIPQ2C0):
		tmState = TuringState('copyQ2c1')
		q2DFATapeIndex += 1
	elif (tmState == TuringState.SKIPQ3C0):
		tmState = TuringState('copyQ3c1')
		q3DFATapeIndex += 1
	elif (tmState == TuringState.SKIPQ4C0):
		tmState = TuringState('copyQ4c1')
		q4DFATapeIndex += 1	
	elif (tmState == TuringState.SKIPQ5C0):
		tmState = TuringState('copyQ5c1')
		q5DFATapeIndex += 1	
	elif (tmState == TuringState.SKIPQ6C0):
		tmState = TuringState('copyQ6c1')
		q6DFATapeIndex += 1	
	elif (tmState == TuringState.SKIPQ7C0):
		tmState = TuringState('copyQ7c1')
		q7DFATapeIndex += 1	
	elif (tmState == TuringState.SKIPQ8C0):
		tmState = TuringState('copyQ8c1')
		q8DFATapeIndex += 1	
	if (tmState == TuringState.COPYQ1C1):
		tmState = TuringState('rewindQ1')
		nextDFAstateTape.append(q1DFAstateTape[q1DFATapeIndex])
		nextDFAstateTapeIndex += 1
	elif (tmState == TuringState.COPYQ2C1):
		tmState = TuringState('rewindQ2')
		nextDFAstateTape.append(q2DFAstateTape[q2DFATapeIndex])
		nextDFAstateTapeIndex += 1
	elif (tmState == TuringState.COPYQ3C1):
		tmState = TuringState('rewindQ3')
		nextDFAstateTape.append(q3DFAstateTape[q3DFATapeIndex])
		nextDFAstateTapeIndex += 1
	elif (tmState == TuringState.COPYQ4C1):
		tmState = TuringState('rewindQ4')
		nextDFAstateTape.append(q4DFAstateTape[q4DFATapeIndex])
		nextDFAstateTapeIndex += 1
	elif (tmState == TuringState.COPYQ5C1):
		tmState = TuringState('rewindQ5')
		nextDFAstateTape.append(q5DFAstateTape[q5DFATapeIndex])
		nextDFAstateTapeIndex += 1
	elif (tmState == TuringState.COPYQ6C1):
		tmState = TuringState('rewindQ6')
		nextDFAstateTape.append(q6DFAstateTape[q6DFATapeIndex])
		nextDFAstateTapeIndex += 1
	elif (tmState == TuringState.COPYQ7C1):
		tmState = TuringState('rewindQ7')
		nextDFAstateTape.append(q7DFAstateTape[q7DFATapeIndex])
		nextDFAstateTapeIndex += 1
	elif (tmState == TuringState.COPYQ8C1):
		tmState = TuringState('rewindQ8')
		nextDFAstateTape.append(q8DFAstateTape[q8DFATapeIndex])
		nextDFAstateTapeIndex += 1
	if (tmState == TuringState.CHECKLASTOUTPUT):
		block4=0
		print('hit turing state check last output')


if (tmState == TuringState.CHECKLASTOUTPUT):
	if (outputTape[outputTapeIndex] == 1):
		tmState = TuringState('accept')
	else:
		tmState = TuringState('reject')

print("The final turing state is: ", str(tmState.value))


print('loop exited')
print(userInputTape[inputTapeHead])
print('hit last line of code')
'''
'''
print("This is the output tape stuff, 1st is entire output Tape, 2nd is final location of output tape index, 3rd is length of output tape")
print(str(outputTape))
print(outputTapeIndex)
print(str(len(outputTape)))
print("The final output should be: ", str(outputTape[outputTapeIndex]))

#I made a change!