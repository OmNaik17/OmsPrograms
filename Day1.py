def main():
  return_value= get_multiplier(10,20)
  return_value2= get_sum(10,20)
  print (return_value)
  print (return_value2)
  
def get_multiplier(first, second):
  product = first * second
  return product
  
def get_sum(first,second):
   sum = first + second
   return sum
  
if __name__== "__main__":
  main()
