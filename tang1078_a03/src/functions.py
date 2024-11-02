"""
-------------------------------------------------------
[Program Description]
-------------------------------------------------------
Author:  Ryan Tang
ID:      169061078
Email:   tang1078@mylaurier.ca
__updated__ = "2024-01-26"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
# Constants

def stack_combine(source1, source2):
    """
    -------------------------------------------------------
    Combines two source stacks into a target stack.
    When finished, the contents of source1 and source2 are interlaced
    into target and source1 and source2 are empty.
    Use: target = stack_combine(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a stack (Stack)
        source2 - another stack (Stack)
    Returns:
        target - the contents of the source1 and source2
            are interlaced into target (Stack)
    -------------------------------------------------------
    """
    target = Stack()
    
    while not source1.is_empty() or not source2.is_empty():
        if not source1.is_empty():
            target.push(source1.pop())
        if not source2.is_empty():
            target.push(source2.pop())
    return target
    
def stack_reverse(source):
    """
    -------------------------------------------------------
    Reverses the contents of a stack.
    Use: stack_reverse(source)
    -------------------------------------------------------
    Parameters:
        source - a Stack (Stack)
    Returns:
        None
    -------------------------------------------------------
    """ 
    list = Stack()
    while not source.is_empty():    
        list.push(source.pop())   
    while not list.is_empty():       
        source.push(list.pop())  
    return

def is_palindrome_stack(string):
    """
    -------------------------------------------------------
    Determines if string is a palindrome. Ignores case, digits, spaces, and
    punctuation in string.
    Use: palindrome = is_palindrome_stack(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        palindrome - True if string is a palindrome, False otherwise (bool)
    -------------------------------------------------------
    """
    stack = Stack()
    cleaned_string = ""
    
    palindrome = True

    for char in string:
        if char.isalnum():
            cleaned_string += char.lower()

    for char in cleaned_string[:len(cleaned_string) // 2]:
        stack.push(char)

    start_index = len(cleaned_string) // 2
    if len(cleaned_string) % 2 != 0:
        start_index += 1

    for char in cleaned_string[start_index:]:
        if stack.is_empty() or stack.pop() != char:
            palindrome = False

    return palindrome

# Constants
OPERATORS = "+-*/"

def postfix(string):
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = postfix(string)
    -------------------------------------------------------
    Parameters:
        string - the postfix string to evaluate (str)
    Returns:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """
    stack = Stack()

    elements = string.split()

    for element in elements:
        if element in OPERATORS:
            right = stack.pop()
            left = stack.pop()

            if element == '+':
                stack.push(left + right)
            elif element == '-':
                stack.push(left - right)
            elif element == '*':
                stack.push(left * right)
            elif element == '/':
                stack.push(left / right)
        else:
            stack.push(float(element))

    answer = stack.pop()
    
    return answer

def stack_maze(maze):
    """
    -------------------------------------------------------
    Solves a maze using Depth-First search.
    Use: path = stack_maze(maze)
    -------------------------------------------------------
    Parameters:
        maze - dictionary of points in a maze, where each point
            represents a corridor end or a branch. Dictionary
            keys are the name of the point followed by a list of
            branches, if any. First point is named 'Start', exit
            is named 'X' (dict)
    Returns:
        path - list of points visited before the exit is reached,
            does not include 'Start', but does include 'X'.
            Return None if there is no exit (list of str)
    -------------------------------------------------------
    """
    stack = Stack()
    stack.push('Start')
    visited = set()
    path = []
    integer = 90
    var1 = 
    
    string = "fgdsr94whg9t4p'4'3tl'43"
    float = 
    while not stack.is_empty():
        current_point = stack.peek()
        if current_point == 'X':
            path += ["X"]
            path.pop(0)
            return path
        
        if current_point not in visited:
            visited.add(current_point)
            path.append(current_point)  
            
            for next_point in maze.get(current_point, []):
                if next_point not in visited:
                    stack.push(next_point)
                    
        else:
            stack.pop() 
        
            
    return