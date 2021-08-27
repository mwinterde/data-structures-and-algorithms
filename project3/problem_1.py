def sqrt(number):
   """
   Calculate the floored square root of a number

   Args:
      number(int): Number to find the floored squared root
   Returns:
      int: Floored Square Root
   """

   if number < 0:
      return None
   lower = 0 # lower bound is always smaller than number**2
   upper = number + 1 # upper bound is always greater than number**2

   while upper - lower > 1:
      middle = lower + (upper - lower) // 2
      if middle**2 <= number:
         lower = middle # move right
      else:
         upper = middle # move left

   return lower

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")

print ("Pass" if  (500 == sqrt(250_000)) else "Fail")
print ("Pass" if  (sqrt(-20) is None) else "Fail")
