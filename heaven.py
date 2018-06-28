import cs1graphics as cg

paper = cg.Canvas()
paper.setBackgroundColor('skyBlue')
paper.setWidth(800)
paper.setHeight(600)
paper.setTitle('Heaven')

# The Sun!
sun = cg.Circle()
paper.add(sun)
sun.setFillColor("orange")
sun.moveTo(800, 0)
sun.setRadius(300)
sun.setBorderWidth(0)

# The House!
facade = cg.Square(200, cg.Point(400, 350))
facade.setFillColor('white')
paper.add(facade)

# The Tree!
tree = cg.Polygon(cg.Point(150, 220), cg.Point(120, 380), cg.Point(180, 380))
tree.setFillColor('darkGreen')
paper.add(tree)

# The Chimney!
chimney = cg.Rectangle(50, 70, cg.Point(450, 215))
chimney.setFillColor('red')
paper.add(chimney)

# The Grass!
grass = cg.Rectangle(800, 300, cg.Point(400, 550))
grass.setFillColor('darkGreen')
grass.setBorderColor('darkGreen')
grass.setDepth(75)
# must be behind house and tree
paper.add(grass)

# The Roof!
roof = cg.Polygon(cg.Point(300, 220),
                  cg.Point(500, 220),
                  cg.Point(525, 250),
                  cg.Point(275, 250))
roof.setFillColor('gray')
paper.add(roof)
