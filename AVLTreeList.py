# username - danagur1
# id1      - 328301072
# name1    - Dana Gur
# id2      - 327703831
# name2    - Ofer Bogoslavsky
import random

"""A class represnting a node in an AVL tree"""


class AVLNode(object):
    """Constructor, you are allowed to add more fields.

    @type value: str
    @param value: data of your node
    """

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = -1
        self.size = 0

    """returns the left child
    @rtype: AVLNode
    @returns: the left child of self, None if there is no left child
    """

    def getLeft(self):
        return self.left

    """returns the right child

    @rtype: AVLNode
    @returns: the right child of self, None if there is no right child
    """

    def getRight(self):
        return self.right

    """returns the parent 

    @rtype: AVLNode
    @returns: the parent of self, None if there is no parent
    """

    def getParent(self):
        return self.parent

    """return the value

    @rtype: str
    @returns: the value of self, None if the node is virtual
    """

    def getValue(self):
        return self.value

    """returns the height

    @rtype: int
    @returns: the height of self, -1 if the node is virtual
    """

    def getHeight(self):
        return self.height

    """returns the size

    @rtype: int
    @returns: the size of self
    """

    def getSize(self):
        return self.size

    """sets left child

    @type node: AVLNode
    @param node: a node
    """

    def setLeft(self, node):
        self.left = node

    """sets right child

    @type node: AVLNode
    @param node: a node
    """

    def setRight(self, node):
        self.right = node

    """sets parent

    @type node: AVLNode
    @param node: a node
    """

    def setParent(self, node):
        self.parent = node

    """sets value

    @type value: str
    @param value: data
    """

    def setValue(self, value):
        self.value = value

    """sets the balance factor of the node

    @type h: int
    @param h: the height
    """

    def setHeight(self, h):
        self.height = h

    """sets the size of the node

    @type s: int
    @param s: the size
    """

    def setSize(self, s):
        self.size = s

    """returns whether self is not a virtual node 

    @rtype: bool
    @returns: False if self is a virtual node, True otherwise.
    """

    def update_size(self):
        self.size = self.left.size + self.right.size + 1

    def update_height(self):
        self.height = max(self.left.height, self.right.height) + 1

    def isRealNode(self):
        return self.height != -1


return_list_idx = 0


def listToArrayRec(return_list, curr_elem):
    global return_list_idx
    if curr_elem.value is not None:
        listToArrayRec(return_list, curr_elem.left)
        return_list[return_list_idx] = curr_elem.value
        return_list_idx += 1
        listToArrayRec(return_list, curr_elem.right)


def single_rotation_l(lst, z):
    if lst.root is z:
        lst.root = x
    x = z.getLeft()
    x.setParent(z.getParent())
    x.setRight(z)
    z.setParent(x)
    z.setLeft(x.getRight())
    x.getRight().setParent(z)


def single_rotation_r(lst, z):
    if lst.root is z:
        lst.root = x
    x = z.getright()
    x.setParent(z.getParent())
    x.setLeft(z)
    z.setParent(x)
    z.setRight(x.getLeft())
    x.getLeft().setParent(z)


def rotations(lst, node):
    curr_rotate = node
    count = 0
    while curr_rotate is not None:
        BF = curr_rotate.getLeft().getSize() - curr_rotate.getRight().getSize()
        curr_rotate = curr_rotate.getParent()
        if BF == 2:
            LeftBF = curr_rotate.getLeft().getLeft().getSize() - curr_rotate.getLeft().getRight().getSize()
            if LeftBF == -1:
                lst.lr_rotation(curr_rotate)
                count += 2
            if LeftBF == 1:
                lst.r_rotation(curr_rotate)
                count += 1
            if LeftBF == 0:
                r_singel_rotation(lst, curr_rotate)
                count += 1
        if BF == -2:
            RightBF = curr_rotate.getLeft().getLeft().getSize() - curr_rotate.getLeft().getRight().getSize()
            if RightBF == 1:
                lst.rl_rotation(curr_rotate)
                count += 2
            if RightBF == -1:
                lst.l_rotate(curr_rotate)
                count += 1
            if LeftBF == 0:
                r_singel_rotation(lst, curr_rotate)
                count += 1
    return count


def updates(node):
    update_curr = node
    while update_curr is not None:
        update_curr.update_size()
        update_curr.update_height()
        update_curr = update_curr.getParent()


def join(T1, x, T2):
    if T1.height > T2.height:
        T1, T2 = T2, T1
    h = T1.height
    while T2.height != h and T2.height != h-1:
        T2 = T2.getLeft()
    x.setLeft(T1)
    T1.setParent(x)
    x.setRight(T2)
    T2.setParent(x)
    x.setParent(T2.getParent())
    T2.getParent().setLeft(x.getParent())
    # update sizes, heights:
    updates(x)
    # rotations:
    rotations(T2, x)
    return T2


"""
A class implementing the ADT list, using an AVL tree.
"""


