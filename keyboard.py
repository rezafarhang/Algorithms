keyboard = "qwertyuiopasdfghjkl;zxcvbnm,./"
keyboard = list("".join(keyboard))

typ = input()
word = input()
word = list("".join(word))
for i in range(len(word)):
    for j in range(len(keyboard)):
        if word[i] == keyboard[j]:
            if typ == "R":
                print(keyboard[j - 1], end="")
            else:
                print(keyboard[j + 1], end="")
