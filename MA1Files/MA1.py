"""
Solutions to module 1
Student: Hugo Vennergrund Blom
Mail: hugo.vennergrund-blom.9969@student.uu.se
Reviewed by: Stephan
Reviewed date: 2024-09-06
"""

"""
Important notes: 
These examples are intended to practice RECURSIVE thinking. Thus, you may NOT 
use any loops nor built in functions like count, reverse, zip, math.pow etc. 

You may NOT use any global variables.

You can write code in the main function that demonstrates your solutions.
If you have testcode running at the top level (i.e. outside the main function)
you have to remove it before uploading your code into Studium!
Also remove all trace and debugging printouts!

You may not import any packages other than time and math and these may
only be used in the analysis of the fib function.

In the oral presentation you must be prepared to explain your code and make minor 
modifications.

We have used type hints in the code below (see 
https://docs.python.org/3/library/typing.html).
Type hints serve as documatation and and doesn't affect the execution at all. 
If your Python doesn't allow type hints you should update to a more modern version!
"""

import time
import math

def multiply(m: int, n: int) -> int:  
    """ Computes m*n using additions"""
    if n == 0:
        return 0
    else:
        return m + multiply(m, n-1)
    


def harmonic(n: int) -> float:              
    """ Computes and returns the harmonc sum 1 + 1/2 + 1/3 + ... + 1/n"""
    if n == 1:
        return 1
    else:
        return 1/n + harmonic(n-1)


def get_binary(x: int) -> str:              
    """ Returns the binary representation of x """
    strmod = ''
    if x < 0:
        x *= -1
        strmod = '-'

    if x == 0:
        return strmod + '0'
    elif x == 1:
        return strmod + '1'
    else:
        return strmod + get_binary(int(x/2)) + str(x % 2)


def reverse_string(s: str) -> str:        
    """ Returns the s reversed """
    if len(s) > 1:
        return s[-1] + reverse_string(s[:-1])
    else:
        return s


def largest(a: iter):                     
    """ Returns the largest element in a"""
    if len(a) == 1:
        return a[-1]
    else:
        if a[0] > a[-1]:
            return largest(a[:-1])
        else:
            return largest(a[1:])


def count(x, s: list) -> int:                
    """ Counts the number of occurences of x on all levels in s"""
    if len(s) == 0:
        return 0
    else:
        if s[0] == x:
            return 1 + count(x, s[1:])
        elif isinstance(s[0], list):
            return count(x, s[0]) + count(x, s[1:])
        else:
            return count(x, s[1:])


def bricklek(f: str, t: str, h: str, n: int) -> str:
    if n == 0: return []
    return bricklek(f, h, t, n - 1) + [f + "->" + t] + bricklek(h, t, f, n - 1)


def fib(n: int) -> int:                      
    """ Returns the n:th Fibonacci number """
    # You should verify that the time for this function grows approximately as
    # Theta(1.618^n) and also estimate how long time the call fib(100) would take.
    # The time estimate for fib(100) should be in reasonable units (most certainly
    # years) and, since it is just an estimate, with no more than two digits precision.
    #
    # Put your code at the end of the main function below!
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def fib_mem(n, memory = None):
    if memory is None:
        memory = {0: 0, 1: 1}
    if n not in memory:
        memory[n] = fib_mem(n-1, memory) + fib_mem(n-2, memory)
    return memory[n]


def main():

    print('\nCode that demonstates my implementations\n')
    tiles = 1
    print(f'Nr of moves in tile game with {tiles} tiles: {len(bricklek('f','t','h',tiles))}')
    print('\n\nCode for analysing fib and fib_mem\n')
    #fib
    n_stop = 35
    for n in range(20, 41):
        t = time.perf_counter_ns()
        fib(n)
        #fib_mem(n)
        print(f'{time.perf_counter_ns() - t}')
    #print(f'fib_mem(n=100) = {fib_mem(100)}')
    print('\nBye!')


if __name__ == "__main__":
    main()

####################################################

"""
  Answers to the none-coding tasks
  ================================
  
  
  Exercise 8: Time for the tile game with 50 tiles:
    If each move takes one sec then it will take 1.13*10^15 seconds or about 3.6*10^7 years

  
  
  Exercise 9: Time for Fibonacci:
    The function grows as Theta(1.618^n) as seen in Theta(1.618^n) och Fib Runtime.png, using C = 79.27. The time for n=50 on my computer is approximately 37 min and for n=100 it will take approximately 2*10^6 years.

  
  
  Exercise 10: Time for fib_mem:
    Fib_mem took 17600 ns to run for n=100 and the value is 354224848179261915075
  
  
  
  
  Exercise 11: Comparison sorting methods:
    Insertion sort:
        Theta(1000^2) = 1 sec -> Theta(10^6^2) = 11.6 days and Theta(10^9^2) = 31700 years
    Merge sort:
        Theta(1000*log(1000)) = 1 sec -> Theta(10^6*log(10^6)) = 33 min -> Theta(10^9*log(10^9)) = 34.7 days
  
  
  
  Exercise 12: Comparison Theta(n) and Theta(n*log(n))
    n*log(n) = n -> log(n) = 1 -> n = 10
    Answer: Theta(n) is faster than Theta(n*log(n)) when n > 10
  
"""
