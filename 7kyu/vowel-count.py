# Return the number (count) of vowels in the given string.
#
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
#
# The input string will only consist of lower case letters and/or spaces.


# My solutions
def get_count(sentence):
    answ = 0
    for i in ["a", "e", "i", "o", "u"]:
        answ += sentence.count(i)
    return answ