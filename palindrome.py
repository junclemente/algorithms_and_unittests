def find_palindrome(a):
    """Returns the largest palindrome found within a string

    Efficiency: O(n)

    Parameters:
    -----------
    a : string

    Returns:
    --------
    palindrome
        The largest palindrome substring contained in a.
    message
        A message explaining why a palindrome was not found.
    """

    MIN_PALINDROME_LENGTH = 3
    palindrome = ""
    word = a.replace(" ", "")
    p_hash = {}

    if len(a) < MIN_PALINDROME_LENGTH:
        return ("The string '{}' is too short to check for "
                "palindromes.".format(a))

    # Create hash table of all char and creates a list of indices.
    for i in range(len(word)):
        if word[i] in p_hash:
            p_hash[word[i]].append(i)
        else:
            p_hash[word[i]] = [i]

    # Iterate through all keys in hash table
    # If the list for the key(character) has more than one element,
    # It will iterate through the combinations of indices to determine if it
    # is a palindrome replacing the palindrome whenever a longer palindrome
    # is found.
    for key in p_hash:
        if len(p_hash[key]) > 1:
            index_list = p_hash[key]
            for x in range(len(index_list) - 1):
                y = x + 1
                while y < len(index_list):
                    check = word[index_list[x]: index_list[y] + 1]
                    if (len(check) >= MIN_PALINDROME_LENGTH
                       and len(check) > len(palindrome)):
                            if (check == check[::-1]):
                                palindrome = check
                    y += 1

    return palindrome or "There are no palindromes found in '{}'.".format(a)
