# This is program for unwrapping a curve I drew for a scrolled flare pattern.
# It unwraps the spatial dimension defined by the curve and this becomes the y axis. 
# The x axis from the sketch becomes the radius of the prism
# One tenth of the circumference is plotted so that a pattern piece can be created

import math

measurements = [
    [0, -2],
    [30, 0],
    [80, 5],
    [110, 10],
    [130, 15],
    [155, 25],
    [163, 30],
    [170, 35],
    [177, 40],
    [184, 45],
    [190, 50],
    [196, 55],
    [201, 60],
    [207, 65],
    [210, 70],
    [215, 75],
    [222, 80],
    [227, 85],
    [235, 90],
    [258, 95],
    [275, 90],
    [285, 85],
    [291, 80],
    [296, 75],
    [301, 70],
    [306, 65],
    [311, 60],
    [315, 55],
    [320, 50],
    [325, 45],
    [330, 40],
    [335, 35],
    [341, 30],
    [348, 25],
    [356, 20],
    [365, 15]
]




previous = [0,0]
points = []
for heightDownwards, x in measurements:
    radius = x + 85
    circumference = 2 * math.pi * radius
    tenthCircumference= circumference * .1
    points.append(tenthCircumference)
    points.append(heightDownwards)

print (points)


# plot the graph


import drawSvg as draw

d = draw.Drawing(500, 1000, origin='center',  stroke='black', fill='none')
d.append(draw.Lines(*points, close=False))


def pairwise(iterable):
    "s -> (s0, s1), (s2, s3), (s4, s5), ..."
    a = iter(iterable)
    return zip(a, a)

for x, y in pairwise(points):
    d.append(draw.Circle(x, y, 1, fill="black"))
    d.append(draw.Text("{:.0f}mm".format(x), 5, x+5,y, stroke="none", fill="#000000"))
    d.append(draw.Line(0, y, x, y, stroke_width=.1))
    d.append(draw.Text("{:.0f}mm".format(y), 5, 5, y - 6, stroke="none", fill="#000000"))


top = 0
bottom = points[-1]
print(bottom)

d.append(draw.Lines( *points[:2],0,0, 0, bottom, *points[-2:], stroke="black"))


def drawScale(sx, sy, ex, ey, interval): 
    stuff = draw.Group()


    # draw the ruler
    ruler = draw.Line(sx, sy, ex, ey)
    stuff.append(ruler)

    rulerLength = math.sqrt(pow(sx-ex, 2) + pow(sy-ey, 2))
    print("rulerLength", rulerLength)
    unit = [(ex-sx)/rulerLength , (ey-sy)/rulerLength ]
    perp = [unit[1], -unit[0]]

    # draw the markings
    z = 0
    x = sx
    y = sy
    while z < rulerLength:
        x1 = x + perp[0] * 3
        y1 = y + perp[1] * 3
        stuff.append(draw.Line(x,y, x1, y1))
        stuff.append(draw.Text("{:.0f}mm".format(z), 5, x + perp[0]*5, y + perp[1]*5, stroke="none", fill="black"))

        print (x, y)
        z += interval
        x += unit[0] * interval
        y += unit[1] * interval
    return stuff

    

d.append(drawScale(200, 0, 200, 300, interval=100))

d.saveSvg('pattern piece (one fifth).svg')

