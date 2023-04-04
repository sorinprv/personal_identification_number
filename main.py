from cnp import cnp, cnp_test
from machine import Test

"""Program made for the verification and decoding of the personal numerical code (cnp),
        in order to verify the data on the IC with those from the personal numerical code (cnp)."""
a = cnp
b = cnp_test

print(Test(a).output())
