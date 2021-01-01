import pprint

board = {'top-L':' ','top-M':' ','top-R':' ','mid-L':' ','mid-M':' ','mid-R':' ','low-L':' ','low-M':' ','low-R':' '}

#pprint.pprint(board)


print("Welcome to the TIC TAC TOE \n\t\t-made by Anonymous with efforts")
print("Enter the name of the players below to enter the game\nPlayer 1 : ",end='')
player0=input()
player1=input("Player 2 : ")

print("Welcome {} and {}. Let's begin below are rules.".format(player0,player1))
print("\n Rules are :- \n1.Once entered can't be changed.\n2.Enter 1 for top left, 2 for top mid and 3. for top right.")
print("3. Similarly 4 for middle left, 7 for lower left and so on.")

print("\n\n\t 1\t|\t2\t|\t3")
print("\t-----------------------------------")
print("\t 4\t|\t5\t|\t6")
print("\t-----------------------------------")
print("\t 7\t|\t8\t|\t9\n\n")

temp={}
temp1=1
for i in board.keys():
    temp.setdefault(temp1,'')
    temp[temp1]=i
    temp1=temp1+1

#pprint.pprint(temp)

def pboard(board):
    print("\n\t "+board['top-L']+"\t|\t"+board['top-M']+"\t|\t"+board['top-R'])
    print("\t-----------------------------------")
    print("\n\t "+board['mid-L']+"\t|\t"+board['mid-M']+"\t|\t"+board['mid-R'])
    print("\t-----------------------------------")
    print("\n\t "+board['low-L']+"\t|\t"+board['low-M']+"\t|\t"+board['low-R'])

y=0
done=''
while(True):
    pboard(board)
    z='player'+str(y%2+1)
    print(z,end='  => ')
    x=int(input("Enter the place : "))
    if(x<1 or x>9):
        print("wrong input")
        continue
    if (y%2==0):
        board[temp[x]]='X'
        print("\nAfter "+player0+"'s  turn :-")
    else:
        board[temp[x]]='O'
        print("\nAfter "+player1+"'s  turn :-")
    y+=1
    if y>4:
        if(board['top-L']==board['top-R'] and  board['top-R']==board['top-M'] and (board['top-R']=='X' or board['top-R']=='X')):
            pboard(board)
            #pprint.pprint(board)
            break
        elif(board['mid-L']==board['mid-M'] and  board['mid-M']==board['mid-R'] and (board['mid-R']=='X' or board['mid-R']=='X')):
            pboard(board)
            #pprint.pprint(board)
            break
        elif(board['low-L']==board['low-M'] and  board['low-M']==board['low-R'] and (board['low-R']=='X' or board['low-R']=='X')):
            pboard(board)
            #pprint.pprint(board)
            break
        elif(board['top-L']==board['mid-L'] and  board['mid-L']==board['low-L'] and (board['top-L']=='X' or board['top-L']=='X')):
            pboard(board)
            #pprint.pprint(board)
            break
        elif(board['top-M']==board['mid-M'] and  board['mid-M']==board['low-M'] and (board['top-M']=='X' or board['top-M']=='X')):
            pboard(board)
            #pprint.pprint(board)
            break
        elif(board['top-R']==board['mid-R'] and  board['mid-R']==board['low-R'] and (board['low-R']=='X' or board['low-R']=='X')):
            pboard(board)
            #pprint.pprint(board)
            break
        elif(board['top-L']==board['mid-M'] and  board['mid-M']==board['low-R'] and (board['low-R']=='X' or board['low-R']=='X')):
            pboard(board)
            #pprint.pprint(board)
            break
        elif(board['top-R']==board['mid-M'] and  board['mid-M']==board['low-L'] and (board['top-R']=='X' or board['top-R']=='X')):
            pboard(board)
            #pprint.pprint(board)
            break
        else:
            pass
    

    '''check for the below loop
some error is there based on looping mthod.... musst check''' 
    if str(x) in done:
            y=y-1
            print("Already done...")
            #board[temp[x]]=' '
            continue
    done+=str(x)
    
if(y%2==0):
    print("Congracts "+player0+" won !!")
else:
    print("Congracts "+player1+" won !!")

        
    #pprint.pprint(board)
    
