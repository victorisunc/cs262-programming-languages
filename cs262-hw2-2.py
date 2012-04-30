# Email Addresses & Spam
#
# In this assignment you will write Python code to to extract email
# addresses from a string of text. To avoid unsolicited commercial email
# (commonly known as "spam"), users sometimes add the text NOSPAM to an
# other-wise legal email address, trusting that humans will be smart enough
# to remove it but that machines will not. As we shall see, this provides
# only relatively weak protection.
#
# For the purposes of this exercise, an email address consists of a
# word, an '@', and a domain name. A word is a non-empty sequence
# of upper- or lower-case letters. A domain name is a sequence of two or
# more words, separated by periods.
#
# Example: wes@udacity.com
# Example: username@domain.name
# Example: me@this.is.a.very.long.domain.name
#
# If an email address has the text NOSPAM (uppercase only) anywhere in it,
# you should remove all such text. Example:
# 'wes@NOSPAMudacity.com' -> 'wes@udacity.com'
# 'wesNOSPAM@udacity.com' -> 'wes@udacity.com'
#
# You should write a procedure addresses() that accepts as input a string.
# Your procedure should return a list of valid email addresses found within
# that string -- each of which should have NOSPAM removed, if applicable.
#
# Hint 1: Just as we can FIND a regular expression in a string using
# re.findall(), we can also REPLACE or SUBSTITUTE a regular expression in a
# string using re.sub(regexp, new_text, haystack). Example:
#
# print re.sub(r"[0-9]+", "NUMBER", "22 + 33 = 55")
# "NUMBER + NUMBER = NUMBER"
#
# Hint 2: Don't forget to escape special characters.
#
# Hint 3: You don't have to write very much code to complete this exercise:
# you just have to put together a few concepts. It is possible to complete
# this exercise without using a lexer at all. You may use any approach that
# works.


import ply.lex as lex
import re

# Fill in your answer here.

def addresses(haystack):
  better_haystack = re.sub("NOSPAM", "", haystack)
  # regexp = "[\w+\-.]+@[a-z\d\-.]+\.[a-z]+"
  regexp = "[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
  result = re.findall(regexp, better_haystack)
  # print result
  return result


# We have provided a single test case for you. You will probably want to
# write your own.
input1 = """louiseNOSPAMaston@germany.de (1814-1871) was an advocate for
democracy. irmgardNOSPAMkeun@NOSPAMweimar.NOSPAMde (1905-1982) wrote about
the early nazi era. rahelNOSPAMvarnhagen@berlin.de was honored with a 1994
deutsche bundespost stamp. seti@home is not actually an email address.
CommonCompanyName@RandomNOSPAMName.DEAServiceProvider.com"""

output1 = ['louiseaston@germany.de', 'irmgardkeun@weimar.de', 'rahelvarnhagen@berlin.de', 'CommonCompanyName@RandomName.DEAServiceProvider.com']

print addresses(input1) == output1
