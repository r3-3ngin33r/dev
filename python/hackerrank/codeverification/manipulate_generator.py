#@author: r33 - r33ngin33r@gmail.com
#@timestamp_creation: 02/19/2019 - 01:29 GMT-3

def manipulate_generator(generator, n):
    # Enter your code here
    #Check if a number is prime
    def isprime(n):
        '''Simple function to check if a natural number is prime

        Args:
            number (int): A natural number

        Raises:
            ValueError: Negative argument

        Returns:
            boolean value: True if n is prime, False if not
        '''
        if n < 1:
            raise ValueError("Negative Number")
        if n == 1 :
            return False
        elif n == 2:
            return True
        else:
            for x in range(2,n):
                if (n % x == 0) :
                    return False
            return True

    #Check if the next number is not prime and must be printed
    if not isprime(n + 1):
        return #Return to the main loop
    else:
        n = next(generator) 
        manipulate_generator(generator, n) #Continue inside this function in order to prevent the prime number printing in the main loop
        
def positive_integers_generator():
    n = 1
    while True:
        x = yield n
        if x is not None:
            n = x
        else:
            n += 1

k = int(input())
g = positive_integers_generator()
for _ in range(k):
    n = next(g)
    print(n)