class AVLTreeList(object):
    """
    Constructor, you are allowed to add more fields.

    """

    def __init__(self):
        self.root = None
        self.last_elem = None  # pointer to the last element in the list
        self.first_elem = None  # pointer to the first element in the list

    def l_rotate(self, node):
        B = node
        A = node.right
        Al = A.left
        B_parent = B.parent
        if B_parent is None:
            self.root = A
            A.parent = None
        else:
            A.parent = B_parent
            if B == B_parent.left:
                B_parent.left = A
            else:
                B_parent.right = A
        B.parent = A
        A.left = B
        B.right = Al
        Al.parent = B

        B.update_size()
        A.update_size()

    def r_rotate(self, node):
        B = node
        A = node.left
        Ar = A.right
        B_parent = B.parent
        if B_parent is None:
            self.root = A
            A.parent = None
        else:
            A.parent = B_parent
            if B == B_parent.left:
                B_parent.left = A
            else:
                B_parent.right = A
        B.parent = A
        A.right = B
        B.left = Ar
        Ar.parent = B

        B.update_size()
        A.update_size()

    def lr_rotate(self, node):
        C = node
        A = C.left
        B = A.right
        Bl = B.left
        Br = B.right
        C_parent = C.parent
        if C_parent is None:
            self.root = B
            B.parent = None
        else:
            B.parent = C_parent
            if C == C_parent.left:
                C_parent.left = B
            else:
                C_parent.right = B
        B.left = A
        B.right = C
        A.parent = B
        C.parent = B
        A.right = Bl
        C.left = Br
        Bl.parent = A
        Br.parent = C

        C.update_size()
        A.update_size()
        B.update_size()

    def rl_rotate(self, node):
        C = node
        A = C.right
        B = A.left
        Bl = B.left
        Br = B.right
        C_parent = C.parent
        if C_parent is None:
            self.root = B
            B.parent = None
        else:
            B.parent = C_parent
            if C == C_parent.left:
                C_parent.left = B
            else:
                C_parent.right = B
        B.right = A
        B.left = C
        A.parent = B
        C.parent = B
        C.right = Bl
        A.left = Br
        Bl.parent = C
        Br.parent = A

        C.update_size()
        A.update_size()
        B.update_size()

    """returns whether the list is empty

    @rtype: bool
    @returns: True if the list is empty, False otherwise
    """

    def empty(self):
        return self.root is None

    def find(self, i):  # returns the i'th node (0 <= i < n)
        assert 0 <= i < self.root.size
        i += 1
        node = self.root
        small_items = 0  # number of items in list that are smaller than node (by index)
        while node.isRealNode():
            if node.left.size + small_items >= i:
                node = node.left
            elif node.left.size + small_items == i - 1:  # there are exactly i-1 items smaller than node
                return node
            else:  # all the left children of node are smaller than node.right
                small_items += node.left.size + 1
                node = node.right
        raise Exception(f"problem in find({i})")  # we shouldn't get here

    """"retrieves the value of the i'th item in the list

        @type i: int
        @pre: 0 <= i < self.length()
        @param i: index in the list
        @rtype: str
        @returns: the the value of the i'th item in the list
        """

    def retrieve(self, i):
        return self.find(i).value

    """inserts val at position i in the list

    @type i: int
    @pre: 0 <= i <= self.length()
    @param i: The intended index in the list to which we insert val
    @type val: str
    @param val: the value we inserts
    @rtype: list
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    def update_heights(self, node):
        while node is not None:
            node.update_height()
            node = node.parent

    """inserts val at position i in the list

    @type i: int
    @pre: 0 <= i <= self.length()
    @param i: The intended index in the list to which we insert val
    @type val: str
    @param val: the value we inserts
    @rtype: list
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    def insert(self, i, val):
        assert 0 <= i <= self.length()
        new_node = AVLNode(val)
        new_node.height = 0
        new_node.size = 1
        new_node.left = AVLNode(None)
        new_node.right = AVLNode(None)
        new_node.left.parent = new_node
        new_node.right.parent = new_node
        if self.empty():
            self.root = new_node
            self.first_elem = new_node
            self.last_elem = new_node
            return 0
        if i == 0:
            new_node.parent = self.first_elem
            self.first_elem.left = new_node
            self.first_elem = new_node
        elif i == self.root.size:
            new_node.parent = self.last_elem
            self.last_elem.right = new_node
            self.last_elem = new_node
        else:
            node = self.find(i)
            if not node.left.isRealNode():
                node.left = new_node
                new_node.parent = node
            else:
                node = self.find(i - 1)
                node.right = new_node
                new_node.parent = node

        # update size:
        node = new_node.parent
        while node is not None:
            node.update_size()
            node = node.parent

        # fix tree:
        node = new_node.parent

        while node is not None and abs(node.left.height - node.right.height) < 2:
            prev_h = node.height
            node.update_height()
            if prev_h == node.height:
                self.update_heights(node)
                return 0
            node = node.parent
        if node is None:
            return 0
        # now |BF(node)| = 2. rotation:
        if abs(node.left.height - node.right.height) != 2:
            print(node.left.height - node.right.height)
        if node.left.height > node.right.height:
            if node.left.left.height > node.left.right.height:
                # right rotation:
                self.r_rotate(node)
            else:
                # left then right rotation:
                self.lr_rotate(node)
        else:
            if node.right.left.height < node.right.right.height:
                # left rotation:
                self.l_rotate(node)
            else:
                # right then left rotation:
                self.rl_rotate(node)

        self.update_heights(new_node)
        node = new_node.parent
        while node is not None:
            node.update_size()
            node = node.parent
        return 1

    """deletes the i'th item in the list

    @type i: int
    @pre: 0 <= i < self.length()
    @param i: The intended index in the list to be deleted
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    def delete(self, i):
        i_node = find(i)
        if i_node.getParent().getLeft() is i_node:
            i_node.getParent().setLeft(AVLNode(None))
        else:
            i_node.getParent().setRight(AVLNode(None))
        return rotations(self, i_node.getParent())

    """returns the value of the first item in the list

    @rtype: str
    @returns: the value of the first item, None if the list is empty
    """

    def first(self):
        return self.first_elem

    """returns the value of the last item in the list

    @rtype: str
    @returns: the value of the last item, None if the list is empty
    """

    def last(self):
        return self.last_node

    """returns an array representing list 

    @rtype: list
    @returns: a list of strings representing the data structure
    """

    def listToArray(self):
        global return_list_idx
        if self.root is None:
            return []
        return_list = [None] * self.root.size
        return_list_idx = 0
        curr_elem = self.root
        listToArrayRec(return_list, curr_elem)
        return return_list

    """returns the size of the list 

    @rtype: int
    @returns: the size of the list
    """

    def length(self):
        if self.root is None:
            return 0
        return self.root.size

    """splits the list at the i'th index

    @type i: int
    @pre: 0 <= i < self.length()
    @param i: The intended index in the list according to whom we split
    @rtype: list
    @returns: a list [left, val, right], where left is an AVLTreeList representing the list until index i-1,
    right is an AVLTreeList representing the list from index i+1, and val is the value at the i'th index.
    """

    def split(self, i):
        last_right, last_left = True, True
        i_node = self.find(i)
        curr_elem = i_node
        last_left = i_node.left
        last_right = i_node.right
        while curr_elem is not None:
            if curr_elem.parent.right is curr_elem:
                last_left = join(curr_elem.parent.left, curr_elem.parent, last_left)
            else:
                last_right = join(curr_elem.parent.right, curr_elem.parent, last_right)
            curr_elem = curr_elem.parent()
        right_tree = AVLTreeList()
        left_tree = AVLTreeList()
        right_tree.root = last_right
        right_tree.root = last_left
        while test_elem is not None:
            curr_cost = abs(test_elem.left.height - test_elem.right.height)
            sum_join += curr_cost
            count_join += 1
            max_join = max(max_join, curr_cost)
            test_elem = test_elem.parent
        print("avarage join: "+str(sum_join/count_join))
        print("max join: " + str(max_join))
        return left_tree, curr_elem.value, right_tree

    """concatenates lst to self

    @type lst: AVLTreeList
    @param lst: a list to be concatenated after self
    @rtype: int
    @returns: the absolute value of the difference between the height of the AVL trees joined
    """

    def concat(self, lst):
        height_diff = self.getRoot().getHeight() - lst.getRoot().getHeight()
        conect_elem = self.last()
        lst.delete(self.root.size-1)
        new_tree = AVLTreeList
        new_tree.root = join(self.root, conect_elem, lst.root)
        return new_tree

        # update sizes:
        while v is not None:
            v = v.getRight().getSize() + v.getLeft().getSize() + 1
            v = v.parent
        # update heights:
        while v is not None:
            v = v.getRight().getHeight() + v.getLeft().getHeight() + 1
            v = v.parent
        return abs(height_diff)

    """searches for a *value* in the list

    @type val: str
    @param val: a value to be searched
    @rtype: int
    @returns: the first index that contains val, -1 if not found.
    """

    def search(self, val):
        if self.getRoot().getSize() == 1:
            return self.getRoot().getVal() == val
        left_search = self.search((self.getRoot().getLeft()), val)
        if left_search != -1:
            return left_search
        if self.getRoot().getVal() == val:
            return val
        right_search = self.search((self.getRoot().getRight()), val)
        if right_search != -1:
            return right_search

    """returns the root of the tree representing the list

    @rtype: AVLNode
    @returns: the root, None if the list is empty
    """

    def getRoot(self):
        return self.root


"""
T = AVLTreeList()
x = 1
a = random.sample(range(1000*(2**x)+1), 1000*(2**x)+1)
for i in range(1000*(2**x)):
    T.insert(i, a[i])
T.split(random.randint(1, 1000*(2**x)+1))
T = AVLTreeList()
for i in range(1000*(2**x)):
    T.insert(i, a[i])
index2_item = T.root.left
small = 0
while index2_item.right is not None:
    small = index2_item.left.size+1
    index2_item = index2_item.right
T.split(small+1)
print(small+1)*/
"""

T = AVLTreeList()
for i in range(6):
    T.insert(i, i)
T.split(5)