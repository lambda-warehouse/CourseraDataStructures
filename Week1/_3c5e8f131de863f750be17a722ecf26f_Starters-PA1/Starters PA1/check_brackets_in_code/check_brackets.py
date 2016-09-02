# python3

#opening brackets problem with a stack

import sys


#----------------------------
class Stack:

    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
         return self.items == []
#-------------------------------

#---------------------------------------
class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

#----------------------------------------


#-----------------------------------------------------------
class CheckBalanced:

    def __init__(self):
        self.isbalanced = False

    def IsBalanced(self):

        text = input()

        opening_brackets_stack = Stack()
        top = ""

        for next in text:

            if next == '(' or next == '[' or next == '{':
                # Process opening bracket, write your code here
                opening_brackets_stack.push(next)
            else:
                
                if next == ')' or next == ']' or next == '}':
                    if (opening_brackets_stack.isEmpty()):
                        return False

                    top = opening_brackets_stack.pop()
                    if((top == '[' and next != ']') or (top== '{' and next != '}') or (top== '(' and next != ')')): 
                        return False
        return opening_brackets_stack.isEmpty()
#-------------------------------------------------------------



if __name__ == "__main__":
    

   
    #opening_brackets_stack = []


    checker = CheckBalanced()

    print(checker.IsBalanced())


            

    
"""
    for i, next in enumerate(text):
        print(str(i)+str(next))
        if next == '(' or next == '[' or next == '{':
            # Process opening bracket, write your code here
            opening_brackets_stack.push(next)
            print("hola2")

        if next == ')' or next == ']' or next == '}':
            # Process closing bracket, write your code here
            pass

    # Printing answer, write your code here
    """