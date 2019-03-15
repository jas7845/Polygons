import turtle #turtle

import sys #argv

def draw_poly_rec(length, depth, fill) :
    # recursively draws polygons until its a triangle
    # parameters:
    #  Length: length of the sides (int)
    #  Depth: amount of sides (int)
    #  Fill: whether it is filled(boolean)
    #returns the sum of all the side lengths

    sum = 0
    turtle.down()
    color = turtle.pencolor()

    if fill :         #draws the polygons first which allows then to be filled in independently
        turtle.begin_fill()
        for x in range(depth) :
            turtle.color(COLORS[depth])
            poly(depth, length)
        turtle.end_fill()


    if depth == 2 : # base case for recursive function (ends at 2 so it ends drawing a triangle)
        return 0
        #pass

    else :          #draws the polygons recursively and calculates the sum of the sides
        for x in range(depth) :
            turtle.color(COLORS[depth])
            turtle.forward(length)
            turtle.left(360 / (depth))
            sum += length
            sum += draw_poly_rec(length/2, depth-1, fill)
    return sum # returns sum of th sides

def poly(numsides, length) :
    # draws the polygons individually so that they can get filled
    # parameters:
    # numsides: are the number of sides in the polygon
    # length: length of each side
    # called in the recursive method so that each level can get filled the correct color

    turtle.fd(length)
    turtle.left(360/numsides)


def init(sides, filling) :
    # initializes screen size
    # parameters:
    # sides: amound of sides in the command line
    # filling: if it should be filled or not
    # writes my name and the amount of sides and if it should be filled in bottom left


    turtle.screensize(WINDOW_LENGTH, WINDOW_LENGTH)

    turtle.speed(0)

    #turtle.tracer(0,0) # WONT DRAW THE LAST TRIANGLE?????

    writing = ''
    writing = 'Sides: '
    writing += str(sides)
    writing += '  Fill: '
    writing += str(filling)

    turtle.up()
    turtle.setposition(-200, -300)
    turtle.write(writing, move=False, align="right", font=("Arial", 10, "normal"))
    turtle.setposition(-200, -270)

    turtle.write("Julie Sojkowski", move=False, align="right", font=("Arial", 10, "normal"))
    turtle.home()
    turtle.setposition(-20, -100)




# constants used for colors at each depth
COLORS = 'red', 'orange', 'yellow', 'SpringGreen3', 'deep sky blue', 'coral', 'medium purple', 'pink', 'medium slate blue'

# window dimensions
WINDOW_LENGTH = 800
SIDE_LENGTH = 200

#pen sizes to use for filled and unfilled polygons
FILL_PEN_WIDTH = 2
UNFILL_PEN_WIDTH = 8

#constands used for the amount of sides and fill
num_sides = 0
fill = True



def main() -> None:
#executes polygon function

    fill_option = sys.argv[2]
    fill = True
    if fill_option == "unfill":
        fill = False

    num_sides = int(sys.argv[1])

    init(num_sides, fill)
    sum = 0
    turtle.down()

    if fill :
        turtle.width(FILL_PEN_WIDTH)
        turtle.tracer(0, 0)
        print(draw_poly_rec(SIDE_LENGTH, num_sides, fill))
        turtle.update()
    else :
        turtle.width(UNFILL_PEN_WIDTH )
        turtle.tracer(0, 0)
        print(draw_poly_rec(SIDE_LENGTH, num_sides, fill))
        turtle.update()

    turtle.mainloop()

if __name__ == '__main__':
    main()