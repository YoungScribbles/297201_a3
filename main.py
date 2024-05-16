
# 297201 - Assignment 3
#
#   M. Phillips
#   J. X
#   F. X
#
#   License plate model

import pandas as pd
import plate_parser as pp
import plate_model as pm

# Tokenise input

a = 'Test Input a'
b = 'TeST inPUT b'
c = 'TEST INPUT 3'
d = 'TESTPLA'

inputs = [a,b,c]

mod = pm.PlateModel('./data/applications.csv')
mod.build_model()
mod.evaluate_model()

while 1:
    p = input('Enter your license plate: ')

    if p == 'q':
        break

    mod.predict_approved(p)