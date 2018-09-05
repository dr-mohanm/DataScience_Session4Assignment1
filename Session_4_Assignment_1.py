
# coding: utf-8

# In[1]:


# 1.1  Write a Python Program(with class concepts) to find the area of the triangle using the below formula. 
# area = (s*(s-a)*(s-b)*(s-c)) ** 0.5 
# Function to take the length of the sides of triangle from user should be defined in the parent class and 
#function to calculate the area should be defined in subclass. class Triangle:

# Create parent class and assign 3 attributes to get inputs for 3 sides.
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    print("Parent Class")
    
# Create child class and call parent class using super command and create a method to calculate the area of triangle. 
class Triangle_Child(Triangle):
 
 def __init__(self, a, b, c):
  print ("Child Class")
  super(Triangle_Child, self).__init__(a, b, c)

 def area_tri(self):
    s=(self.a + self.b + self.c)/2
    print (str(s))
    return (s*(s-self.a)*(s-self.b)*(s-self.c))**0.5

# Get the inputs from user.
Tri = Triangle_Child(float(input('Enter a = ')), float(input('Enter b = ')) , float(input('Enter c = ')))

# Print the final result.
print("Area of the triangle: " + str(Tri.area_tri()))


# In[5]:


# 1.2  Write a function filter_long_words() that takes a list of words and an integer n and 
# returns the list of words that are longer than n. 

# create a class and add 2 methods to get the inputs and filter the longest words.
class Words_list:
 def __init__(self, wordlist):
  self.wordlist = wordlist

 def filter_long_words(self, n):
  return list(filter(lambda x:len(x) > n, self.wordlist))

# Pass the input to the class.
Long_word = Words_list(["This", "is" , "the" , "data science" , "course"])

# Print the words which are greater/longer than n.
print ("New List of Words is = " + str(Long_word.filter_long_words(2)) ) 


# In[3]:


# 2.1 Write a Python program using function concept that maps list of words into a list of integers
# representing the lengths of the corresponding words.
# Hint:<200b> <200b>If a list [ ab,cde,erty] is passed on to the python function output should come as [2,3,4]
# Here 2,3 and 4 are the lengths of the words in the list.

# create a class and find the length of each word.
def word_length(word_list):
 return list(map(lambda x: len(x), word_list))

# Pass the input to the class.
word_list = ["This", "is" , "the" , "data science" , "course"]

# Print the lenth of each word.
print ("word lengths in array = " + str(word_length(word_list)))


# In[4]:


# 2.2  Write a Python function which takes a character (i.e. a string of length 1) and 
# returns True if it is a vowel, False otherwise

# FUnction to check char is vowel and return True/False
def vowel_check(char):
 if(char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' or
    char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U'):
  return True
 else:
  return False

# Pass the input
char = input("Enter character: ");

# Check whether the string is vowel or not and print the result.
if (vowel_check(char)):
 print(char, "is a vowel.");
else:
 print(char, "is not a vowel."); 

