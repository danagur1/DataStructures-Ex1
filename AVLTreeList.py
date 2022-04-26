# username - danagur1
# id1      - 328301072
# name1    - Dana Gur
# id2      - complete info
# name2    - complete info


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
		return None

	"""returns the right child

	@rtype: AVLNode
	@returns: the right child of self, None if there is no right child
	"""
	def getRight(self):
		return None

	"""returns the parent 

	@rtype: AVLNode
	@returns: the parent of self, None if there is no parent
	"""
	def getParent(self):
		return None

	"""return the value

	@rtype: str
	@returns: the value of self, None if the node is virtual
	"""
	def getValue(self):
		return None

	"""returns the height

	@rtype: int
	@returns: the height of self, -1 if the node is virtual
	"""
	def getHeight(self):
		return -1

	"""sets left child

	@type node: AVLNode
	@param node: a node
	"""
	def setLeft(self, node):
		return None

	"""sets right child

	@type node: AVLNode
	@param node: a node
	"""
	def setRight(self, node):
		return None

	"""sets parent

	@type node: AVLNode
	@param node: a node
	"""
	def setParent(self, node):
		return None

	"""sets value

	@type value: str
	@param value: data
	"""
	def setValue(self, value):
		return None

	"""sets the balance factor of the node

	@type h: int
	@param h: the height
	"""
	def setHeight(self, h):
		return None

	"""returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""
	def isRealNode(self):
		return False


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
		return None

	"""retrieves the value of the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: index in the list
	@rtype: str
	@returns: the the value of the i'th item in the list
	"""
	def retrieve(self, i):
		return None

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
		return -1


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
		return None


