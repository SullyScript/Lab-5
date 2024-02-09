# ECOR 1041 Lab 5

__author__ = "Emily Causi"
__student_number__ = "101236902"

#======================================================
# Exercise 1
def tip(meal_Cost: float, satisfaction_Level: int) -> float:
     """Return a tip based on customer satisfaction regarding level of 
     service recieved.
     Preconditions: meal_Cost >= 0, 
     1 <= satisfaction_Level >= 3 
     >>> tip(50.0, 1)
     10.0
     >>> tip(13.8, 2)
     2.07
     >>> tip(82.5, 3)
     4.12
     """
     if (satisfaction_Level == 1):   
          return round(meal_Cost * 0.20,2)
     elif (satisfaction_Level == 2):
          return round(meal_Cost * 0.15,2)
     elif (satisfaction_Level == 3):
          return round(meal_Cost * 0.05,2) 

#======================================================
# Exercise 2
def coupon(grocery_Cost: float) -> float:
     """Return coupon dependant on the amount spent on groceries.
     Preconditions: grocery_Cost >= 0
     >>> coupon(10.0)
     0.0
     >>> coupon(72.4)
     7.24
     >>> coupon(252.3)
     35.32
     """
     if (grocery_Cost > 210):
          return round(grocery_Cost * 0.14,2)
     elif ((grocery_Cost > 150) and (grocery_Cost <= 210)):
          return round(grocery_Cost * 0.12,2)
     elif ((grocery_Cost > 60) and (grocery_Cost <= 150)):
          return round(grocery_Cost * 0.10,2)
     elif ((grocery_Cost >= 10) and (grocery_Cost <= 60)):
          return round(grocery_Cost * 0.8,2)
     else:
          return grocery_Cost * 0

#======================================================
# Exercise 3
def bakers_party(is_Weekend: bool, pasteries_Brought: int) -> bool:
     """Return whether or not a bakers party was successful, dependant on 
     the date and number of pasteries in attendance. 
     Preconditions: pasteries_Brought >= 0
     >>> bakers_party(False, 70)
     False
     >>> bakers_party(True, 30)
     False
     >>> bakers_party(True, 110)
     True
     """
     if (((pasteries_Brought >= 40) and (pasteries_Brought <= 60) and 
          (is_Weekend == False)) or ((is_Weekend == True) and 
          (pasteries_Brought >= 40))):
          return True
     else:
          return False
          
#======================================================
# Exercise 4
def squirrel_play(is_Summer: bool, temperature: int) -> bool:
     """Return whether or not the squirrels are playing or not, dependant on
     the temperature outside and the season.
     Preconditions: temperature >= 0
     >>> squirrel_play(True, 70)
     True
     >>> squirrel_play(True, 120)
     False
     >>> squirrel_play(False, 89)
     True
     """
     if (((is_Summer == False) and (temperature >= 60) and (temperature <= 90))
         or ((is_Summer == True) and (temperature >= 60) and (temperature <= 100)
             )):     
          return True
     else:
          return False

#======================================================
# Exercise 5
def great_42(a: int, b: int) -> bool:
     """Return whether or not 2 hitchhikers pass the great 42 test...
     >>> great_42(42, 0)
     True
     >>> great_42(40, 2)
     False
     >>> great_42(-11, 53)
     True
     """  
     a = abs(a)
     b = abs(b)
     if (a == 42 or b == 42 or ((b - a) == 42) or ((a - b) == 42) 
         or ((a + b) == 42)):
          return True
     else:
          return False

#======================================================
# Exercise 6
def multiply_uniques(a: int, b: int, c: int) -> int:
     """Return the product of 3 inputted values, given they are unique from
     one another.
     >>> multiply_uniques(2, 6, 3)
     36
     >>> multiply_uniques(4, 7, 4)
     7
     >>> multiply_uniques(5, 5, 5)
     1
     """
     if ((a != b) and (b != c) and (a != c)):
          return a * b * c
     elif ((a == b) and (b != c)):
          return c
     elif ((a == c) and (a != b)):
          return b
     elif ((b == c) and (b != a)):
          return a
     elif (a == b == c): 
          return 1
