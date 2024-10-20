
"""
Solutions to module 4
Review date:
"""

student = ""
reviewer = ""

import math as m
import random as random

def sphere_volume(n, d, r):
    # n is a list of set of coordinates
    # d is the number of dimensions of the sphere
    lst = []
    point_in_sphere = lambda point: m.sqrt(sum(point)) <= r

    def _sphere_volume(n, d, r):
        points = [[random.uniform(0, r)**2 for _ in range(d)] for _ in range(n)]
        return list(filter(point_in_sphere, points))

    lst +=_sphere_volume(n, d, r)
    return 2**d*len(lst)/n

def hypersphere_exact(d,r):
    return (m.pi**(d/2)*r**d)/(m.gamma(d/2+1))
     
def main():
    n = 100000
    d = 11
    r = 1
    print(sphere_volume(n,d,r))
    print(hypersphere_exact(d,r))


if __name__ == '__main__':
	main()
