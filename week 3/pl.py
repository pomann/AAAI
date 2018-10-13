class Move:
   def __init__(self, row, col):
      self.row = row
      self.col = col

   def __str__(self):
      return "({0}, {1})".format(self.row, self.col)

SIZE = 3

class Puzzle8Node():
   def __init__(self, position, parent = None):
      # The name will be the square
      # The name should only contain the numbers 1 to 8 and a blank
      sorted_pos = " 123456789ABCDEF" if SIZE == 4 else " 12345678"
      assert "".join(sorted(position)) == sorted_pos
      self.position = position
      self.parent = parent
      self.score = 0
      self.depth = 0

   def __eq__(self, other):
      """Override the default Equals behavior"""
      if other == None:
         return False
      return self.position == other.position

   def __ne__(self, other):
      """Define a non-equality test"""
      return not self.__eq__(other)

   def __hash__(self):
      return hash(self.position)

   def get_parent(self): return self.parent

   def get_path(self):
      # Follow the parent to create the path
      path = []
      node = self
      while node != None:
         path.append(node)
         node = node.parent
      return path

   def heuristic(self, goal):
      # Manhattan
      g_pos = {}
      g_board = goal.make_board(goal.position)
      for row in range(SIZE):
         for col in range(SIZE):
            g_pos[g_board[row][col]] = (row, col)

      dist = 0
      board = self.make_board(self.position)
      for row in range(SIZE):
         for col in range(SIZE):
            tile = board[row][col]
            if tile != ' ':
               # this value should be at goal_row, goal_col
               goal_row, goal_col = g_pos[tile]
               dist += abs(row - goal_row) + abs(col - goal_col)

      return dist

   def __str__(self):
      s = "|"
      for i in range(SIZE):
         start = i * SIZE
         s += self.position[start:start + SIZE] + "|"
      s += " ({}+{})".format(self.depth, self.score)
      return s

   def __repr__(self):
      return str(self)

   def make_board(self, this_position):
      board = [ ['-' for c in range(SIZE)] for r in range(SIZE)]
      index = 0
      for row in range(SIZE):
         for col in range(SIZE):
            board[row][col] = this_position[index]
            index += 1

      return board

   def make_name(self, board):
      position = ''
      for row in range(SIZE):
         for col in range(SIZE):
            position += board[row][col]

      return position

   def get_blank(self, board):
      # Find the blank
      for row in range(SIZE):
         for col in range(SIZE):
            if board[row][col] == ' ':
               return Move(row, col)

      return None # Error, this shouldn't happen. 

   def get_children(self):
      # The children are just the moves.
      children = self.get_moves()
      # Add in the parent
      # (that would be myself!)
      for child in children:
         # Record the parent and the depth.
         child.parent = self
         child.depth = child.parent.depth + 1 # Child is one deeper than parent

      return children

   def get_moves(self):
      # The moves depend on the current board position
      # Lets make the board
      board = self.make_board(self.position)
      blank = self.get_blank(board)

      # Now make the moves. There could be 4
      moves = []
      if blank.col != 0:
         # LEFT
         board[blank.row][blank.col-1], board[blank.row][blank.col] = board[blank.row][blank.col], board[blank.row][blank.col-1]
         # Convert board to a name and append to moves
         moves.append(self.make_name(board))
         # swap back to undo the move
         board[blank.row][blank.col-1], board[blank.row][blank.col] = board[blank.row][blank.col], board[blank.row][blank.col-1]
      if blank.row != 0: # Can't move up if already at the top
         # UP
         # swap blank and position above it
         board[blank.row-1][blank.col], board[blank.row][blank.col] = board[blank.row][blank.col], board[blank.row-1][blank.col]
         # Convert board to a name and append to moves
         moves.append(self.make_name(board))
         board[blank.row-1][blank.col], board[blank.row][blank.col] = board[blank.row][blank.col], board[blank.row-1][blank.col]
      if blank.col != SIZE-1:
         # RIGHT
         board[blank.row][blank.col+1], board[blank.row][blank.col] = board[blank.row][blank.col], board[blank.row][blank.col+1]
         # Convert board to a name and append to moves
         moves.append(self.make_name(board))
         board[blank.row][blank.col+1], board[blank.row][blank.col] = board[blank.row][blank.col], board[blank.row][blank.col+1]
      if blank.row != SIZE - 1:
         # Down
         board[blank.row+1][blank.col], board[blank.row][blank.col] = board[blank.row][blank.col], board[blank.row+1][blank.col]
         # Convert board to a name and append to moves
         moves.append(self.make_name(board))
         board[blank.row+1][blank.col], board[blank.row][blank.col] = board[blank.row][blank.col], board[blank.row+1][blank.col]

      return [Puzzle8Node(move) for move in moves]

def greedy(start, goal, debug = True):
   # We will start here, so the list of nodes to do is the start
   start.score = start.heuristic(goal)
   done = False
   num_searches = 0
   next = start
   while not done:
      # Find the next position
      num_searches += 1

      if debug:
         print(num_searches)
         print(next)

      if next == goal:
         done = True
      else:
         # Keep searching.
         # What searching? This is a greedy search - there is no searching - just try the best child.
         children = next.get_children()
         # Get the score for each of these children
         for child in children:
            child.score = child.heuristic(goal)

            print("\t\t{}".format(child))

         # Best child ...
         best = min(children, key = lambda x : x.score)
         print("\t choose {}".format(best))
         if best.score < next.score:
            next = best # we improved, start from here.
         else:
            done = True # Our move made no progress ... hang our head in shame and give up.

   return num_searches, next

def bfs(start, goal):
   # We will start here, so the list of nodes to do is the start
   todo = [start]
   visited = []
   num_searches = 0
   while len(todo) > 0:
      next = todo.pop(0) # Get (and remove) first element in the list (using the list as a queue)
      num_searches += 1

      if next == goal:
         return num_searches, next
      else:
         # Keep searching.
         visited.append(next) # Remember that we've been here
         children = list(child for child in next.get_children() if child not in visited and child not in todo)
         todo += children
   return num_searches, None # no route to goal, just return how long it took.

def main():

   start = Puzzle8Node('1238 4765')
   goal = Puzzle8Node('24863 175')
   num_searches, next = a_star_search(start, goal)
   print("Searches: {}: path = {}".format(num_searches, next.get_path()) )
   if next == goal:
      print("We dun it!")
   else:
      print(":[")

def a_star_search(start, goal):
   todo = [start]
   visited = set()
   num_searches = 0
   while len(todo) > 0:
      next = todo.pop(0) # Get (and remove) first element in the list (using the list as a queue)
      num_searches += 1

      if next == goal:
         return num_searches, next
      else:
         # Keep searching.
         visited.add(next) # Remember that we've been here

         # Add children to the todo list and update the score
         for child in next.get_children():
            if child not in visited and child not in todo:
               child.score = child.depth + child.heuristic(goal)  # score = g(n) + h(n)
               todo.append(child)

         # Sort the children by score (lowest better)
         todo.sort(key = lambda x : x.score)

   return num_searches, None # no route to goal

if __name__ == "__main__":
   main()
