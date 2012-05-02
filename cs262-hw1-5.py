# Title: Simulating Non-Determinism

# Each regular expression can be converted to an equivalent finite state
# machine. This is how regular expressions are implemented in practice.
# We saw how non-deterministic finite state machines can be converted to
# deterministic ones (often of a different size). It is also possible to
# simulate non-deterministic machines directly -- and we'll do that now!
#
# In a given state, a non-deterministic machine may have *multiple*
# outgoing edges labeled with the *same* character.
#
# To handle this ambiguity, we say that a non-deterministic finite state
# machine accepts a string if there exists *any* path through the finite
# state machine that consumes exactly that string as input and ends in an
# accepting state.
#
# Write a procedure nfsmsim that works just like the fsmsim we covered
# together, but handles also multiple outgoing edges and ambiguity. Do not
# consider epsilon transitions.
#
# Formally, your procedure takes four arguments: a string, a starting
# state, the edges (encoded as a dictionary mapping), and a list of
# accepting states.
#
# To encode this ambiguity, we will change "edges" so that each state-input
# pair maps to a *list* of destination states.
#
# For example, the regular expression r"a+|(?:ab+c)" might be encoded like
# this:
edges = { (1, 'a') : [2, 3],
          (2, 'a') : [2],
          (3, 'b') : [4, 3],
          (4, 'c') : [5] }
accepting = [2, 5]
# It accepts both "aaa" (visiting states 1 2 2 and finally 2) and "abbc"
# (visting states 1 3 3 4 and finally 5).

def nfsmsim(string, current, edges, accepting):
    if string == "":
      return current in accepting
    else:
      letter = string[0]
      if (current, letter) in edges:
        destination = edges[(current, letter)]
        for element in destination:
          if element in accepting:
            return element in accepting
          else:
            remaining_string = string[1:]
            return nfsmsim(remaining_string, current, edges, accepting)
      else: return False



# This problem includes some test cases to help you tell if you are on
# the right track. You may want to make your own additional tests as well.
edges_2 = {(2, 'a'): [2],
           (1, 'a'): [2, 3],
           (3, 'b'): [4, 3],
           (4, 'c'): [5]}
print "Test case 1 passed: " + str(nfsmsim("abc", 1, edges, accepting) == True)
print "Test case 2 passed: " + str(nfsmsim("aaa", 1, edges, accepting) == True)
print "Test case 3 passed: " + str(nfsmsim("abbbc", 1, edges, accepting) == True)
print "Test case 4 passed: " + str(nfsmsim("aabc", 1, edges, accepting) == False)
print "Test case 5 passed: " + str(nfsmsim("", 1, edges, accepting) == False)
print "Test case 6 passed: " + str(nfsmsim('aabc', 1, edges_2, accepting))