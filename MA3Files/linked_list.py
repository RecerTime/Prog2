""" linked_list.py

Student: Hugo Vennergrund BLom
Mail: hugo.vennergrund-blom.9969@student.uu.se
Reviewed by:
Date reviewed:
"""


class LinkedList:

    class Node:
        def __init__(self, data, succ):
            self.data = data
            self.succ = succ

    def __init__(self):
        self.first = None

    def __iter__(self):            # Discussed in the section on iterators and generators
        current = self.first
        while current:
            yield current.data
            current = current.succ

    def __in__(self, x):           # Discussed in the section on operator overloading
        for d in self:
            if d == x:
                return True
            elif x < d:
                return False
        return False

    def insert(self, x):
        if self.first is None or x <= self.first.data:
            self.first = self.Node(x, self.first)
        else:
            f = self.first
            while f.succ and x > f.succ.data:
                f = f.succ
            f.succ = self.Node(x, f.succ)

    def print(self):
        print('(', end='')
        f = self.first
        while f:
            print(f.data, end='')
            f = f.succ
            if f:
                print(', ', end='')
        print(')')

    # To be implemented

    def length(self):
        n = 0
        f = self.first
        while f:
            n += 1
            f = f.succ
        return n

    def mean(self):               
        n = 0
        val = 0
        f = self.first
        while f:
            val += f.data
            n += 1
            f = f.succ
        if n == 0: raise ValueError
        return val/n

    def remove_last(self):
        f = self.first
        if not f:
            raise ValueError
        
        prev = f
        while f.succ:
            prev = f
            f = f.succ

        prev.succ = None
        result = f.data

        if f == self.first:
            self.first = None

        return result

    def remove(self, x):
        f = self.first
        found_x = False
        prev = None

        while f:
            found_x = f.data == x
            if found_x:
                if not prev: #Removes first element
                    self.first = f.succ
                else:
                    prev.succ = f.succ
                break
            prev = f
            f = f.succ
        
        return found_x

    def to_list(self):

        def _to_list(f):
            if f is None:
                return []
            else:
                return [f.data] + _to_list(f.succ)
            
        return _to_list(self.first)

    def remove_all(self, x):
        
        def _remove_all(f, x):
            if f.remove(x):
                return 1 + _remove_all(f, x)
            else:
                return 0
        
        return _remove_all(self, x)

    def __str__(self):
        ret_str = ''
        for data in self:
            ret_str += f'{data}, '

        return '(' + ret_str[:-2] + ')'
     

    def copy_1(self):               #
        result = LinkedList()
        for x in self:
            result.insert(x)
        return result
    ''' Complexity for this implementation: 
        O(n^2)
    '''

    def copy(self):
        result = LinkedList()
        for i in reversed(self.to_list()):
            result.insert(i)
        return result
    ''' Complexity for this implementation:
        O(n)
    '''

def main():
    lst = LinkedList()
    n = 10e6
    for x in range(n):
        lst.insert(x)
    lst.print()

    # Test code:

    lst.copy1()
    lst.copy2()
if __name__ == '__main__':
    main()
