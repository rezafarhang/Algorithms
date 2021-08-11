import string

n = int(input())
truth_list = input().split()
circut = input().split()

truth_dic = dict()
counter = 0
for i in range(ord('A'), ord(string.ascii_uppercase[n - 1]) + 1):
    truth_dic[chr(i)] = truth_list[counter]
    counter += 1

stack = []
for i in range(len(circut)):
    if circut[i] in "*+-":
        continue
    else:
        circut[i] = truth_dic[circut[i]]

stacki, listi = 0, 0
while listi != len(circut):
    if circut[listi] not in "*+-":
        stack.append(circut[listi])
        stacki += 1
    else:
        if circut[listi] == '*':
            x = stack.pop(stacki - 1)
            y = stack.pop(stacki - 2)
            stacki -= 2
            if x == 'T' and y == 'T':
                stack.append('T')
            else:
                stack.append('F')
            stacki += 1

        elif circut[listi] == '+':
            x = stack.pop(stacki - 1)
            y = stack.pop(stacki - 2)
            stacki -= 2
            if x == 'F' and y == 'F':
                stack.append('F')
            else:
                stack.append('T')
            stacki += 1


        elif circut[listi] == '-':
            x = stack.pop(stacki - 1)
            stacki -= 1
            if x == 'T':
                stack.append('F')
            else:
                stack.append('T')
            stacki += 1
    listi += 1
print(stack[0])