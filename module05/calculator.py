class Calculator():

   # This function adds two numbers 
   def add(self, x, y):
      return x + y

   # This function subtracts two numbers 
   def subtract(self, x, y):
      return x - y

   # This function multiplies two numbers
   def multiply(self, x, y):
      return x * y

   # This function divides two numbers
   def divide(self, x, y):
      return x / y

   def start_calc(self):
      ''' Program make a simple calculator that can add, subtract, multiply and divide using functions '''
      print("Select operation.")
      print("1.Add")
      print("2.Subtract")
      print("3.Multiply")
      print("4.Divide")

      # Take input from the user 
      self.choice = int(input("Enter choice(1/2/3/4):"))

      self.num1 = int(input("Enter first number: "))
      self.num2 = int(input("Enter second number: "))

      if self.choice == 1:
         print(self.num1, " + ", self.num2," = ", self.add(self.num1, self.num2))
      elif self.choice == 2:
         print(self.num1, " - ", self.num2," = ", self.subtract(self.num1, self.num2))
      elif self.choice == 3:
         print(self.num1, " * ", self.num2," = ", self.multiply(self.num1, self.num2))
      elif self.choice == 4:
         print(self.num1, " / ", self.num2," = ", self.divide(self.num1, self.num2))
      else:
         print("Invalid choice", self.choice)