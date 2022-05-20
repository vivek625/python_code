from random import choice , randint
correct = 5
incorrect = 0

ops = ['+','-','*','/']
while correct > 0:
    if incorrect == 5:
        print("Shame on you !!! you have lost the game")
        break
    a,b,c,d = (randint (10,20) for _ in range(4))
    x,y,z = (choice(['+','-','*','/']) for _ in range(3))
    expr = f"{a}{x}{b}{y}{c}{z}{d}"
    ans = int(eval(expr))
    uans = int(input(expr+" = "))
    if uans == ans:
        print("!!correct!!")
    else:
        incorrect += 1
        print("!!Incorrect!!")
        print("correct ans: ",ans)
        continue
    correct -= 1
else:
    print("congrats !!! you such a master ")