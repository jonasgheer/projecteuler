""" Largest palindrome product """

def is_pal(n):
    n = str(n)
    if n == n[::-1]:
        return True
    else:
        return False

def largest_palindrome_product(n_d=3):
    """ 
        Find largest palindrome product 
        n_d : number of digits 
    """
    palindromes = []
    m = 10**n_d 
    for i in range(1, m):
        for j in range(1, m):
            if is_pal(i*j):
                palindromes.append(i*j)

    return max(palindromes)
    
print('Largest palindrome product:', largest_palindrome_product())
