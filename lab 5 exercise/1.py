#lab 5 exercise-1
#name - İbrahim Enes Köse
#id -   2200356055

num  = int(input())
if num % 2 == 0:
    print("Sum of odd numbers --> ",(num/2)**2)
    print("Average of even numbers --> ",((num/2)*((num/2)+1))/(num/2))
else:
    print("Sum of odd numbers --> ",((num+1)/2)**2)
    print("Average of even numbers --> ",(((num-1)/2)*(((num-1)/2)+1))/((num-1)/2))
