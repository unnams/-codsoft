import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R'
         'S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','#','$','%','&','(',')','*','+']
print("welcome to my password generator")
nr_letters=int(input("how many letters you want to like in your password\n"))
nr_sy=int(input("how many symbols you want"))
nr_num=int(input("how many numbers you want"))
password=''
for char in range(1,nr_letters+1):
    password+=random.choice(letters)
for char in range(1,nr_sy+1):
    password+=random.choice(symbols)
for char in range(1,nr_num+1):
    password+=random.choice(numbers)
print(password)
