from py_maths import *
import c_maths

#I am using the GMP library in C to give me bignum maths support when not in
#Python. Argument values passed to C however can only go in as native C types,
#so there is an effective bottleneck on number size for arguments passed
#directly to C. This can be avoided by passing string arguments instead which
#may then be parsed into GMP data types. I don't think it's elegant however to
#be conscientious about always converting to strings, so I've implemented these
#method calls at the Python module level to automate needed conversions.


def c_fibo_iter(inpt):
    """
    An iterative Fibonacci sequence generator. It will return the set of
    Fibonacci numbers which are less than or equal to the input integer as a
    list.
    """
    if isinstance(inpt, str):
        return c_maths.c_fibo_iter(inpt)
    else:
        return c_maths.c_fibo_iter(str(inpt))

