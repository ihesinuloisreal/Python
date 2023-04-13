import math

def paint_calc(height, width, cover):
    answer = (height * width) / cover
    print(f"You will need {math.ceil(answer)} can of paints")

test_h = int(input("Height of the wall: "))
test_w = int(input("width of the wall: "))
coverage = 5
paint_calc(height = test_h, width = test_w, cover = coverage)