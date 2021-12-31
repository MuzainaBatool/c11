import turtle
dict={'shape':'square','size':100,'angle':90,'color':'pink'}
for i in range(4):
    turtle.pencolor(dict['color'])
    turtle.shape(dict['shape'])
    turtle.forward(dict['size'])
    turtle.left(dict['angle'])
                     
                   

