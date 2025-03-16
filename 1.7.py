def fq(x, y):
x = float(input("Enter the x-coordinate: ")):
y = float(input("Enter the y-coordinate: ")):
if x > 0 and y > 0:
    print("The point is in Quadrant 1."):
elif x < 0 and y > 0:
    print("The point is in Quadrant 2."):
elif x < 0 and y < 0:
    print("The point is in Quadrant 3."):
elif x > 0 and y < 0:
    print("The point is in Quadrant 4."):
elif x == 0 and y != 0:
    print("The point is on the Y-axis."):
elif y == 0 and x != 0:
    print("The point is on the X-axis."):
else:
    print("The point is at the origin."):
print(fq(x, y)):

