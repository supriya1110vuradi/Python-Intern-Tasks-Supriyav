# Write a Python program for all the cases which can check a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).Write a Python program for all the cases which can check a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).
import re
string = "HelloWorld321"
pattern = re.compile("[A-Za-z0-9]+")


if pattern.fullmatch(string) is not None:
    print("Found match: " + string)
else:

    print("No match")

# Write a Python program that matches a word containing 'ab'.
import re
pattern = re.compile('a.?b')
string = 'ArabianSea'
if re.search(pattern, string):
    print("found a match!")
else:
    print("not match")

# Write a Python program to check for a number at the end of a word/sentence.
import re
test_string = "Thirty days challenge"
print ("The original string is : " +  test_string)
res = len(test_string.split())
print ("The number of words/sentences in the end : " + str(res))

# Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string
import re
results = re.finditer(r"([0-9]{1,3})", "Hey Hello 123 95 468 going")
print("Number of length 1 to 3")
for n in results:
    print(n.group(0))

# Write a Python program to match a string that contains only uppercase letters
import re


def match(text):
    pattern = '[A-Z]+$'

    if re.search(pattern, text):
        return ('Yes')
    else:
        return ('No')


print(match("HELLO"))
print(match("Folks"))

