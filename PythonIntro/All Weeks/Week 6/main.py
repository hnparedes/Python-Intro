from turtle import Turtle


def main():
    myvertices = [(50, 0), (75, -30), (75, -60), (50, -90), (0, -90), (-75, -60), (-75, -30), (0, 0)]

    myturtle = Turtle()
    myturtle.hideturtle()

    count = 0

    while count < len(myvertices):
        mytuple = myvertices[count]
        myturtle.goto(mytuple[0], mytuple[1])
        count += 1

    mylist1 = [[1, 2, 3], [4, 5, 6]]
    print(mylist1[0])


main()
