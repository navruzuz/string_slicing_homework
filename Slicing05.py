def main(s,n):
    """
    The s string variable is given. return n characters from the end.
    Args:
        s(str): parameter
        n(int): parameter
    Returns:
        str: answer
    """
    s='string'
    return s[n:len(s)]
print(main('string',-3))
