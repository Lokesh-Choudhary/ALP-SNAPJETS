
#BMI_CALCULATOR
weight=int(input())
height=float(input())
BMI=weight/float(height*height)
if BMI<18.5:
   print("Underweight")

elif BMI>=18.5 and BMI<25:
    print("Normal")

elif BMI>=25 and BMI<30:
    print("Overweight")
else:
    print("Obesity")
