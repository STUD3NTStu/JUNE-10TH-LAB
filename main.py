'''
Function 1:
'''
'''
nums=[] #assigns the object nums an empty list.
wrds=[] #assigns the object wrds an empty list.

def wrd_or_num(x): #defines the wrd_or_num function and has it take one argument.
  for i in x: #goes over each iteration in the input.
    if i.isdigit()==1: #checks to see if the current iteration is a digit.
      nums.append(i) #adds the curret iteration to the end of the nums list if it is a digit.
    elif i.isalpha()==1: #checks to see if the current iteration is a word.
      wrds.append(i) #adds the current iteration to the ed of the wrds list.
  return print("The numbers in the list are:", ' '.join(nums),"\n" "And the words in the list are:", ' '.join(wrds)) #prints off the separate lists of wrds and nums.

print(wrd_or_num([str(s) for s in input("Please submit any number of digits and words separated only by spaces\n").split()])) #asks the user to submit any numbers and words they want separated by spaces. This turns the inputted string into a list of individual strings separated at the spaces.
'''
'''
Function 2:
'''
''' temp break
nums=[] #assigns the object nums an empty list.
wrds=[] #assigns the object wrds an empty list.

def wrd_or_num(x): #defines the wrd_or_num function and has it take one argument.
  for i in x: #goes over each iteration in the input.
    if i.isdigit()==1: #checks to see if the current iteration is a digit.
      nums.append(i) #adds the curret iteration to the end of the nums list if it is a digit.
    elif i.isalpha()==1: #checks to see if the current iteration is a word.
      wrds.append(i) #adds the current iteration to the ed of the wrds list.
  return print("The numbers in the list are:", ' '.join(nums),"\n" "And the words in the list are:", ' '.join(wrds), "\n", "Every other inputted number:", ' '.join[nums[::2]]) #prints off the separate lists of wrds and nums before it prints off every second iteration in nums.

print(wrd_or_num([str(s) for s in input("Please submit any number of digits and words separated only by spaces\n").split()])) #asks the user to submit any numbers and words they want separated by spaces. This turns the inputted string into a list of individual strings separated at the spaces.
'''
'''
Function 2:
'''
''
def wrd_or_num(x): #defines the wrd_or_num function and has it take one argument.
  for i in x: #goes over each iteration in the input.
    if i.isdigit()==1: #checks to see if the current iteration is a digit.
      nums.append(i) #adds the curret iteration to the end of the nums list if it is a digit.

  return print("The numbers in the list are:", ' '.join(nums),"\n" "And the words in the list are:", ' '.join(wrds)) #prints off the separate lists of wrds and nums.

print(wrd_or_num([str(s) for s in input("Please submit any number of digits and words separated only by spaces\n").split()])) #asks the user to submit any numbers and words they want separated by spaces. This turns the inputted string into a list of individual strings separated at the spaces.
''