"""Create a custom error by inheriting from a built in error class"""

class CustomError(TypeError):
    """
    Custom exception with an error code
    """
    def __init__(self, errcode, message):
        super().__init__(f'Error code {errcode}: {message}')
        self.errcode = errcode

# raise CustomError(500, 'Invalid data type!!!')

err = CustomError(500, 'Invalid data type!!!')
print(err.__doc__)