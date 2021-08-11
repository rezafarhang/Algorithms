n = int(input())
game = []
for i in range(n):
    game.append(input())

flag = True
for line in game:
    if "OO" in line:
        print("YES")
        flag = False
        break
if flag:
    print("NO")
else:
    for line in game:
        if ("OO" in line) and (flag == False):
            if line[0] == "O" and line[1] == "O":
                print("++",end="")
                for i in range(2,5):
                    print(line[i],end="")
            elif line[3] == "O" and line[4] == "O":
                for i in range(3):
                    print(line[i],end="")
                print("++",end="")
            print()
            flag = True
        else:
            print(line)