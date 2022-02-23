def arithmetic_arranger(problems, val= False):

  Line1 = ''
  Line2 = ''
  Line3 = ''
  Dashes = ''
  arranged_problems=''
  
  if len(problems)>=6:
    arranged_problems="Error: Too many problems."
    return arranged_problems
    
  for n in problems:
      
    firstNumber = n.split(" ")[0]
    operator = n.split(" ")[1]
    secondNumber = n.split(" ")[2]

    # Cheking if operands are > 9999
    if len(firstNumber)>4 or len(secondNumber)>4:
      arranged_problems="Error: Numbers cannot be more than four digits."
      return arranged_problems

    #Cheking if operands are numerics
    if not firstNumber.isnumeric() or not secondNumber.isnumeric():
      arranged_problems="Error: Numbers must only contain digits."
      return arranged_problems

    sum=" "
    # Checking if the operator is a '+' or a '-'
    if operator == '+' or operator == '-':
      if operator=="+":
        sum=(str(int(firstNumber)+int(secondNumber)))
      else:
        sum=(str(int(firstNumber)-int(secondNumber)))

      length= max(len(firstNumber),len(secondNumber))+2
      top= str(firstNumber).rjust(length)
      bottom= operator + str(secondNumber).rjust(length-1)
      res= str(sum).rjust(length)
      line=""
      for i in range(length):
        line += "-"
    else:
      arranged_problems="Error: Operator must be '+' or '-'."
      return arranged_problems
    
    if n != problems[-1]:
      Line1 += top +'    '
      Line2 += bottom +'    '
      Dashes += line +'    '
      Line3 += res +'    '
    else:
      Line1 += top  
      Line2 += bottom 
      Dashes += line 
      Line3 += res 

  Line1.rstrip()
  Line2.rstrip()
  Dashes.rstrip()
  Line3.rstrip()  
  if val:
    arranged_problems = Line1 + "\n" + Line2 + "\n" + Dashes + "\n" + Line3
  else:
    arranged_problems = Line1 + "\n" + Line2 + "\n" + Dashes
  return arranged_problems