# The Living and the Dead
#
# In addition to optimizing expressions, it is also possible to optimize
# statements. There are many ways to do so, and we will explore one in this
# problem.
#
# (This problem description looks long, but that is mostly because it
# contains a few worked examples.)
#
# Consider this JavaScript fragment:
#
#       function myfun(a,b,c,d) {
#               a = 1;
#               b = 2;
#               c = 3;
#               d = 4;
#               a = 5;
#               d = c + b;
#               return (a + d);
#       }
#
# Many of the assignment statements end up computing values that are never
# used. The output of the function only really depends on the final values
# of a and d. This function, with two of the lines removed, computes the
# same answer:
#
#       function myfun(a,b,c,d) {
#               # a = 1;
#               b = 2;
#               c = 3;
#               # d = 4;
#               a = 5;
#               d = c + b;
#               return (a + d);
#       }
#
# Those lines can be safely removed because they do not compute a value
# that is used later. We say that a variable is LIVE if the value it holds
# may be needed in the future. More formally, a variable is LIVE if its
# value may be read before the next time it is overwritten. Whether or not
# a variable is LIVE depends on where you are looking in the program, so
# most formally we say a variable is live at some point P if it may be read
# before being overwritten after P.
#
# We can compute the set of live variables by looking at the statements in
# the function in reverse order.
#
#               return (a + d);
#
# Since the output of the function depends on (a + d), a and d are both
# live right before this statement. Now we consider one more statement:
#
#               d = c + b;
#               return (a + d);
#
# "a" and "d" were live going in to the return statement. What is live
# before "d = c + b"? Well, since "d" is overwritten, we have to remove it
# from the set. But since "c" and "b" are written, we have to add them to
# the set. So the set of live variables before that assignment statement is
# "a", "b", "c". In fact, we could annotate the whole program:
#
#       function myfun(a,b,c,d) {
#               a = 1;
#               # LIVE: nothing
#               b = 2;
#               # LIVE: b
#               c = 3;
#               # LIVE: c, b
#               d = 4;
#               # LIVE: c, b
#               a = 5;
#               # LIVE: a, c, b
#               d = c + b;
#               # LIVE: a, d
#               return (a + d);
#       }
#
# Once we know which variables are LIVE, we can now remove assignments to
# variables that will never be read later. Such assignments are called DEAD
# code. Formally, given an assignment statement "X = ...", if "X" is not
# live after that statement, the whole statement can be removed.
#
# Note that remove some dead code may make it possible to remove more
# later. For example, in this fragment:
#
#               a = 1;
#               b = a + 1;
#               c = 2;
#               return c;
#
# We can initially find the following LIVE variables:
#
#               a = 1;
#               # LIVE: a
#               b = a + 1;
#               # LIVE: nothing
#               c = 2;
#               # LIVE: c
#               return c;
#
# But if we remove the "b = a + 1" assignment and repeat the process, we
# will be able to remove the "a = 1" code as well!
#
# In this assignment, you will write an optimizer that removes dead code.
# For simplicity, we will only consider sequences of assignment statements
# (once we can optimize those, we could weave together a bigger optimizer
# that handles both branches of if statements, and so on, but we'll just do
# simple lists of assignments for now).
#
# We will encode JavaScript fragments as lists of tuples. For example,
#
#               a = 1;
#               b = a + 1;
#               c = 2;
#
# Will be encoded as:
#
fragment2 = [ ("a", ["1"] ) ,           # a = 1
              ("b", ["a", "1"] ),       # b = a operation 1
              ("c", ["2"] ), ]          # c = 2
#
# That is, each assignment "LHS = RHS op RHS op RHS ..." will just be
# encoded as (LHS, [RHS, RHS, RHS]). A block is then a list of such
# assignments.
#
# Write a procedure removedead(fragment,returned). "fragment" is encoded
# as above. "returned" is a list of variables returned at the end of the
# fragment (and thus LIVE at the end of it).
#
# Hint 1: One way to reverse a list is [::-1]
# >>> [1,2,3][::-1]
# [3, 2, 1]
#
# Hint 2: One "functional programming" way to make a new list that is just
# like L but with all copies of X removed is:
# [ e for e in L if e != X ]
#
# Hint 3: Remember that if anything changes, you should call yourself
# recursively because you may find even more dead code!

def removedead(fragment,returned):
    old_fragment = fragment
    new_fragment = []
    live = returned
    for stmt in fragment[::-1]: # work line by line backwards
        if stmt[0] in live: # if the LHS of this stmt, the variable to which we are assignming
            new_fragment = [stmt] + new_fragment # add this stmt to the new, optimized fragment
        live = [ x for x in live if x != stmt[0] ] # update the live list, with a duplicate list
        live = live + stmt[1] # update the live list with the list of variables on the RHS
    if new_fragment == old_fragment:
        return new_fragment # if we didn't change anything, return and stop
    else:
        return removedead(new_fragment, returned)


fragment1 = [ ("a", ["1"]),
              ("b", ["2"]),
              ("c", ["3"]),
              ("d", ["4"]),
              ("a", ["5"]),
              ("d", ["c","b"]), ]


print removedead(fragment1, ["a","d"]) == \
        [('b', ['2']),
         ('c', ['3']),
         ('a', ['5']),
         ('d', ['c', 'b'])]

print removedead(fragment2, ["c"]) == [('c', ['2'])]

print removedead(fragment1, ["a"]) == [('a', ['5'])]

print removedead(fragment1, ["d"]) == \
        [('b', ['2']),
         ('c', ['3']),
         ('d', ['c', 'b'])]
