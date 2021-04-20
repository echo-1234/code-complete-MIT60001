# Problem Set 4A
# Name: Echo Zhou
# Collaborators:
# Time Spent: 1 hr

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    ## if the sequence only have one char, return the char as only permutation
    if len(sequence) == 1:
        permutations = [sequence]

    ## otherwise (sequence length longer than one)
    else:
        ## the last element is poped out
        char = sequence[0]
        ## the rest of the sequence is recursed to get the permutations for the reduced sequence
        reduced_permutations = get_permutations(sequence[1:])

        ## initialize to store all the permutations
        permutations = []

        ## loop through all permutations for the reduced sequence
        for each_permutation in reduced_permutations:

            ## for each reduced permutation, construct new permutations
            for i in range(len(each_permutation)+1):
                ## the new sequence is constructed by inserting the character at different locations
                each_permutation_insert = each_permutation[0:i] + char + each_permutation[i:]
                ## and append to the list
                permutations.append(each_permutation_insert)

    return permutations




if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))

#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a
#    sequence of length n)

    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))

    example_input = 'a'
    print('Input:', example_input)
    print('Expected Output:', ['a'])
    print('Actual Output:', get_permutations(example_input))

    example_input = 'lg'
    print('Input:', example_input)
    print('Expected Output:', ['lg', 'gl'])
    print('Actual Output:', get_permutations(example_input))
