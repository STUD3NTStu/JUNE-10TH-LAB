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

print(wrd_or_num([str(s) for s in input("Please submit any number of digits and words separated only by spaces\n.").split()])) #asks the user to submit any numbers and words they want separated by spaces. This turns the inputted string into a list of individual strings separated at the spaces.
'''
'''
Function 2:
'''
'''
nums=[] #assigns the object nums an empty list.

def second_num(x): #defines the second_num function and has it take one argument.
  count=0 #assigns the object count a value of 0.
  for i in x: #goes over each iteration in the input.
    if i.isdigit()==1 and count%2==0: #checks to see if the current iteration is a digit and if the iteration is every other digit.
      nums.append(i) #adds the curret iteration to the end of the nums list if it is a digit.
    count+=1

  return print("Every other number inputted is:", ' '.join(nums)) #prints off the separate lists of wrds and nums.

print(second_num([str(s) for s in input("Please submit any number of digits separated by spaces.\n").split()])) #asks the user to submit any numbers and words they want separated by spaces. This turns the inputted string into a list of individual strings separated at the spaces.
'''