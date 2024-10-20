
"""
Solutions to module 4
Review date:
"""

student = ""
reviewer = ""

from time import perf_counter as pc
import math as m
import random
import concurrent.futures

def sphere_volume(args):
    # n is a list of set of coordinates
    # d is the number of dimensions of the sphere
    n, d, r = args
    lst = []
    point_in_sphere = lambda point: m.sqrt(sum(point)) <= r

    def _sphere_volume(args):
        n, d, r = args
        points = [[random.uniform(0, r)**2 for _ in range(d)] for _ in range(n)]
        return list(filter(point_in_sphere, points))

    lst +=_sphere_volume(args)
    return 2**d*len(lst)/n

def hypersphere_exact(d,r):
    return (m.pi**(d/2)*r**d)/(m.gamma(d/2+1))

# parallel code - parallelize for loop
def sphere_volume_parallel1(n, d, r, np):
     #using multiprocessor to perform 10 iterations of volume function
    args = [(n, d, r) for _ in range(np)]
    with concurrent.futures.ProcessPoolExecutor() as ex:
        results = ex.map(sphere_volume, args)
    return float(sum(results)/np)

# parallel code - parallelize actual computations by splitting data
def sphere_volume_parallel2(n, d, r, np):
    args_lst = [(int(n / np), d, r) for _ in range(np)]
    with concurrent.futures.ProcessPoolExecutor(max_workers=np) as ex:
        results = ex.map(sphere_volume, args_lst)
    
    return sum(results)/np

def main():
    np = 10
    # part 1 -- parallelization of a for loop among 10 processes 
    n = 100000
    d = 11
    r = 1
    
    start = pc()
    vol_sum = 0 
    for _ in range(np):
        vol_sum += sphere_volume((n, d, r))
    vol = vol_sum/np
    end = pc()
    print(f'{np} runs: {vol}, in {round(end-start, 2)} seconds')
    
    start = pc()
    vol = sphere_volume_parallel1(n, d, r, np)
    end = pc()
    print(f'Multiprocessor {np} runs: {vol}, in {round(end-start, 2)} seconds')

    start = pc()
    vol = sphere_volume_parallel2(n, d, r, np)
    end = pc()
    print(f'Parallel {np} runs: {vol}, in {round(end-start, 2)} seconds')

    print(f'Actual vol: {hypersphere_exact(d, r)}')

if __name__ == '__main__':
	main()
