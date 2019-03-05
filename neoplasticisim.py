from graphics import *
import random

PICWIDTH = 600
PICHEIGHT = 600
MIN_WIDTH = 100
COLORS = ["red", "blue", "yellow", "white"]

win = GraphWin("Piet Mondrian by machine", PICWIDTH, PICHEIGHT)
win.setCoords(0,0,PICWIDTH -1, PICHEIGHT - 1)
win.setBackground("grey")

# generate cut_points and put it in a list
# cut_points contains both start point and end point
def cut(start, end, cut_num):
    cut_points = []

    if cut_num == 0:
        cut_points.append(start)
        cut_points.append(end)
        return cut_points

    # making sure that the cut is large enough
    average_cut_dist = (end - start)//cut_num

    # if average cut distance is 0, return all cut points with equal value and equal to start point
    if average_cut_dist == 0:
        for i in range(0, cut_num+1):
            cut_points.append(start)
        cut_points.append(end)
        return cut_points
    
    cut_points.append(start)
    if cut_num == 0:
        return cut_points
    for i in range(1, cut_num+1):
        rand_cut = random.randrange(start + average_cut_dist*(i-1) , start + average_cut_dist*i)
        cut_points.append(rand_cut)
    cut_points.append(end)
    return cut_points

# generate random cut_points
def random_cut(start, end, max_cut):
    cut_num = random.randrange(2, max_cut)
    cut_points = cut(start, end, cut_num)
    return cut_points

def fill_rect(top_left_x, top_left_y, bottom_right_x, bottom_right_y):
    top_left = Point(top_left_x, top_left_y)
    bottom_right = Point(bottom_right_x, bottom_right_y)
    top_left.draw(win)
    bottom_right.draw(win)
    rect = Rectangle(top_left, bottom_right)
    rect.setFill(COLORS[random.randrange(0, 4)])
    rect.draw(win)

# draw neo-plastic on a window
def draw_neo(level, start_x, start_y, end_x, end_y, seed = 3):
    if (level > 2):
        fill_rect(start_x, end_y, end_x, start_y)
        return None

    x_cut_points = random_cut(start_x, end_x, seed)
    y_cut_points = random_cut(start_y, end_y, seed)
    for i in range(0,len(x_cut_points) - 1):
        for j in range(1, len(y_cut_points)):
            # Random selection: to fill with color or devide into smaller rectangles
            if random.randrange(0, 2) == 0:
                fill_rect(x_cut_points[i], y_cut_points[j],
                          x_cut_points[i+1], y_cut_points[j-1])
            else:
                draw_neo(level+1, x_cut_points[i], y_cut_points[j-1],
                          x_cut_points[i+1], y_cut_points[j])
                
draw_neo(1,0,0, PICWIDTH, PICHEIGHT,6)
input()