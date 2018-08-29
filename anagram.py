# Question 1

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def is_anagram(s, t):
    """Determines if t is an anagram of s.

    The function will take in two strings. Any non-alphabetic character will be
    removed then it will determine if t is an anagram of s. Case will not be a
    determining factor.

    Efficiency: O(n)

    Parameters
    ----------
    s : string
        The string to be compared to
    t : string
        The substring to determine if it is an anagram of s

    Returns
    -------
    boolean
        If t is an anagram of s, the function will return True, otherwise,
        it will return False
    """

    # Return False is an empty string is provided.
    if not s or not t:
        return False

    string = s.lower()
    test = t.lower()

    string = string.replace(" ", "")
    test = test.replace(" ", "")

    if test in string:
        return False

    # Create hash table for s
    s_hash = {}
    for letter in string:
        if letter in ALPHABET:
            if letter in s_hash:
                s_hash[letter] += 1
            else:
                s_hash[letter] = 1

    # Return False if no alpha char entered.
    if len(s_hash) < 1:
        return False

    # Create hash table for t
    t_hash = {}
    for letter in test:
        if letter in ALPHABET:
            if letter in t_hash:
                t_hash[letter] += 1
            else:
                t_hash[letter] = 1

    # Return False if no alpha char entered.t
    if len(t_hash) < 1:
        return False

    # Compare the t_hash to s_hash
    for key in t_hash:
        if key not in s_hash:
            return False
        else:
            # If t_hash has higher letter count than s_hash,
            # it cannot be an anagram
            if t_hash[key] > s_hash[key]:
                return False
    return True



