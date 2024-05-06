
# 297201 - Assignment 3
#
#   M. Phillips
#   J. X
#   F. X
#
#   License plate model

import plate_parser as pp

# Tokenise input

a = 'Test Input a'
b = 'TeST inPUT b'
c = 'TEST INPUT 3'

inputs = [a,b,c]

for s in inputs:
    print(s)
    l1 = pp.process_input(s)
    l1.debug()
    l1.convert_to_uint8()
    l1.debug()



