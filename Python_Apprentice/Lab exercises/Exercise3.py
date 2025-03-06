from functools import total_ordering

# Create a basic python class
@total_ordering
class Book:
# Implement an __init__ method
  def __init__(self, title, author, isbn):
    self.title = title
    self.author = author
    self.isbn = isbn

# Implement __repr__ and __str__ methods
  def __repr__(self):
    return '<{0}.{1} object at {2}> ({3}, {4}, {5})'.format(
      self.__module__, type(self).__name__, hex(id(self)),
      self.title, self.author, self.isbn)

  def __str__(self):
    return f'"{self.title}" by "{self.author}"; ISBN: {self.isbn}'

  def __lt__(self, other):
    return (self.author < other.author) or \
            (self.author == other.author and self.title < other.title)

  def __eq__(self, other):
    return (self.author==other.author and self.title == other.title)
  
# Implement comparison or numeric special methods as appropriate for your class
b = Book('Ulysses', 'Joyce, James', '9780679722762')
b2 = Book('Ulysses', 'Joyce, James', '9780679722762')
print(b)
print(repr(b))
print('b == b2: {}'.format(b==b2))

d = Book('Pride and Prejudice', 'Austen, Jane', 'N/A')
print('d < b: {}'.format(d<b))
