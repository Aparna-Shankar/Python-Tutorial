
def find_in(iterable, finder, expected):
    for i in iterable:
        if finder(i) == expected:
            return i
    raise NotFoundError(f'{expected} not found in the iterable provided!')

class NotFoundError(Exception):
    pass

if __name__ == '__main__': # This will execute only when find.py is run as a script
    print(find_in(['Aparna', 'Ann', 'Teena', 'Jasu'] , lambda x:x, 'Jasu'))

print(__name__)