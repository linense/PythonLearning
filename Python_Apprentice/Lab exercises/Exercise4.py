
from abc import ABC, abstractmethod

# Create a class that implements an abstract method
class Post(ABC):
  @abstractmethod
  def getTitle(self):
    pass

  @abstractmethod
  def getText(self):
    pass
  
# Create a subclass
# Implement a static method in the subclass
class Link(Post):
  def __init__(self, title, url):
    self.title = title
    self.url = url

  def getTitle(self):
    return self.title

  def getText(self):
    return self.url
  
class Comment(Post):
  def __init__(self, title, comment, user):
    self.title = title
    if(len(comment) > 500):
      raise ValueError('Comment too long.') 
    self.comment = comment
    self.user = user

  def getTitle(self):
    return self.title

  def getText(self):
    return self.comment

  def getUser(self):
    return self.user
  
class Article(Post):
  def __init__(self, title, body):
    self.title = title
    self.body = body

  def getTitle(self):
    return self.title

  def getText(self):
    return self.body
  
# Instantiate the class and output its contents
posts = []
a = Link('Link title', 'http://example.com/link.html')
posts.append(a)
print(a.getText())
print()

b = Comment('Comment title', 'comment', 'Steve')
c = Article('Article title', 'Article text')
posts.append(b)
posts.append(c)

for p in posts:
  print(p.getTitle())


"""""
Task

    Implement an abstract class and use static methods in a Python program

    Create a class that implements an abstract method
    Create a subclass
    Implement a static method in the subclass
    Instantiate the class and output its contents

Instructions
Task 1 - Create a class that implements an abstract method

    For this exercise start out by importing some important features or methods that we need to implement our abstractions. On line 1 we have from abc import the uppercase ABC, abstractmethod. The ABC stands for abstract base class and abstractmethod is a decorator for abstract methods.

    The second step of the exercise is to create a class that implements an abstract method. Create a class Post(ABC) with ABC as its parent class. On line 5 we have @abstractmethod, we have the decorator. Then def getTitle with self to make it a member method or member function, and I define it with pass. It has the pass keyword because it doesn't implement a body to the method.

    On line 9, there's another @abstractmethod decorator with another method def getText. We have two abstract methods in this abstract class called Post.

from abc import ABC, abstractmethod

# Create a class that implements an abstract method
class Post(ABC):
  @abstractmethod
  def getTitle(self):
    pass

  @abstractmethod
  def getText(self):
    pass

Task 2 + 3

    Now we need to create a subclass and implement a static method in the subclass. Those are the next two steps of the exercise. Create a class link which subclasses or inherits from Post, our abstract base class. It defines its __init__ method that take two parameters, a title and a URL, and then it sets the self.title and the self.url to their given variables.

    On line 20, define the getTitle which is required because it's an abstract method in the base class. And it just returns self.title and then getText which returns self.url. The text of the link is the actual URL of that link. And we implement two more subclasses.

# Create a subclass
# Implement a static method in the subclass
class Link(Post):
  def __init__(self, title, url):
    self.title = title
    self.url = url

  def getTitle(self):
    return self.title

  def getText(self):
    return self.url

    The first one is comment. A comment is a type of post. We have class Comment(Post). In its __init__ method, it takes the parameters, title, comment, and user. Each comment has a title of the comment, the comment itself, the comment body or text, and the user that submitted the comment. On line 29, set self.title is equal to title. Check the length of the comment and if it's greater than 500 characters, raise a value error saying that the comment is too long. Otherwise I set comment equal to comment and self.user equals user. Implement the getTitle and getText methods, as well as a getUser method. And they return their respective variables. In the case of getText, the text of a comment is the actual comment body itself, so it returns self.comment.

class Comment(Post):
  def __init__(self, title, comment, user):
    self.title = title
    if(len(comment) > 500):
      raise ValueError('Comment too long.') 
    self.comment = comment
    self.user = user

  def getTitle(self):
    return self.title

  def getText(self):
    return self.comment

  def getUser(self):
    return self.user

    And then my third subclass of our abstract base class Post is an article. We have class Article(Post). In its __init__ method, it has a title and a body, so the body of the article, and it sets the respective variables of self.title and self.body. And it returns the title for getTitle and the getText method returns self.body.

class Article(Post):
  def __init__(self, title, body):
    self.title = title
    self.body = body

  def getTitle(self):
    return self.title

  def getText(self):
    return self.body

Task 4 - Instantiate the class and output its contents

    Now we need to instantiate the class and output its contents. Start by creating a list called posts. This will have the different posts, whether it be a link, a comment, or an article, and we'll add them to this list.

    On line 59 create a link a = Link, that's called link title with a link http://example.com/link.html. Then call post.append(a), so we append this to the posts list. And then I print a.getText() and print an empty print statement to put a space between this and the next part of the output.

    Then on line 64 we have b = Comment with the title as Comment title, the body of the text comment, and the user Steve. Create an article c = Article with Article title and Article text as its arguments. Then call posts.append(b) and then posts.append(c). Now loop over the posts and call getTitle on each of these posts, because they all implement the getTitle. On line 69, we have for p in posts, print p.getTitle.

# Instantiate the class and output its contents
posts = []
a = Link('Link title', 'http://example.com/link.html')
posts.append(a)
print(a.getText())
print()

b = Comment('Comment title', 'comment', 'Steve')
c = Article('Article title', 'Article text')
posts.append(b)
posts.append(c)

for p in posts:
  print(p.getTitle())

Terminal

    Run the code, And we get the output. We get the URL, so the getText called on the variable a, which was a link so it returns the link. And then in our for loop, the getTitle of each of the elements in the Posts list, are Link title, Comment title, and Article title as expected. And that concludes this exercise.
"""
