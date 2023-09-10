print("\t\t\t*****WELCOME TO TIC_TAC_TOE*****")
print("\n\n\n\nRules of the game\n\n1. The game is played on a grid that's 3 squares by 3 squares.\n\n2. If you are 'x', your friend will be 'o', or if you are 'o', your friend will be 'x'.Players take turns putting their marks in empty squares.\n\n3. The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.")
op=[""," "," "," "," "," "," "," "," "," "]
num=[]
num1=[]
dum=[1,2,3,4,5,6,7,8,9]
player_1s=input("\n\n\nplayer_1 ('x' or 'o')=")
if (player_1s=='x') or (player_1s=='X'):
    player_2s='o'
    print("\n\nplayer_2= 'o' ")

elif (player_1s=='o') or (player_1s=='O'):
    player_2s='x'
    print("\n\nplayer_2= 'x'")



def choice():
    if (player_1s!='x') and (player_1s!='o') and (player_2s!='x') and (player_2s!='o'):
        print("\nWrong Option!!! choose 'x' or 'o'")
        choice()

choice()
print("\n\t\t\tLet's start the game!!!\n\n\nPositions is like this!!!")
print("1  |2  |3\n---|---|---\n4  |5  |6\n---|---|---\n7  |8  |9")

a=0
def check():
    global a
    
    if ((op[0+1]==player_1s) and (op[1+1]==player_1s) and (op[2+1]==player_1s)) or ((op[3+1]==player_1s) and (op[4+1]==player_1s) and (op[5+1]==player_1s)) or ((op[6+1]==player_1s) and (op[7+1]==player_1s) and (op[8+1]==player_1s)) or ((op[0+1]==player_1s) and (op[3+1]==player_1s) and (op[6+1]==player_1s)) or ((op[1+1]==player_1s) and (op[4+1]==player_1s) and (op[7+1]==player_1s)) or ((op[2+1]==player_1s) and (op[5+1]==player_1s) and (op[8+1]==player_1s)) or ((op[0+1]==player_1s) and (op[4+1]==player_1s) and (op[8+1]==player_1s)) or ((op[2+1]==player_1s) and (op[4+1]==player_1s) and (op[6+1]==player_1s)):
        print("\n\n\t\t\tplayer 1 is winner")
        a=1
    elif ((op[0+1]==player_2s) and (op[1+1]==player_2s) and (op[2+1]==player_2s)) or ((op[3+1]==player_2s) and (op[4+1]==player_2s) and (op[5+1]==player_2s)) or ((op[6+1]==player_2s) and (op[7+1]==player_2s) and (op[8+1]==player_2s)) or ((op[0+1]==player_2s) and (op[3+1]==player_2s) and (op[6+1]==player_2s)) or ((op[1+1]==player_2s) and (op[4+1]==player_2s) and (op[7+1]==player_2s)) or ((op[2+1]==player_2s) and (op[5+1]==player_2s) and (op[8+1]==player_2s)) or ((op[0+1]==player_2s) and (op[4+1]==player_2s) and (op[8+1]==player_2s)) or ((op[2+1]==player_2s) and (op[4+1]==player_2s) and (op[6+1]==player_2s)):
        print("\n\n\t\t\tplayer 2 is winner")
        a=1    
    elif dum == sorted(num1):
        print("Match tie!!!")
        a=1
        
    else:
        pass
        
def player_1():
    global a
    check()
    if a!=1:
        pos=input("player_1, Enter the position (1-9):")
        if int(pos)>=1 and int(pos)<=9:
   
            if pos not in num:
                if (player_1s=='x'):
                    op[int(pos)]='x'
                elif (player_1s=='o'):
                     op[int(pos)]='o'
                else:
                    pass
                print(f"{op[0+1]}  |{op[1+1]}  |{op[2+1]}\n---|---|---\n{op[3+1]}  |{op[4+1]}  |{op[5+1]}\n---|---|---\n{op[6+1]}  |{op[7+1]}  |{op[8+1]}")
                num.append(pos)
                num1.append(int(pos))
            elif pos in num:
                print("\nThis position is already taken!!! Choose another position")
                player_1()
        else:
            print("Please enter correct position!!!")
            player_1()
    
def player_2():
      global a
      check()
      if a!=1:
          pos=input("player_2, Enter the position (1-9):")
          if int(pos)>=1 and int(pos)<=9:
              if pos not in num:
                  if (player_2s=='x'):
                     op[int(pos)]='x'
                  elif (player_2s=='o'):
                      op[int(pos)]='o'
                  else:
                      pass
                  print(f"{op[0+1]}  |{op[1+1]}  |{op[2+1]}\n---|---|---\n{op[3+1]}  |{op[4+1]}  |{op[5+1]}\n---|---|---\n{op[6+1]}  |{op[7+1]}  |{op[8+1]}")
                  num.append(pos)
                  num1.append(int(pos))
              elif pos in num:
                 print("\n\nThis position is already taken!!! Choose another position")
                 player_2()
          else:
              print("Please enter correct position!!!")
              player_2()
             
for i in range(10):
    if a!=1:
        player_1()
        if a!=1:
            player_2()
    