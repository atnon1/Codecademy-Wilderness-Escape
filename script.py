######
# TREENODE CLASS
######
class TreeNode:
  def __init__(self, story_piece):
    self.story_piece = story_piece
    self.choices = []
  
  def add_child(self, node):
    self.choices.append(node)

  def traverse(self):
    story_node = self
    print(story_node.story_piece)
    while len(story_node.choices) > 0:
      #Assume that number of option is not fixed
      options = [str(i + 1) for i in range(len(story_node.choices))]
      choice = input('Enter ' + ','.join(options[:-1]) + ' or ' + options[-1] + ' to continue the story: \n')
      if choice in options:
        chosen_index = int(choice) - 1
        story_node = story_node.choices[chosen_index]
        print(story_node.story_piece)
      else:
        print('Input is incorrect. Try again\n')


  
######
# VARIABLES FOR TREE
######
root_piece = """
You are in a forest clearing. There is a path to the left.
A bear emerges from the trees and roars!
Do you: 
1 ) Roar back!
2 ) Run to the left...
"""
choice_a_piece = """
The bear is startled and runs away.
Do you:
1 ) Shout 'Sorry bear!'
2 ) Yell 'Hooray!'
"""
choice_b_piece = """
You come across a clearing full of flowers. 
The bear follows you and asks 'what gives?'
Do you:
1 ) Gasp 'A talking bear!'
2 ) Explain that the bear scared you.
"""
choice_a_1_piece = """
The bear returns and tells you it's been a rough week. After making peace with
a talking bear, he shows you the way out of the forest.

YOU HAVE ESCAPED THE WILDERNESS.
"""
choice_a_2_piece = """
The bear returns and tells you that bullying is not okay before leaving you alone
in the wilderness.

YOU REMAIN LOST.
"""
choice_b_1_piece = """
The bear is unamused. After smelling the flowers, it turns around and leaves you alone.

YOU REMAIN LOST.
"""
choice_b_2_piece = """
The bear understands and apologizes for startling you. Your new friend shows you a 
path leading out of the forest.

YOU HAVE ESCAPED THE WILDERNESS.
"""


story_root = TreeNode(root_piece)
choice_a = TreeNode(choice_a_piece)
choice_b = TreeNode(choice_b_piece)
choice_a_1 = TreeNode(choice_a_1_piece)
choice_a_2 = TreeNode(choice_a_2_piece)
choice_b_1 = TreeNode(choice_b_1_piece)
choice_b_2 = TreeNode(choice_b_2_piece)
story_root.add_child(choice_a)
story_root.add_child(choice_b)
choice_a.add_child(choice_a_1)
choice_a.add_child(choice_a_2)
choice_b.add_child(choice_b_1)
choice_b.add_child(choice_b_2)
######
# TESTING AREA
######
user_choice = input("What is your name?\n")

print("Once upon a time...")
print(story_root.choices)
story_root.traverse()