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
        if self.left.isRealNode():
            return self.left
        return None

    """returns the right child

    @rtype: AVLNode
    @returns: the right child of self, None if there is no right child
    """

    def getRight(self):
        return self.right
        if self.left.isRealNode():
            return self.left
        return None

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


def rotations(lst, node):
    curr_rotate = node
    count = 0
    while curr_rotate is not None:
        BF = curr_rotate.getLeft().getHeight() - curr_rotate.getRight().getHeight()
        if BF == 2:
            LeftBF = curr_rotate.getLeft().getLeft().getHeight() - curr_rotate.getLeft().getRight().getHeight()
            if LeftBF == -1:
                lst.lr_rotate(curr_rotate)
                count += 2
            if LeftBF == 1:
                lst.r_rotatate(curr_rotate)
                count += 1
            if LeftBF == 0:
                r_singel_rotatation(lst, curr_rotate)
                count += 1
        if BF == -2:
            RightBF = curr_rotate.getRight().getLeft().getHeight() - curr_rotate.getRight().getRight().getHeight()
            if RightBF == 1:
                lst.rl_rotatate(curr_rotate)
                count += 2
            if RightBF == -1:
                lst.l_rotate(curr_rotate)
                count += 1
            if RightBF == 0:
                lst.r_singel_rotation(curr_rotate)
                count += 1
        curr_rotate = curr_rotate.getParent()
    return count


def updates(node):
    update_curr = node
    while update_curr is not None:
        update_curr.update_size()
        update_curr.update_height()
        update_curr = update_curr.getParent()


def update_first(T):
    curr = T.root
    if curr.isRealNode():
        while curr.left.isRealNode():
            curr = curr.left
        T.first_elem = curr


def update_last(T):
    curr = T.root
    if curr.isRealNode():
        while curr.right.isRealNode():
            curr = curr.right
        T.last_elem = curr


