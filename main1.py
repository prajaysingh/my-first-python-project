import turtle

def main():
    print ("Welcome to the main menu")
    print ("Here are the menus. Please press 0 or 1 or 2 to select the options below")
    print ("0. Exit program")
    print ("1. Enter details")
    print ("2. Reports")
    val= int(input())
    if val==0:
        exit()
    elif val==1:
        enter_details()
    elif val==2:
        reports()
    else:
        print ("Invalid input")
        exit()

def drawBar(t, height, item):
    drawlist = ['Romance', 'Rom-com', 'Action', 'War', 'Spy', 'Si-Fi', 'Horror', 'Historic', 'Fantasy', 'Animated']
    t.begin_fill()
    t.write(drawlist[item], align="left", font=("Comic Sans MS", 12, "normal"))
    t.left(90)
    t.forward(height)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()


def enter_details():
    outfile = open("movies.txt", "a")
    while True:
        movie = input("Enter movie name: ")
        if len(movie) < 5:
            print("Movie name must be atleast 5 characters. Please enter again")
            continue
        genre = int(input('''Enter Movie Genre : Choose between 1 to 10 below \n Enter 1 for Romance
 Enter 2 for Rom-com \n Enter 3 for Action \n Enter 4 for War \n Enter 5 for Spy
 Enter 6 for Si-Fi \n Enter 7 for Horror \n Enter 8 for Historic
 Enter 9 for Fantasy \n Enter 10 for Animanted \n'''))
        if (not (genre > 0 and genre < 11)):
            print("Genre must be selected from 1 to 10. Please enter again")
            continue
        genrelist = ["Romance", "Rom-com", "Action", "War", "Spy", "Si-Fi", "Horror", "Historic", "Fantasy", "Animated"]
        rating = int(input("Enter rating from 1 to 10: \n"))
        if not (rating > 0 and rating < 11):
            print("Rating must be selected from 1 to 10. Please enter again")
            continue
        outfile.write(movie + "," + genrelist[genre - 1] + "," + str(rating) + '\n')
        flag = input("Press y to continue or any other key to exit\n")
        if flag.lower() != 'y':
            break
    outfile.close()
    print ("Thank you for entering details. Do you wish to see the reports?")
    print ("Please press 0 or 1 to select the options below")
    print ("0. Go to Reports Menu")
    print ("1. Exit ")
    val = int(input())
    if val == 0:
        reports()
    elif val == 1:
        exit()
    else:
        print("Invalid input")
        exit()

def reports():
    print("Welcome to Report Menu")
    print ("Here are the report menus. Please press 0 or 1 to select the options below")
    print ("0. Return to Main menu")
    print ("1. List all movies and display bar graph")
    val = int(input())
    if val == 0:
        main()
    elif val == 1:
        display_reports()
    else:
        print("Invalid input")
        exit()

def display_reports():
    list=[]
    infile = open("movies.txt", "r")
    print("{0:40s} {1:20s} {2:20s}".format("Movies:", "Genre:", "Rating:"))
    for line in infile:
        line = line.rstrip()
        values = line.split(",")
        print("{0:40s} {1:20s} {2:20s}".format(values[0], values[1], values[2]))
        list.append(values[-2])
    infile.close()


    numlist = [list.count('Romance'), list.count('Rom-com'), list.count('Action'), list.count('War'), list.count('Spy'),
               list.count('Si-Fi'), list.count('Horror'), list.count('Historic'), list.count('Fantasy'),
               list.count('Animated')]
    maxheight = max(numlist)
    numbars = 10
    border = 10

    wn = turtle.Screen()
    wn.setworldcoordinates(0 - border, 0 - border, 40 * numbars + border, maxheight + border)
    wn.bgcolor("white")

    pj = turtle.Turtle()
    pj.color("black")
    pj.fillcolor("red")
    pj.pensize(2)

    val = 0
    for a in numlist:
        drawBar(pj, a, val)
        val += 1

    wn.exitonclick()


main()
