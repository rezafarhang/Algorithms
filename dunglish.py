word_num = int(input())
sentence = input().split(" ")  # list

good_dic = dict()
bad_dic = dict()

for i in range(int(input())):
    dutch_word, transalte, correctence = input().split(" ")
    if dutch_word not in good_dic:
        good_dic[dutch_word] = []
        bad_dic[dutch_word] = []
    if correctence == "correct":
        good_dic[dutch_word] += [transalte]
    bad_dic[dutch_word] += [transalte]


def possibilities(dic):
    result = 1
    for word in sentence:
        result *= len(dic[word])
    return result


correct_p = possibilities(good_dic)
total_p = possibilities(bad_dic)

if total_p == 1:
    if correct_p == 1:
        for i in range(len(sentence)):
            print(" ".join(good_dic[sentence[i]]), end=" ")
            print("correct")
    else:
        for i in range(len(sentence)):
            print(" ".join(bad_dic[sentence[i]]), end=" ")
        print()
        print("inorrect")

else:
    print(correct_p, "correct")
    print(total_p - correct_p, "incorrect")
