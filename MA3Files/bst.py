""" bst.py

Student: Hugo Vennergrund BLom
Mail: hugo.vennergrund-blom.9969@student.uu.se
Reviewed by: 
Date reviewed: 
"""


from linked_list import LinkedList


class BST:

    class Node:
        def __init__(self, key, left=None, right=None):
            self.key = key
            self.left = left
            self.right = right

        def __iter__(self):     # Discussed in the text on generators
            if self.left:
                yield from self.left
            yield self.key
            if self.right:
                yield from self.right

    def __init__(self, root=None):
        self.root = root

    def __iter__(self):         # Dicussed in the text on generators
        if self.root:
            yield from self.root

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, r, key):
        if r is None:
            return self.Node(key)
        elif key < r.key:
            r.left = self._insert(r.left, key)
        elif key > r.key:
            r.right = self._insert(r.right, key)
        else:
            pass  # Already there
        return r

    def print(self):
        self._print(self.root)

    def _print(self, r):
        if r:
            self._print(r.left)
            print(r.key, end=' ')
            self._print(r.right)

    def contains(self, k): #
        n = self.root
        while n and n.key != k:
            if k < n.key:
                n = n.left
            else:
                n = n.right
        return n is not None

    def size(self):
        return self._size(self.root)

    def _size(self, r):
        if r is None:
            return 0
        else:
            return 1 + self._size(r.left) + self._size(r.right)

#
#   Methods to be completed
#

    def height(self):
        
        def _height(n):
            if not n:
                return 0
            
            h_r = _height(n.right)
            h_l = _height(n.left)

            if h_r > h_l:
                return 1 + h_r
            else:
                return 1 + h_l
        
        return _height(self.root)


    def remove(self, key): #
        if not self.contains(key):
            return None
            
        self.root = self._remove(self.root, key)

    def _remove(self, r, k):                      #
        if r is None:
            return None
        elif k < r.key:
            # r.left = left subtree with k removed
            r.left = self._remove(r.left, k)
        elif k > r.key:
            # r.right = right subtree with k removed
            r.right = self._remove(r.right, k)
        else:  # This is the key to be removed
            if r.left is None:     # Easy case
                return r.right
            elif r.right is None:  # Also easy case
                return r.left
            else:  # This is the tricky case.
                # Find the smallest key in the right subtree
                # Put that key in this node
                # Remove that key from the right subtree
                n = r.right
                prev_n = r

                while n.left is not None:
                    prev_n = n
                    n = n.left

                r.key = n.key

                if prev_n.left == n:
                    prev_n.left = None
                else:
                    prev_n.right = None

        return r  # Remember this! It applies to some of the cases above

    def __str__(self):
        ret_str = ''

        for n in self:
            ret_str += f'{n}, '
        
        return f'<{ret_str[:-2]}>'

    def to_list(self): #complexity: O(n)
        return [*self]

    def to_LinkedList(self): #complexity: O(n)
        linked_lst = LinkedList()
        for i in reversed(self.to_list()):
            linked_lst.insert(i)
        return linked_lst

def random_tree(n):                               # Useful
    pass


def main():
    t = BST()
    for x in [4, 1, 3, 6, 7, 1, 1, 5, 8]:
        t.insert(x)
    #t.print()
    print(t)

    #print('size  : ', t.size())
    #for k in [0, 1, 2, 5, 9]:
    #    print(f"contains({k}): {t.contains(k)}")

    t.remove(6)
    print(t)

if __name__ == "__main__":
    main()


"""
What is the generator good for?
==============================

1. computing size?
yes
2. computing height?
no
3. contains?
yes
4. insert?
no
5. remove?
no

"""
