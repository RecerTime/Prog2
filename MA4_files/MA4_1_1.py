"""
Solutions to module 4
Review date:
"""

student = "Hugo Vennergrund Blom"
reviewer = ""

import random as r
import math
import matplotlib.pyplot as plt

def approximate_pi(n):
    in_circle = lambda point: math.sqrt(point[0]**2 + point[1]**2) <= 1

    points_out_circle = []
    points_in_circle = []

    for _ in range(n):
        point = (r.uniform(-1, 1), r.uniform(-1, 1))
        if in_circle(point):
            points_in_circle.append(point)
        else:
            points_out_circle.append(point)

    #print(len(points_in_circle))
    pi = 4*len(points_in_circle)/n
    #print(pi)
    #print(math.pi)

    #plt.figure(figsize=(10,10))
    #plt.scatter([point[0] for point in points_in_circle], [point[1] for point in points_in_circle], c='blue')
    #plt.scatter([point[0] for point in points_out_circle], [point[1] for point in points_out_circle], c='red')

    #plt.savefig(f'{n}.png')
    #plt.show()

    return pi
    
def main():
    dots = [1000, 10000, 100000]
    for n in dots:
        approximate_pi(n)

if __name__ == '__main__':
	main()
