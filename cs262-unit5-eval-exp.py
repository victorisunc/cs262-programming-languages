# Quiz: Eval Exp

# Write an eval_exp procedure to interpret JavaScript arithmetic expressions.
# Only handle +, - and numbers for now.

def eval_exp(tree):
    # ("number" , "5")
    # ("binop" , ... , "+", ... )
    nodetype = tree[0]
    if nodetype == "number":
        return int(tree[1])
    elif nodetype == "binop":
        left_child = tree[1]
        operator = tree[2]
        right_child = tree[3]
        left_value = eval_exp(left_child)
        right_value = eval_exp(right_child)
        if operator == '+':
            return left_value + right_value
        elif operator == '-':
            return left_value - right_value


test_tree1 = ("binop",("number","5"),"+",("number","8"))
print eval_exp(test_tree1) == 13

test_tree2 = ("number","1776")
print eval_exp(test_tree2) == 1776

test_tree3 = ("binop",("number","5"),"+",("binop",("number","7"),"-",("number","18")))
print eval_exp(test_tree3) == -6