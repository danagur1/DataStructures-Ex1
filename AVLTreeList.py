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
        h = self.height
        self.height = max(self.left.height, self.right.height) + 1
        return 1 if h != self.height else 0

    def isRealNode(self):
        return self.height != -1




"""
A class implementing the ADT list, using an AVL tree.
"""


class AVLTreeList(object):

    def __init__(self):
        self.root = None
        self.last_elem = None  # pointer to the last element in the list
        self.first_elem = None  # pointer to the first element in the list

    def l_single_rotation(self, z):
        x = z.left
        if self.root is z:
            self.root = x
        x.setParent(z.getParent())
        if z.getParent() is not None:
            z.getParent().left = x
        z.setLeft(x.right)
        x.right.setParent(z)
        x.setRight(z)
        z.setParent(x)

    def r_singel_rotation(self, z):
        x = z.right
        if self.root is z:
            self.root = x
        x.setParent(z.getParent())
        if z.getParent() is not None:
            z.getParent().right = x
        z.setRight(x.left)
        x.left.setParent(z)
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

    @staticmethod
    def rotations(lst, node):
        curr_rotate = node
        count = 0
        while curr_rotate is not None:
            BF = curr_rotate.left.getHeight() - curr_rotate.right.getHeight()
            if BF == 2:
                LeftBF = curr_rotate.left.left.getHeight() - curr_rotate.left.right.getHeight()
                if LeftBF == -1:
                    lst.lr_rotate(curr_rotate)
                    count += 2
                if LeftBF == 1:
                    lst.r_rotation(curr_rotate)
                    count += 1
                if LeftBF == 0:
                    lst.l_single_rotation(curr_rotate)
                    count += 1
            if BF == -2:
                RightBF = curr_rotate.right.left.getHeight() - curr_rotate.right.right.getHeight()
                if RightBF == 1:
                    lst.rl_rotate(curr_rotate)
                    count += 2
                if RightBF == -1:
                    lst.l_rotation(curr_rotate)
                    count += 1
                if RightBF == 0:
                    lst.r_singel_rotation(curr_rotate)
                    count += 1
            curr_rotate = curr_rotate.getParent()
        return count

    @staticmethod
    def join(T1, x, T2):
        a = T1.root
        b = T2.root
        if T1.root.height <= T2.root.height:
            h = a.height
            if h == -1:
                AVLTreeList.update_first(T2)
                AVLTreeList.update_last(T2)
                AVLTreeList.updates(x)
                if not T2.root.isRealNode():
                    T2.root = None
                T2.insert(0, x.value)
                return T2
            if b.height == h or b.height == h - 1:
                x.right = b
                a.parent = x
                x.left = a
                b.parent = x
                T2.root = x
            else:
                while b.height > h:
                    b = b.left
                x.setLeft(a)
                a.setParent(x)
                x.setParent(b.getParent())
                b.getParent().setLeft(x)
                x.setRight(b)
                b.setParent(x)
            # update sizes, heights:
            AVLTreeList.updates(x)
            # rotations:
            AVLTreeList.rotations(T2, x)
            return T2
        else:
            h = b.height
            if h == -1:
                AVLTreeList.update_first(T1)
                AVLTreeList.update_last(T1)
                AVLTreeList.updates(x)
                if not T1.root.isRealNode():
                    T1.root = None
                T1.insert(T1.root.left.size + T1.root.right.size + 1, x.value)
                return T1
            if a.height == h - 1:
                x.right = a
                a.parent = x
                x.left = b
                b.parent = x
                T1.root = x
            else:
                while a.height > h:
                    a = a.right
                x.setRight(b)
                b.setParent(x)
                x.setParent(a.getParent())
                a.getParent().setRight(x)
                x.setLeft(a)
                a.setParent(x)
            # update sizes, heights:
            AVLTreeList.updates(x)
            # rotations:
            AVLTreeList.rotations(T1, x)
            return T1

    """
    listToArrayRec- used in listToArray
    complexity: O(n)
    """
    return_list_idx = 0

    @staticmethod
    def listToArrayRec(return_list, curr_elem):
        global return_list_idx
        if curr_elem.value is not None:
            AVLTreeList.listToArrayRec(return_list, curr_elem.left)
            return_list[return_list_idx] = curr_elem.value
            return_list_idx += 1
            AVLTreeList.listToArrayRec(return_list, curr_elem.right)

    @staticmethod
    def updates(node):
        update_curr = node
        while update_curr is not None:
            update_curr.update_size()
            update_curr.update_height()
            update_curr = update_curr.getParent()

    @staticmethod
    def update_first(T):
        curr = T.root
        if curr.isRealNode():
            while curr.left.isRealNode():
                curr = curr.left
            T.first_elem = curr

    @staticmethod
    def update_last(T):
        curr = T.root
        if curr.isRealNode():
            while curr.right.isRealNode():
                curr = curr.right
            T.last_elem = curr


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
        result = 0
        while node is not None and abs(node.left.height - node.right.height) < 2:
            prev_h = node.height
            result += node.update_height()
            if prev_h == node.height:
                # self.update_heights(node)
                return result
            node = node.parent
        if node is None:
            return result
        # now |BF(node)| = 2. rotation:
        if node.left.height > node.right.height:
            if node.left.left.height > node.left.right.height:
                # right rotation:
                self.r_rotate(node)
                result += 1
            else:
                # left then right rotation:
                self.lr_rotate(node)
                result += 2
        else:
            if node.right.left.height < node.right.right.height:
                # left rotation:
                self.l_rotate(node)
                result += 1
            else:
                # right then left rotation:
                self.rl_rotate(node)
                result += 2

        self.update_heights(new_node)
        node = new_node.parent
        while node is not None:
            node.update_size()
            node = node.parent
        return result

    def _delete_without_fixes_or_updates_when_at_most_one_child(self, delete_node):
        if not delete_node.left.isRealNode():
            node = delete_node.parent
            if not delete_node.right.isRealNode():  # no children
                if node.left == delete_node:
                    node.left = AVLNode(None)
                    node.left.parent = node
                else:
                    node.right = AVLNode(None)
                    node.left.parent = node

            else:  # only right child
                child = delete_node.right
                if node.left == delete_node:
                    node.left = child
                    child.parent = node
                else:
                    node.right = child
                    child.parent = node

        else:  # only left child
            node = delete_node.parent
            child = delete_node.left
            if node.left == delete_node:
                node.left = child
                child.parent = node
            else:
                node.right = child
                child.parent = node


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
            successor = self.find(i+1)
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
        result = 0
        while node is not None:
            while node is not None and abs(node.left.height - node.right.height) < 2:
                result += node.update_height()
                node = node.parent
            if node is None:
                self.first_elem = self.find(0)
                self.last_elem = self.find(self.root.size - 1)
                return result
            # now |BF(node)| = 2. rotation:
            if node.left.height > node.right.height:
                if node.left.left.height >= node.left.right.height:
                    # right rotation:
                    self.r_rotate(node)
                    result += 1
                else:
                    # left then right rotation:
                    self.lr_rotate(node)
                    result += 2
            else:
                if node.right.left.height <= node.right.right.height:
                    # left rotation:
                    self.l_rotate(node)
                    result += 1
                else:
                    # right then left rotation:
                    self.rl_rotate(node)
                    result += 2

        # fix first and last:
        self.first_elem = self.find(0)
        self.last_elem = self.find(self.root.size - 1)

        return result

    """returns the value of the first item in the list
    @rtype: str
    @returns: the value of the first item, None if the list is empty
    """

    def first(self):
        return self.first_elem.value

    """returns the value of the last item in the list
    @rtype: str
    @returns: the value of the last item, None if the list is empty
    """

    def last(self):
        return self.last_elem.value

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
        AVLTreeList.listToArrayRec(return_list, curr_elem)
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
                left_tree = AVLTreeList.join(new_tree, parents[curr_idx], left_tree)
            else:
                new_tree = AVLTreeList()
                new_tree.root = parents[curr_idx].right
                new_tree.root.parent = None
                right_tree = AVLTreeList.join(right_tree, parents[curr_idx], new_tree)
        left_tree.update_first(left_tree)
        left_tree.update_last(left_tree)
        right_tree.update_first(right_tree)
        right_tree.update_last(right_tree)
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
        self.delete(self.root.size - 1)
        self = AVLTreeList.join(self, conect_elem, lst)
        return abs(height_diff)

    """
    @type val: str
    @param val: a value to be searched
    @rtype: int
    @returns: the first index that contains val, -1 if not found.
    """

    def search_rec(self, node, val):
        if node.left is not None and self.search_rec(node.left, val) != -1:
            return self.search_rec(node.left, val)
        if node.value == val:
            return node.left.size
        if node.right is not None and self.search_rec(node.right, val) != -1:
            return self.search_rec(node.right, val)+node.left.size+1
        return -1

    def search(self, val):
        return self.search_rec(self.root, val)

    """returns the root of the tree representing the list
    @rtype: AVLNode
    @returns: the root, None if the list is empty
    """

    def getRoot(self):
        return self.root


if __name__ == '__main__':
    # for i in range(1, 11):
    #     print(test3(1000 * i))
    # insert_test2(1000)
    # insert_delete_test()
    # for i in range(1, 11):
    #     print(test3(1000 * i))
    # arr = good_list(14)
    # for i in range(1, 11):
    #     print(test3(1000 * i)/(1000 * i))

#     tree = AVLTreeList()
#     for i in range(8):
#         tree.insert(random.randint(0, tree.length()), i//2)
#     print(tree.listToArray())
#     tmp = tree.split(4)
#     print(tmp[0].listToArray(), tmp[1], tmp[2].listToArray())
#     tree2 = tmp[0].concat(tmp[2])
#     print("___")
#     print(tree2.listToArray())
