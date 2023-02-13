#Maximum Number of Words Found in Sentences A sentence is a list of words that are separated by a single space with no leading or trailing spaces.
Sol:
str1=input("Enter the sentence: ")
str2=str1.split(",")
print(len(str2))
print(str2)
count=[]
for i in range(len(str2)):
    str3=(str2[i].split(" "))
    print(str3)
    count.append(len(str3))
print(max(count))

#Output:
Enter the sentence: "alice and bob love leetcode","i think so too","this is great thanks very much"
6
