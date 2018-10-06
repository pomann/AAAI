from Node import Node
from string import ascii_lowercase

class WordGameNode(Node):
   def __init__(self, name, parent = None):
      # Ensure lowercase letters (no digits or special chars)
      for letter in name:
         assert letter in ascii_lowercase
      self.name = name
      self.parent = parent

   def __str__(self):
      return self.name

   def get_children(self):
      alp = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
      # all one letter mutations of the word
      child_words = []# Your code here
      for v,i in enumerate(self.name):
          alt = [n for n in self.name]
          for l in alp:
              if l != i.upper():
                  alt[v] = l.lower()
                  child_words.append(WordGameNode(''.join(alt)))
                  
      return child_words# Need to return a list of WordGameNode objects.

   def get_parent(self):
      return self.parent
      
   def get_path(self):
      node = [self]
      parent = self.get_parent()
      while parent != None:
          node.append(parent)
          parent = parent.get_parent()
      return node