def main(s,n):
    """
    The s string variable is given. return all characters except n characters from the beginning.
    Args:
        s(str): parameter
        n(int): parameter
    Returns:
        str: answer
    """
    s='string'
    return s[n:len(s)]
print(main('string',2))