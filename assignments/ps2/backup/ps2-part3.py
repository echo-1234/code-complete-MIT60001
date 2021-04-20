def match_with_gaps(my_word, other_word):
    my_word = my_word.replace(' ', '')
    if len(my_word) != len(other_word):
        return False
    else:
        for index in range(len(other_word)):
            if my_word[index] != '_' and my_word[index] != other_word[index]:
                return False
            elif my_word[index] == '_' and other_word[index] in my_word:
                return False
    return True

print(match_with_gaps("te_ t", "tact"))
print(match_with_gaps("a_ _ le", "banana"))
print(match_with_gaps("a_ _ le", "apple"))
print(match_with_gaps("a_ ple", "apple"))
