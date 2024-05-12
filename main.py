
# 297201 - Assignment 3
#
#   M. Phillips
#   J. X
#   F. X
#
#   License plate model

import plate_parser as pp
import plate_model as pm

pm.init()

# Tokenise input

a = 'Test Input a'
b = 'TeST inPUT b'
c = 'TEST INPUT 3'
d = 'TESTPLA'

inputs = [a,b,c]

for s in inputs:
    print(s)
    l1 = pp.process_input(s)
    l1.debug()
    l1.convert_to_uint8()
    l1.debug()


A = pm.generate_permutations(d)
print(A)
