# username - danagur1
# id1      - 328301072
# name1    - Dana Gur
# id2      - 327703831
# name2    - Ofer Bogoslavsky


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


    """sets left child

    @type node: AVLNode
    @param node: a node
    """

    def setLeft(self, node):
        self.left = node
        return None

    """sets right child

    @type node: AVLNode
    @param node: a node
    """

    def setRight(self, node):
        self.right = node
        return None

    """sets parent

    @type node: AVLNode
    @param node: a node
    """

    def setParent(self, node):
        self.parent = node
        return None

    """sets value

    @type value: str
    @param value: data
    """

    def setValue(self, value):
        self.value = value
        return None

    """sets the balance factor of the node

    @type h: int
    @param h: the height
    """

    def setHeight(self, h):
        self.height = h
        return None

    """returns whether self is not a virtual node 

    @rtype: bool
    @returns: False if self is a virtual node, True otherwise.
    """

    def isRealNode(self):
        return self.height != -1


def listToArrayRec(return_list, return_list_idx, curr_elem):
	if curr_elem is not None:
		listToArrayRec(curr_elem.left)
		return_list[return_list_idx] = curr_elem
		listToArrayRec(curr_elem.right)


"""
A class implementing the ADT list, using an AVL tree.
"""


class AVLTreeList(object):

	"""
	Constructor, you are allowed to add more fields.

	"""
	def __init__(self):
		self.root = None
		self.last_elem = None # pointer to the last element in the list
		self.first_elem = None # pointer to the first element in the list

	"""returns whether the list is empty

	@rtype: bool
	@returns: True if the list is empty, False otherwise
	"""
	def empty(self):
        	return self.root is None

	


	def find(self, i):  # returns the i'th node
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
		
    	"""retrieves the value of the i'th item in the list

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
	def insert(self, i, val):
        new_node = AVLNode(val)
        new_node.height = 0
        new_node.size = 1
        new_node.left = AVLNode(val)
        new_node.right = AVLNode(val)
        if i == 0:
            new_node.parent = self.first_elem
            self.first_elem.left = new_node
            self.first_elem = new_node
        elif i == self.root.size - 1:
            new_node.parent = self.last_elem
            self.last_elem.right = new_node
            self.last_elem = new_node
        else:
            node = self.find(i)
            if not node.left.isRealNode:
                node.left = new_node
                new_node.parent = node
            else:
                node = self.find(i-1)
                node.right = new_node
                new_node.parent = node

        # set size:
        node = new_node.parent
        while node is not None:
            node.size = node.left.size + node.right.size

        # fix_the_tree:
        node = new_node.parent

        while node is not None and abs(node.left.height - node.right.height) < 2:
            prev_h = node.height
            node.height = node.left.height + node.right.height
            if prev_h == node.height:
                return 0
            node = node.parent
        # now |BF(node)| = 2. rotation:
        print("+-2 = ", node.left.height - node.right.height, " ?")
        if node.left.height > node.right.height:
            if node.left.left.height > node.left.right.height:
                # right rotation:
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
            else:
                # left then right rotation:
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

        else:
            if node.right.left.height < node.right.right.height:
                # left rotation:
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
            else:
                # right then left rotation:
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
                Bl.parent = A
                Br.parent = C
        return 1


	"""deletes the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list to be deleted
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def delete(self, i):
		return -1


	"""returns the value of the first item in the list

	@rtype: str
	@returns: the value of the first item, None if the list is empty
	"""
	def first(self):
		return self.first_node

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
		return_list = [None]*self.root.size
		return_list_idx = 0
		curr_elem = self.root
		listToArrayRec(return_list, return_list_idx, curr_elem)
		return return_list


	"""returns the size of the list 

	@rtype: int
	@returns: the size of the list
	"""
	def length(self):
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
		left_tree = AVLTreeList()
		first_left = True
		right_tree = AVLTreeList()
		first_right = True
		curr_elem = self.root
		curr_idx = curr_elem.left.size + 1
		while curr_idx != i:
			if i < curr_idx:
				if first_left:
					left_tree.root = curr_elem
					curr_elem.parent = None
					first_left = False
				else:
					left_tree_curr.left = curr_elem
					curr_elem.parent = left_tree_curr
				left_tree_curr = curr_elem
				curr_elem = curr_elem.left
			if i > curr_idx:
				if first_right:
					right_tree.root = curr_elem
					curr_elem.parent = None
					first_right = False
				else:
					right_tree_curr.right = curr_elem
					curr_elem.parent = right_tree_curr
				right_tree_curr = curr_elem
				curr_elem = curr_elem.right
		left_tree_curr.left = curr_elem.left
		curr_elem.left.parent = left_tree_curr
		right_tree_curr.right = curr_elem.right
		curr_elem.right.parent = right_tree_curr
		# update sizes in right tree:
		while right_tree_curr is not None:
			right_tree_curr = right_tree_curr.right+right_tree_curr.left+1
			right_tree_curr = right_tree_curr.parent
		# update sizes in left tree:
		while left_tree_curr is not None:
			left_tree_curr = left_tree_curr.right + left_tree_curr.left + 1
			left_tree_curr = left_tree_curr.parent
		return left_tree_curr, curr_elem.val, right_tree_curr

	"""concatenates lst to self

	@type lst: AVLTreeList
	@param lst: a list to be concatenated after self
	@rtype: int
	@returns: the absolute value of the difference between the height of the AVL trees joined
	"""
	def concat(self, lst):
		return None

	"""searches for a *value* in the list

	@type val: str
	@param val: a value to be searched
	@rtype: int
	@returns: the first index that contains val, -1 if not found.
	"""
	def search(self, val):
		return None



	"""returns the root of the tree representing the list

	@rtype: AVLNode
	@returns: the root, None if the list is empty
	"""
	def getRoot(self):
		return self.root


