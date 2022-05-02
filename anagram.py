word1 = "cArm"
word2 = "RaCe"
word1 = word1.lower()
word2 = word2.lower()
if len(word1) == len(word2):
    print("Length of both words is same. We can proceed further.")
    if sorted(word1) == sorted(word2):
        print("Words are anagram")
    else:
        print("Words are not an anagram.")
else:
    print("Length of both words is not same. Hence not an anagram.")
