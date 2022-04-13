import sys
import adtcode.stack
sys.path.insert(0,'/home/scott/Documents/pythondsa/adtcode')
from adtcode import stack
"""
using a stack to convert decimal to binary
when a dec number is % 2 it returns an odd/even 1/0
thats added to the stack
then the num is // divided by 2 to reduce each power of 2 
"""
def dectobin(decNumber):
    s = adtcode.stack.Stack()

    while decNumber > 0:
        rem = decNumber % 2
        s.push(rem)
        decNumber = decNumber // 2

    binString = ""
    while not s.isEmpty():
        binString = binString + str(s.pop())

    print(binString)
dectobin(233)