def join(T1, x, T2):
    """
    global count_join, max_join, sum_join
    curr_join = abs(T1.root.height-T2.root.height)
    sum_join += curr_join
    count_join += 1
    max_join = max(max_join, curr_join)
    """
    a = T1.root
    b = T2.root
    if T1.root.height <= T2.root.height:
        h = a.height
        if h == -1:
            update_first(T2)
            update_last(T2)
            updates(x)
            if not T2.root.isRealNode():
                T2.root = None
            T2.insert(0, x.value)
            return T2
        if b.height == h or b.height == h-1:
            x.right = b
            a.parent = x
            x.left = a
            b.parent = x
            T2.root = x
        else:
            while b.height > h:
                b = b.getLeft()
            x.setLeft(a)
            a.setParent(x)
            x.setParent(b.getParent())
            b.getParent().setLeft(x)
            x.setRight(b)
            b.setParent(x)
        # update sizes, heights:
        updates(x)
        # rotations:
        rotations(T2, x)
        return T2
    else:
        h = b.height
        if h == -1:
            update_first(T1)
            update_last(T1)
            updates(x)
            if not T1.root.isRealNode():
                T1.root = None
            T1.insert(T1.root.left.size+T1.root.right.size+1, x.value)
            return T1
        if a.height == h - 1:
            x.right = a
            a.parent = x
            x.left = b
            b.parent = x
            T1.root = x
        else:
            while a.height > h:
                a = a.getRight()
            x.setRight(b)
            b.setParent(x)
            x.setParent(a.getParent())
            a.getParent().setRight(x)
            x.setLeft(a)
            a.setParent(x)
        # update sizes, heights:
        updates(x)
        # rotations:
        rotations(T1, x)
        return T1


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

    def l_single_rotation(self, z):
        x = z.getLeft()
        if self.root is z:
            self.root = x
        x.setParent(z.getParent())
        if z.getParent() is not None:
            z.getParent().left = x
        z.setLeft(x.getRight())
        x.getRight().setParent(z)
        x.setRight(z)
        z.setParent(x)

    def r_singel_rotation(self, z):
        x = z.getRight()
        if self.root is z:
            self.root = x
        x.setParent(z.getParent())
        if z.getParent() is not None:
            z.getParent().right = x
        z.setRight(x.getLeft())
        x.getLeft().setParent(z)
        x.setLeft(z)
        z.setParent(x)

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
        B.update_height()
        A.update_size()
        A.update_height()

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
        B.update_height()
        A.update_size()
        A.update_height()

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
        C.update_height()
        A.update_size()
        A.update_height()
        B.update_size()
        B.update_height()

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
        C.update_height()
        A.update_size()
        A.update_height()
        B.update_size()
        B.update_height()

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
            print("error in insert, BF =", node.left.height - node.right.height)
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
        assert 0 <= i < self.root.size
        delete_node = self.find(i)
        if not (delete_node.left.isRealNode() and delete_node.right.isRealNode()):
            node = delete_node.parent
            if node is None:  # delete_node is the root
                # there are only 2 real nodes in tree
                if delete_node.left.isRealNode():
                    self.root = delete_node.left
                elif delete_node.right.isRealNode():
                    self.root = delete_node.right
                else:  # self has only one node
                    self.root = None
                    self.first_elem = None
                    self.last_elem = None
                    return 0
                self.root.parent = None
                self.first_elem = self.root
                self.last_elem = self.root
                return 0
            self._delete_without_fixes_or_updates_when_at_most_one_child(delete_node)
        else:  # delete_node has 2 children
            successor = self.find(i + 1)
            node = successor.parent
            if node == delete_node:
                node = successor
            self._delete_without_fixes_or_updates_when_at_most_one_child(successor)
            # replace delete_node by successor:
            delete_node_parent = delete_node.parent
            if delete_node_parent is None:  # delete_node is the root
                self.root = successor
            else:
                if delete_node_parent.left == delete_node:
                    delete_node_parent.left = successor
                else:
                    delete_node_parent.right = successor
            successor.parent = delete_node_parent
            successor.left = delete_node.left
            successor.right = delete_node.right
            successor.left.parent = successor
            successor.right.parent = successor

        # update size:
        _node = node
        while _node is not None:
            _node.update_size()
            _node = _node.parent

        # fix tree:
        rotations_counter = 0
        while node is not None:
            while node is not None and abs(node.left.height - node.right.height) < 2:
                # prev_h = node.height
                node.update_height()
                # if prev_h == node.height:
                #     self.update_heights(node)
                #     return rotations_counter
                node = node.parent
            if node is None:
                self.first_elem = self.find(0)
                self.last_elem = self.find(self.root.size - 1)
                return rotations_counter
            # now |BF(node)| = 2. rotation:
            if node.left.height > node.right.height:
                if node.left.left.height >= node.left.right.height:
                    # right rotation:
                    self.r_rotate(node)
                else:
                    # left then right rotation:
                    self.lr_rotate(node)
            else:
                if node.right.left.height <= node.right.right.height:
                    # left rotation:
                    self.l_rotate(node)
                else:
                    # right then left rotation:
                    self.rl_rotate(node)
            rotations_counter += 1

        # fix first and last:
        self.first_elem = self.find(0)
        self.last_elem = self.find(self.root.size - 1)

        return rotations_counter

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

    def _delete_without_fixes_or_updates_when_at_most_one_child(self, delete_node):
        if not delete_node.left.isRealNode():
            node = delete_node.parent
            if not delete_node.right.isRealNode():  # no children
                if node.left == delete_node:
                    node.left = AVLNode(None)
                    node.left.parent = node
                elif node.right == delete_node:
                    node.right = AVLNode(None)
                    node.left.parent = node
                else:
                    raise Exception("problem in delete({i}) <0>")
            else:  # only right child
                child = delete_node.right
                if node.left == delete_node:
                    node.left = child
                    child.parent = node
                elif node.right == delete_node:
                    node.right = child
                    child.parent = node
                else:
                    raise Exception("problem in delete({i}) <1>")

        else:  # only left child
            node = delete_node.parent
            child = delete_node.left
            if node.left == delete_node:
                node.left = child
                child.parent = node
            elif node.right == delete_node:
                node.right = child
                child.parent = node
            else:
                raise Exception("problem in delete({i}) <1>")


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
        right_left = []
        parents = []
        i += 1
        node = self.root
        small_items = 0  # number of items in list that are smaller than node (by index)
        while node.isRealNode():
            if node.left.size + small_items >= i:
                right_left.append(False)
                parents.append(node)
                node = node.left
            elif node.left.size + small_items == i - 1:  # there are exactly i-1 items smaller than node
                i_node = node
                break
            else:  # all the left children of node are smaller than node.right
                small_items += node.left.size + 1
                right_left.append(True)
                parents.append(node)
                node = node.right
        curr_elem = i_node
        right_tree = AVLTreeList()
        left_tree = AVLTreeList()
        right_tree.root = i_node.right
        left_tree.root = i_node.left
        for curr_idx in range(len(parents)-1, -1, -1):
            if right_left[curr_idx]:
                new_tree = AVLTreeList()
                new_tree.root = parents[curr_idx].left
                new_tree.root.parent = None
                left_tree = join(new_tree, parents[curr_idx], left_tree)
            else:
                new_tree = AVLTreeList()
                new_tree.root = parents[curr_idx].right
                new_tree.root.parent = None
                right_tree = join(right_tree, parents[curr_idx], new_tree)
        """
            while test_elem is not None:
            curr_cost = abs(test_elem.left.height - test_elem.right.height)
            sum_join += curr_cost
            count_join += 1
            max_join = max(max_join, curr_cost)
            test_elem = test_elem.parent
        print("avarage join: "+str(sum_join/count_join))
        print("max join: " + str(max_join))
        """
        return left_tree, curr_elem.value, right_tree

    """concatenates lst to self

    @type lst: AVLTreeList
    @param lst: a list to be concatenated after self
    @rtype: int
    @returns: the absolute value of the difference between the height of the AVL trees joined
    """

    def concat(self, lst):
        height_diff = self.getRoot().getHeight() - lst.getRoot().getHeight()
        conect_elem = self.last_elem
        self.delete(self.root.size-1)
        self = join(self, conect_elem, lst)
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
        return -1

    """returns the root of the tree representing the list

    @rtype: AVLNode
    @returns: the root, None if the list is empty
    """

    def getRoot(self):
        return self.root


"""
Q2: split
T = AVLTreeList()
max_join, count_join, sum_join = 0, 0, 0
x = 10
n = 1000*(2**x)
a = random.sample(list(range(n)), n)
for i in range(n):
    T.insert(i, a[i])
T.split(random.randint(1, n))
print("avarage "+str(sum_join/count_join))
print("max "+str(max_join))
max_join, count_join, sum_join = 0, 0, 0
T = AVLTreeList()
for i in range(n):
    T.insert(i, a[i])
index2_item = T.root.left
small = 0
while index2_item.right is not None:
    small += index2_item.left.size+1
    index2_item = index2_item.right
T.split(small+1)
print("avarage "+str(sum_join/count_join))
print("max "+str(max_join))
print(small+1)
"""
"""
T1 = AVLTreeList()
for i in range(10):
    T1.insert(i, i)
T2 = AVLTreeList()
for i in range(5):
    T2.insert(i, i+10)
print(T1.listToArray())
print(T2.listToArray())
T1.concat(T2)
print(T1.listToArray())
"""
