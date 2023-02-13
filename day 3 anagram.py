#Given an array of strings strs, group the anagrams together. You can
#return the answer in any order. An Anagram is a word or phrase formed by
#rearranging the letters of a different word or phrase, typically using all the original letters exactly once. strs[i] consists of lowercase English letters.

Program:

def anagram(li):
    dictionary={}
    for word in li:
        sortedword=''.join(sorted(word))
        print(sortedword)
        if sortedword not in dictionary:
            dictionary[sortedword]=[word]
        else:
           dictionary[sortedword]+=[word]
        return[dictionary[i] for i in dictionary]
li=['pop','bat','tab','opp']
print(anagrame(li))

#Output:
opp
[['pop']]
