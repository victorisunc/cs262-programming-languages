# Your function should display HTML according to a given parse tree.

# graphics.warning(msg) displays an error message. Upon encountering mismatched
# tags, use graphics.warning to display the error message: "mismatched tag".

# To display a tag, use graphics.begintag(tag,args) at the start and
# graphics.endtag() at the end of the tag.

import graphics

def interpret(trees): # Hello, friend
    for tree in trees: # Hello,
        # ("word-element","Hello")
        nodetype=tree[0] # "word-element"
        if nodetype == "word-element":
            graphics.word(tree[1])
        elif nodetype == "tag-element":
            # <b>Strong text</b>
            tagname = tree[1] # b
            tagargs = tree[2] # []
            subtrees = tree[3] # ...Strong Text!...
            closetagname = tree[4] # b
            if (tagname != closetagname):
                graphics.warning("mismatched tag")
            else:
                graphics.begintag(tagname, tagargs)
                interpret(subtrees)
                graphics.endtag()

# Note that graphics.initialize and finalize will only work surrounding a call
# to interpret

graphics.initialize() # Enables display of output.\
interpret([("word-element","Hello")])
graphics.finalize() # Enables display of output.

