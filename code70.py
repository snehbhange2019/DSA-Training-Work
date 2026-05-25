str1 = "listen"
str2 = "silent"

if len(str1) != len(str2):
    print("Not Anagrams")
else:
    flag = 1
    for i in range(len(str1)):
        count1 = 0
        count2 = 0
        for j in range(len(str1)):
            if str1[i] == str1[j]:
                count1 = count1 + 1
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                count2 = count2 + 1
        if count1 != count2:
            flag = 0
            break
    if flag == 1:
        print("Anagrams")
    else:
        print("Not Anagrams")