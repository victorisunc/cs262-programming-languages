# QUIZ: Evaluating Statements

def eval_stmts(tree, environment):
    stmttype = tree[0]
    if stmttype == "assign":
        # ("assign", "x", ("binop", ..., "+",  ...)) <=== x = ... + ...
        variable_name = tree[1]
        right_child = tree[2]
        new_value = eval_exp(right_child, environment)
        env_update(environment, variable_name, new_value)
    elif stmttype == "if-then-else": # if x < 5 then A;B; else C;D;
        conditional_exp = tree[1] # x < 5
        then_stmts = tree[2] # A;B;
        else_stmts = tree[3] # C;D;
        # QUIZ: Complete this code
        # Assume "eval_stmts(stmts, environment)" exists
        if eval_exp(conditional_exp, environment):
            eval_stmts(then_stmts, environment)
        else:
            eval_stmts(else_stmts, environment)


def eval_exp(exp, env):
        etype = exp[0]
        if etype == "number":
                return float(exp[1])
        elif etype == "string":
                return exp[1]
        elif etype == "true":
                return True
        elif etype == "false":
                return False
        elif etype == "not":
                return not(eval_exp(exp[1], env))

def env_update(env, vname, value):
        env[vname] = value

environment = {"x" : 2}
tree = ("if-then-else", ("true", "true"), ("assign", "x", ("number", "8")), ("assign", "x", "5"))
eval_stmts(tree, environment)
print environment == {"x":8}


