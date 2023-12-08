
# Given a lowercase string that has alphabetic characters only and no spaces,
# return the highest value of consonant substrings. Consonants are any letters of the alphabet except "aeiou".
# We shall assign the following values: a = 1, b = 2, c = 3, .... z = 26. 

def consonant(s):
    alphabets = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
    max_value = 0 # initialize maximum value to 0
    consonants_value = 0 # holds the substrings/consonants
    vowels = 'aeiou'
    
    for char in s:
        # use index to be value of the tuple
        if char not in vowels:
            char_value = alphabets.index(char) + 1 # add one since a should be 1 not 0
            consonants_value += char_value

        # find maximum value
            max_value = max(max_value, consonants_value)

        # check for character in vowel
        else:
            consonants_value = 0 # Reset to 0
    return max_value

    # ask user for input
prompt = input('Enter a word:')
result = consonant(prompt) # call the function
print(result) # print result




          
    