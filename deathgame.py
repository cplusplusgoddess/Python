'''This is an Amazon challenge:
 There are n people standing in a circle (numbered clockwise 1 to n) waiting to be executed.
 The counting begins at point 1 in the circle and proceeds around the circle in a fixed direction (clockwise).
 In each step, a certain number of people are skipped and the next person is executed.
 The elimination proceeds around the circle (which is becoming smaller and smaller as the executed people are removed)
 , until only the last person remains, who is given freedom.
 Given the total number of persons n and a number k which indicates that k-1 persons are skipped and kth person
 is killed in circle. The task is to choose the place in the initial circle so that you are the last one
 remaining and so survive.
 Consider if n = 5 and k = 2, then the safe position is 3.
 Firstly, the person at position 2 is killed, then person at position 4 is killed, then person at position 1 is killed.
 Finally, the person at position 5 is killed. So the person at position 3 survives.'''
import sys
def find_lucky_one(n,k):
    '''for a circle of n prisoners, execute all but the last remaining, and skip k-1 between executions
    and return the last living prisoner position '''
    if k>0: k -= 1  #insure k non-negative
    else: k = 0
    deathRow = []
    for i in range(1,n+1):
        deathRow += [i]
    #print(deathRow)
    currentIdx= 0
    while( len(deathRow) > 1):
        currentIdx = ( currentIdx+k  < len(deathRow) ) and (currentIdx+k) or (  abs(len(deathRow)-(currentIdx+k) )% len(deathRow) )
        del deathRow[currentIdx]
    return deathRow[0]

num_cases = int(input('enter number of test cases to follow: '))
for _ in range( num_cases ):
    n,k = map(int,input().split())
    print( n, " prisoners, skipping ", k , ' the lucky one is position: ', find_lucky_one( n, k ) )

''' For fast test io:
num_cases = int(sys.stdin.readline() )
for _ in range( num_cases ):
    #integer input from user, 2 input in single line
    n,k = map(int,input().split()) 
    print( find_lucky_one( n, k ) ) '''


