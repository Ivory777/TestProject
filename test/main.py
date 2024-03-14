from errors.errors import MyError
"""
Testing imports. Import the MyError class.
"""
# Test the exception
name = 'pierre'

try:
    if name != 'john':
        raise MyError('Name is not equal to John')
except MyError as e:
    print(repr(e))