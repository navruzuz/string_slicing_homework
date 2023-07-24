def main(s):
    """
    The s string variable is given. return the characters in the odd position.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    s='string'
    return s[3:len(s)]+s[0:3]
print(main('string'))