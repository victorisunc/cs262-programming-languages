# This is an insert procedure that takes a tree and an element
# and returns a new tree with that element inserted correctly

def insert(tree, element):
    if tree == None:
        return (None, element, None)
    else:
        left_child = tree[0]
        this_element = tree[1]
        right_child = tree[2]
        if element <= this_element:
            new_left_child = insert(left_child, element)
            return (new_left_child, this_element, right_child)
        else:
            # element >= this_element
            new_right_child = insert(right_child, element)
            return (left_child, this_element, new_right_child)

my_tree = (None, 'midpoint', None)
print insert(my_tree, 'zuma,jacob')
#       midpoint
#          / \
#      None  zuma,jacob

def print_tree(tree):
    '''
    This prints out the tree in ascending order
    '''
    if tree == None:
        return
    else:
        left_child = tree[0]
        this_element = tree[1]
        right_child = tree[2]
        print_tree(left_child)
        print this_element
        print_tree(right_child)

t1 = (None, 'midpoint', None)
t2 = insert(t1, 'zuma,jacob')
t3 = insert(t2, 'atwood,margaret')

print_tree(t3)
