"""
-------------------------------------------------------
[Program Description]
-------------------------------------------------------
Author:  Ryan Tang
ID:      169061078
Email:   tang1078@mylaurier.ca
__updated__ = "2024-02-09"
-------------------------------------------------------
"""
# Imports

# Constants

def recurse(x, y):
    """
    -------------------------------------------------------
    Recursive function - example of tree recursion.
    Use: ans = recurse(x, y)
    -------------------------------------------------------
    Parameters:
        x - an integer (int)
        y - an integer (int)
    Returns:
        ans - the function result (int)
    -------------------------------------------------------
    """
    ans = 0
    
    if x < 0 or y < 0:
        ans = x-y
    else:
        ans = recurse(x-1, y) + recurse(x, y-1)
    return ans

def gcd(m, n):
    """
    -------------------------------------------------------
    Recursively find the Greatest Common Denominator of two numbers.
    Use: ans = gcd(m, n)
    -------------------------------------------------------
    Parameters:
        n - an integer (int)
        m - an integer (int)
    Returns:
        ans - the function result (int)
    -------------------------------------------------------
    """
    ans = 0
    
    if m % n == 0:
        ans = n
    else:
        ans = gcd(n, m % n)
    return ans

def vowel_count(s):
    """
    -------------------------------------------------------
    Recursively counts number of vowels in a string.
    Use: count = vowel_count(s)
    -------------------------------------------------------
    Parameters:
        s - string to examine (str)
    Returns:
        count - number of vowels in s (int)
    -------------------------------------------------------
    """
    vowels = "aeiouAEIOU"
    
    if s == "":
        count = 0
    else:
        if s[0] in vowels:
            count = 1 + vowel_count(s[1:])
        else:
            count = vowel_count(s[1:])
    return count

def to_power(base, power):
    """
    -------------------------------------------------------
    Calculates base^power.
    Use: ans = to_power(base, power)
    -------------------------------------------------------
    Parameters:
        base - base to apply power to (float)
        power - power to apply (int)
    Returns:
        ans - base ^ power (float)
    -------------------------------------------------------
    """
    if power == 0:
        ans = 1
    elif power < 0:
        ans = 1 / to_power(base, -power)
    else:
        ans = base * to_power(base, power - 1)
    return ans

def is_palindrome(s):
    """
    -------------------------------------------------------
    Recursively determines if s is a palindrome. Ignores non-letters and case.
    Use: palindrome = is_palindrome(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        palindrome - True if s is a palindrome, False otherwise (boolean)
    -------------------------------------------------------
    """
    filtered_s = ''.join([char.lower() for char in s if char.isalpha()])
    palindrome = False
    if len(filtered_s) <= 1:
        palindrome = True
    elif filtered_s[0] == filtered_s[-1]:
        palindrome =  is_palindrome(filtered_s[1:-1])
    else:
        palindrome = False
    return palindrome

def bag_to_set(bag):
    """
    -------------------------------------------------------
    Copies elements of a bag to a set.
    Use: new_set = bag_to_set(bag)
    -------------------------------------------------------
    Parameters:
        bag - a list of values (list)
    Returns:
        new_set - containing one each of the elements in bag (list)
    -------------------------------------------------------
    """
    new_set = []
    
    if len(bag) == 0:
        new_set = []
    else:
        head = bag[0]
        tail = bag_to_set([x for x in bag[1:] if x != head])
        new_set = [head] + tail
    return new_set