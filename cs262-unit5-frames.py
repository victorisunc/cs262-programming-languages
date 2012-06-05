# QUIZ : Frames
# Return will throw an excception
# Function Calls: new environments, catch return values

def eval_stmt(tree,environment):
    stmttype = tree[0]
    if stmttype == "call": # ("call", "sqrt", [("number","2")])
        fname = tree[1] # "sqrt"
        args = tree[2] # [ ("number", "2") ]
        fvalue = env_lookup(fname, environment)
        if fvalue[0] == "function":
            # We'll make a promise to ourselves:
            # ("function", params, body, env)
            fparams = fvalue[1] # ["x"]
            fbody = fvalue[2]
            fenv = fvalue[3]
            if len(fparams) <> len(args):
                print "ERROR: wrong number of args"
            else:
                #QUIZ: Make a new environment frame
                newenv = (fenv, {})
                for i in range(len(args)):
                    argval = eval_exp(args[i], fenv)
                    (newenv[1])[fparams[i]] = argval  # add to env
                # Evaluate the body in the new frame
                try:
                    eval_stmts(fbody, newenv)
                    return None
                except Exception as return_value:
                    return return_value
        else:
            print  "ERROR: call to non-function"
    elif stmttype == "return":
        retval = eval_exp(tree[1],environment)
        raise Exception(retval)
    elif stmttype == "exp":
        eval_exp(tree[1],environment)

def env_lookup(vname,env):
        if vname in env[1]:
                return (env[1])[vname]
        elif env[0] == None:
                return None
        else:
                return env_lookup(vname,env[0])

def env_update(vname,value,env):
        if vname in env[1]:
                (env[1])[vname] = value
        elif not (env[0] == None):
                env_update(vname,value,env[0])


def eval_exp(exp,env):
        etype = exp[0]
        if etype == "number":
            return float(exp[1])
        elif etype == "binop":
            a = eval_exp(exp[1],env)
            op = exp[2]
            b = eval_exp(exp[3],env)
            if op == "*":
                return a*b
        elif etype == "identifier":
            vname = exp[1]
            value = env_lookup(vname,env)
            if value == None:
                print "ERROR: unbound variable " + vname
            else:
                return value

def eval_stmts(stmts,env):
        for stmt in stmts:
            eval_stmt(stmt,env)



sqrt = ("function",("x"),(("return",("binop",("identifier","x"),"*",("identifier","x"))),),{})

environment = (None,{"sqrt":sqrt})

print eval_stmt(("call","sqrt",[("number","2")]),environment)
