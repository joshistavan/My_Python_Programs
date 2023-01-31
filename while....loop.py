# i=1
# while i<10:
#     print(i)
#     i+=1

# a=int(input("enter your number"))
# while True:
#     if a<100:
#         a=int(input('Try again bhai'))
#     elif a>100:
#         break
# print('congrulation bro you enter more then value of 100')

# n=18
# gus=1
# print("Number of guesses is limited to only 9 times: ")
# while (gus<=9):
#     guess_number = int(input("Guess the number :\n"))
#     if guess_number<18:
#         print("you enter less number please input greater number.\n")
#     elif guess_number>18:
#         print("you enter greater number please input smaller number.\n ")
#     else:
#         print("you won\n")
#         print(gus,"no.of guesses he took to finish.")
#         break
#     print(9-gus,"no. of guesses left")
#     gus = gus + 1
#
# if(gus>9):
#     print("Game Over")

a=18
gus=1
while gus<=9:
    num=int(input('entetr the number'))
    if num<18:
        print('please incress the number')
    elif num>18:
        print('please decress the number')
    else:
        print('congrulation you are win')
        print(gus,'bhai you have ')
        break
    print(9-gus,'you have left')
    gus+=1
    if gus<9:
        print('game over')








