def diagonalFind(arr):
  subArrayAmount = 0
  iterAmount = (len(arr[0]) + len(arr)) - 1
  bufferAmount = iterAmount - len(arr[0]) 
  print("Iteramount: ", iterAmount)
  print("Buffer Amount: " ,bufferAmount)
  for i in range(iterAmount):
    
    lettersArr = []
    '''
    if(iterAmount % 2 == 0):
      if(i < int((iterAmount) / 2)):#This finds how many sub iteration. Or how many letters
        print("here")
        subArrayAmount += 1
      elif(i > int((iterAmount) / 2)):#Since it looks like a triangle. ON the equal iteration, dont change anything
        print("down here")
        subArrayAmount -= 1
    else:#Key part
      if(i <= int(iterAmount / 2) - 1):
        subArrayAmount += 1
      elif(i > int(iterAmount / 2 + 1)):
        subArrayAmount -= 1
      '''
   # print(i)
    if(i <= bufferAmount):#Used to figure out how far from beginning or end of array to stop incrementing/decrementing. Formula for that is IterAmount - amountOfColumns
      subArrayAmount += 1
    elif(i > iterAmount - bufferAmount - 1):
      subArrayAmount -= 1
    

    
  
    
    if(i < len(arr[0])): #Pattern shows the first index will be zero until it is greater than len(arr[0]). Then i++ each time
      firstIndex = 0
    else:
      firstIndex = i - len(arr[0]) + 1#The indexes HAVE to add up to the iter cycle number. SO find one and use subtraction
    secondIndex = i - firstIndex
    #print(arr[firstIndex][secondIndex], " ", subArrayAmount)
    lettersArr.append(arr[firstIndex][secondIndex])#Add the first letter to the letters array
    secondCount = firstIndex #According to pattern below. The second first ([x][]) index will be one larger than the first letters first index. Thats where it starts getting bigger
    if(subArrayAmount > 1):
      for j in range(subArrayAmount - 1):
        secondCount += 1
        #print("Second count: ", secondCount, " " , arr[secondCount][i - secondCount])
        lettersArr.append(arr[secondCount][i - secondCount])#Still two indexes add to 'i'
    print(lettersArr)

'''
array = [
  ["E","D","C","B","A"],
  ["J","I","H","G","F"],
  ["O","N","M","L","K"],
  ["T","S","R","Q","P"]
]
  '''


arr = [
  ["E","D","C","B","A"],
  ["J","I","H","G","F"],
  ["O","N","M","L","K"],
  ["T","S","R","Q","P"]
]
  
diagonalFind(arr)
'''
A   0  [0][0]
BF  1  [0][1], [1][0]
CGK 2  [0][2], [1][1], [2][0]
DHL 3  [0][3], [1][2], [2][1]
EIM 4  [0][4], [1][3], [2][2]
JN  5  [1][4], [2][3]
O   6  [2][4]

7
  '''






#THIS ONE GOES RIGHT TO LEFT

    
  

  

'''
A B C D E
F G H I J
K L M N O
P Q R S T

A    0   [0][0]
BF   1   [0][1], [1][0]
CGK  2   [0][2], [1][1], [2][0]
DHLP 3   [0][3], [1][2], [2][1], [3][0]  
EIMQ 4   [0][4], [1][3], [2][2], [3][1]
JNR  5   [1][4], [2][3], [3][2]
OS   6   [2][4], [3][3]
T    7   [3][4]

total: 8. ROW + COLUMN length - 1.
total 20;
---------------

EDCBA
JIHGF
ONMLK
TSRQP
arr = [
  ["E","D","C","B","A"],
  ["J","I","H","G","F"],
  ["O","N","M","L","K"],
  ["T","S","R","Q","P"]
]
E     0   [0][4]
DJ    1   [0][3], [1][4]
CIO   2   [0][2], [1][3], [2][4]
BHNT  3   [0][1], [1][2], [2][3], [3][4]
AGMS  4   [0][0], [1][1], [2][2], [3][3]
FLR   5   [1][0], [2][1], [3][2]
KQ    6   [2][3], [3][1]
P     7   [3][0]
A  0 | 1 [0][0]
BF 1 | 2 [0][1], [1][0]
CL 2 | 2 [0][2], [1][1]
DM 3 | 2 [0][3], [1][2]
EN 4 | 2 [0][4], [1][3]
O  5 | 1 [1][4]


Iteramount: 6;

[A,B,C,D,E]
[K,L,M,N,O]

ROWS: 2;
COLS: 5;


[V, E, T, J, V, N, F, Q, Q, E, E], 
[H, B, L, A, U, J, O, G, K, T, Z], 
[B, W, H, C, H, H, H, I, S, Q, I], 

0 | 1   7 | 3
1 | 2	8 | 3	
2 | 3	9 | 3
3 | 3	10| 3
4 | 3	11| 2
5 | 3	12| 1


Iteramount: 13;

ROWS: 3;
COLS: 11;

Iteramount -  COLS = How much from the beginning and end to start ++ or --
  '''
