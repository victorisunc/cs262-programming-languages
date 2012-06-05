# QUIZ : Variable Lookup

# Adding variable lookup to the interpreter!

def eval_exp(tree, environment):
    nodetype = tree[0]
    if nodetype == "number":
        return int(tree[1])
    elif nodetype == "binop":
        left_value = eval_exp(tree[1], environment)
        operator = tree[2]
        right_value = eval_exp(tree[3], environment)
        if operator == "+":
            return left_value + right_value
        elif operator == "-":
            return left_value - right_value
    elif nodetype == "identifier":
        # ("binop", ("identifier","x"), "+", ("number","2"))
        # QUIZ: (1) find the identifier name
        # (2) look it up in the environment and return it
        variable_name = tree[1]
        return env_lookup(environment, variable_name)


# Here's some code to simulate env_lookup for now. It's not quite what we'll be
# using by the end of the course.

def env_lookup(env,vname):
        return env.get(vname,None)

environment = {"x" : 2}
tree = ("binop", ("identifier","x"), "+", ("number","2"))
print eval_exp(tree,environment) == 4