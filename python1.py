#Ex: 2
Name = input("What is your name : ")
From = input("Where are you frorm : ")
age = int (input ("How old are you :"))
Height=float(input("How tell are you :"))
print ("________________________________")
print ("Your name     : "+Name)
print ("You come form : "+From)
print ("You are "+ str(age) +" year old")
print ("Your tall     : "+str(Height)+"m")
#Ex : 3
wigth = float(input ("Width : "))
length = float(input ("Length :"))
Area = wigth*length
print ("The area is "+str(Area)+" m^2")

#Ex4

width = float(input (" Width: "))

length = float(input("Length: "))

Area   = (width*length)/43560

print ("The are is "+str(Area)+ " acres ")
#Ex : 5
Num = int(input("Enter Number : "))
Num1 = Num + 1
Num2 = (Num*Num1)/2
if Num > 1 :
    print ("Answer : "+str(Num2))
else :
    print ("It is worng !")