m1=int(input("enter marks for test1:"))
m2=int(input("enter marks for test2:"))
m3=int(input("enter marks for test3:"))

best_of_two=sorted([m1,m2,m3],reverse=True)[:2]
average_best_of_two=sum(best_of_two)/2
print("average of best two test marks out of three test's marks is",average_best_of_two)