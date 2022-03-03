
def part1():
  # for part 1
  print("part 1")
  # Assign the value 42 (an integer) to a variable with the name n

  # Assign twice the value of the number π (the approximate value 3.14159 for π will     
  # do) to a variable named tau

  # Assign the value Sault College (a string) to a variable named school

  n = 42 
  tau = 3.14169 * 2
  school = "Sault College"
  
def part2():
  #for part 2
  print("part 2")
  # class = "CSD110"        
  # desired-grade = 100     
  # 2hot = "hothot"
  # 3.14159 = pi
  
  class_code = "CSD110"        
  desired_grade = 100     
  hot2 = "hothot"
  pi =3.14159 


def part3():
  #for part 3
  print("part 3")
  warm = "Hot" 
  # Hot can only be written once in this segment of code so I used warm as the variable with the string hot being   the value
  print("Feeling..."+warm+warm+warm+"!")
  

def part4():
  #for part 4
  print("part 4")
  # NOTE: The volume of a square-base pyramid is 1/3 x base2 x height. A pyramid of base 3,000cm and height 
  # 1,000cm should have a volume of 3,000,000,000 cm3 NOTE:The base and height must be 3,000 cm and 1,000 cm,   
  # espectively, for the autograding tests to pass. You may try other values if you like, but remember to set the 
  # values back to 3,000 and 1,000 before submitting in order to pass the tests.

  height = 1000
  base2 = 3000 
  volume = 1/3 * base2*base2 * height 
  # I did base2*base2 since obviously the creator was implying it was base squared
  print("Your pyramid with a Base of "+str(base2)+"cm and a Height of "+str(height)+"cm and had a Volume of "+str(volume)+"cm3")


  
# 1 and 2 arent needed since they do nothing for the output
part3()
part4()
# line 25 is currently in def part4(): try typing somnething like print("4") under def part4():