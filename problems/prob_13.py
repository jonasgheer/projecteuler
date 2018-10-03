""" Longest Collatz sequence """

def collatz_gen(n):
    """ 
        takes number 'start' and returns next number in sequence
        up to and including 1.
    """
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3*n + 1
        yield n
        
number = 0
longest = 0
for n in range(1, 1_000_000):
    collatz = collatz_gen(n)
    len_seq = 1
    while True:
        try:
            next(collatz) 
        except StopIteration:
            break
        else:
            len_seq += 1
    if len_seq > longest:
        number = n
        longest = len_seq
    
print(f'{number} is the number with the longest sequence of {longest} terms')

            