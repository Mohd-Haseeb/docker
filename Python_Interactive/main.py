from random import randint

min_number = int(input("Enter the minimum number : "))
max_number = int(input("Enter the maximum number : "))

if(min_number > max_number):
   print("Please enter a valid number")
else:
   rnd_number = randint(min_number, max_number)
   print(rnd_number)


## docker run -it [id]

## docker start -a -i [id]
