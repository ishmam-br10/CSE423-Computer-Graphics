# House 


from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

window_width = 900
window_height = 900

rain_speed = 7
raindrops_number = 2000
raindrops = []

# randomly raindrop banabo jekhane amar length iccha moto dhorbo
for i in range(raindrops_number):
    x_points = random.randint(-window_width, window_width) # pura screen er moddhe ekta point nite koitesi
    y_points = random.randint(100, window_height // 2) #random y points between 100 and 800 //2
    drop_size = random.randint(5, 8) # 10-13 er moddhe ekta size er raindrop nibe
    # ja ja korsi segula save korbo ekta list e 
    raindrops.append((x_points, y_points, drop_size))

bend_to_wind = 0 # batas er sathe direction chandge
# lal . nil, sobuj ar saturation
r = 0.0
g = 0.0
b = 0.0
s = 0.0

# background color er state ar saturation
background_colors = [r, g, b, s]
current_color = 0

class point:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
        # setting all the co ordinate points

def convert_coordinate(x, y):
    global window_width, window_height
    a = x - (window_width / 2)
    b = (window_height /2) - y
    return a,b

def draw_points(x, y, s):
    glPointSize(s)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def drawShapes():
    scale = 0.25
    glLineWidth(4)
    # chad
    glBegin(GL_TRIANGLES)
    glColor3d(0, 1, 0)
    glVertex2f(5 * scale, 200 * scale)
    glVertex2f(-250 * scale, 5 * scale)
    glVertex2f(250 * scale, 5 * scale)
    glEnd()

    # deyal
    glColor3f(0, 0.4, 1)
    glBegin(GL_LINES)
    glVertex2f(-250 * scale, 5 * scale)
    glVertex2f(-250 * scale, -250 * scale)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-250 * scale, -250 * scale)
    glVertex2f(250 * scale, -250 * scale)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(250 * scale, -250 * scale)
    glVertex2f(250 * scale, 5 * scale)
    glEnd()

    # Doroja
    glColor3f(0, 0.4, 1)
    glBegin(GL_LINES)
    glVertex2f(-80 * scale, -250 * scale)
    glVertex2f(-80 * scale, -100 * scale)

    glVertex2f(-80 * scale, -100 * scale)
    glVertex2f(10 * scale, -100 * scale)

    glVertex2f(10 * scale, -100 * scale)
    glVertex2f(10 * scale, -250 * scale)

    glVertex2f(10 * scale, -250 * scale)
    glVertex2f(-80 * scale, -250 * scale)
    glEnd()

    # Doroja knob
    glColor3f(1.0, 0, 0.0)
    glPointSize(10)
    glBegin(GL_POINTS)
    glVertex2f(-20 * scale, -175 * scale)
    glEnd()

    # janala
    glColor3d(0, 0.4, 1)
    # glBegin(GL_LINES)
    # glVertex2f(100 * scale, -185 * scale)
    # glVertex2f(100 * scale, -80 * scale)

    # glVertex2f(100 * scale, -80 * scale)
    # glVertex2f(220 * scale, -80 * scale)

    # glVertex2f(220 * scale, -80 * scale)
    # glVertex2f(220 * scale, -185 * scale)

    # glVertex2f(220 * scale, -185 * scale)
    # glVertex2f(100 * scale, -185 * scale)
    glBegin(GL_QUADS)  # Start drawing a quadrilateral (filled shape)
    glVertex2f(100 * scale, -185 * scale)  # Bottom-left corner
    glVertex2f(220 * scale, -185 * scale)  # Bottom-right corner
    glVertex2f(220 * scale, -80 * scale)   # Top-right corner
    glVertex2f(100 * scale, -80 * scale)   # Top-left corner

    glEnd()

def draw_rain():
    glColor3f(0.0, 0.0, 1.0) # blue rain
    glLineWidth(1.5)
    glBegin(GL_LINES)
    # x, y er value raindrops theke iterate kora lagbe
    for x,y, size in raindrops:
        glVertex(x, y)
        glVertex2f(x + bend_to_wind, y- size) # end point
    glEnd()

def keyboardListener(key, x, y):
    glutPostRedisplay()

def specialKeyListener(key, x, y):
    global bend_to_wind, background_colors
    if key == GLUT_KEY_RIGHT:
        bend_to_wind += 1
        print("Bending towards right")
    elif key == GLUT_KEY_LEFT:
        bend_to_wind -= 1
        print("bending to the left")
    # background color 1 hoye gele ei condition e ar dhukbe na 
    elif key == GLUT_KEY_UP and 0<= background_colors[0] < 1:
        background_colors[0] += 0.5
        background_colors[1] += 0.5
        background_colors[2] += 0.5
        print(background_colors)
        if 0<= background_colors[0] <= 1:
            print(f"Background Colour Now: {background_colors[current_color]}")
            glClearColor(*tuple(background_colors))
    
    # 1 hooye gele user ke bole dibo je ar bright hobe na 
    elif  key == GLUT_KEY_UP and background_colors[0] == 1:
        print("Cannot Make brighter")

    # background color shunno hoye gele ei condition e ar dhukbe na 
    elif key == GLUT_KEY_DOWN and 0< background_colors[0] <= 1:
        background_colors[0] -= 0.5
        background_colors[1] -= 0.5
        background_colors[2] -= 0.5
        print(background_colors)
        if 0<= background_colors[0] <= 1:
            print(f"Background Colour Now: {background_colors[current_color]}")
            glClearColor(*tuple(background_colors))
    
    elif  key == GLUT_KEY_DOWN and background_colors[0] == 0:
        print("Cannot Make dimmer")
    glutPostRedisplay()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 0, 200, 0, 0, 0, 0, 1, 0)
    # glOrtho(-900, 900, -900, 900, 0.0, 1.0)
    draw_rain()
    drawShapes()

    glutSwapBuffers()


def animate():
    glutPostRedisplay()
    global raindrops
    for i in range(len(raindrops)):
        x, y, size = raindrops[i]
        x += bend_to_wind
        y -= rain_speed

        if y< 30: # rain drop house corss korle
            # resetting the value of x and y
            y = window_height // 2
            x = random.randint(-window_width, window_width)
        
        if y < -window_height // 2:
            y = window_height // 2
            x = random.randint(-window_width, window_width)
        
        if x > window_width :
            x = -window_width
        elif x < -window_width:
            x = window_width
        raindrops[i] = (x, y, size)



def init():
    global wind
    glutInit()
    glutInitWindowSize(window_width, window_height)
    glutInitWindowPosition(100, 100)
    glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)
    wind = glutCreateWindow(b"Rain and Home")
    glClearColor(*tuple(background_colors))
    glutDisplayFunc(display)
    glutIdleFunc(animate)
    glutKeyboardFunc(keyboardListener)
    glutSpecialFunc(specialKeyListener)
    # glutMouseFunc(mouseListener)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # gluPerspective(104, 1, 1, 1000.0)
    gluPerspective(45, 1, 1, 1000.0)


init()
glutMainLoop()



# Ball 

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

window_width = 500
window_height = 500

balls = []
speed = 5
ball_size = 7
func_flag = True # Ball douracche kina tai dekhtesi
blink = False

class point:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        dirn = random.choice([(-1, 1), (-1, -1), (1, 1), (1, -1)])
        self.dx = dirn[0]*speed
        self.dy = dirn[1]*speed
        # iccha moto colour
        self.color = (random.random(), random.random(), random.random())
        self.ball_size = ball_size
        self.temp_color = None



def convert_coordinate(x, y):
    global window_width, window_height
    a = x - (window_width / 2)
    b = (window_height / 2) - y
    return a, b

def draw_points(ball):
    glPointSize(ball.ball_size)
    glBegin(GL_POINTS)
    glColor3f(ball.color[0], ball.color[1], ball.color[2])
    glVertex2f(ball.x, ball.y)
    glEnd()

def keyboardListener(key, x, y):
    global ball_size
    if key == b" ":
        # press space bar to thamano
        global func_flag
        if func_flag == False:
            func_flag = True
            print("Function Flag Set to True, Animation Resume")
        else:
            func_flag = False
            print("Function Flag set to False, The animation has stopped")

    glutPostRedisplay()

def specialKeyListener(key, x, y):
    global func_flag
    if func_flag == False:
        print("There is no animation Right Now")
        return
    global speed
    if key == GLUT_KEY_UP:
        speed += 0.5
        for ball in balls:
            ball.dx = (ball.dx / abs(ball.dx)) * speed
            ball.dx = (ball.dy / abs(ball.dy)) * speed
        print(f"balls speed increased, current speed is {speed}")
    
    if key == GLUT_KEY_DOWN:
        speed -= 0.5
        if speed > 0:
            for ball in balls:
                ball.dx = (ball.dx / abs(ball.dx)) * speed # bujhte hobe line ta
                ball.dy = (ball.dy / abs(ball.dy)) * speed
            print(f"balls speed decreased, current speed is {speed}")
        else:
            speed = 5
            print(f"Speed was too low to do your intended operation, currently speed set to {speed}")

def toogle_blink(value):
    global blink
    if blink == False:
        for ball in balls:
            if ball.temp_color:
                ball.color = ball.temp_color # going back to temp
        return
    
    if value == 0:
        for ball in balls:
            ball.temp_color = ball.color
            ball.color = (0, 0, 0)
        # 1 second for shift
        glutTimerFunc(1000, toogle_blink, 1) 
    if value == 1:
        for ball in balls:
            ball.color = ball.temp_color
        
        if blink:
            glutTimerFunc(1000, toogle_blink, 0)
    glutPostRedisplay()


def mouseListener(button, state, x, y):
    global func_flag
    global speed
    global blink

    if func_flag == False:
        print("Function flag is set to False")
        return
    
    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        print(x, y)
        conv_x, conv_y = convert_coordinate(x, y)
        ball_new = Ball(conv_x, conv_y)
        direction = random.choice([(-1, 1), (-1, -1), (1, 1), (1, -1)])
        ball_new.dx = direction[0] * speed
        ball_new.dy = direction[1] * speed
        balls.append(ball_new)
    glutPostRedisplay()

    # left button
    if button == GLUT_LEFT_BUTTON: 
        if state == GLUT_DOWN:
            blink = True
            glutTimerFunc(0, toogle_blink, 0)
        elif state == GLUT_UP:
            blink = False
            for ball in balls:
                if ball.temp_color:
                    ball.color = ball.temp_color
        
        print(f"Blink state =  {blink}")
    glutPostRedisplay()


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0, 0, 0, 0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 0, 200, 0, 0, 0, 0, 1, 0)
    for ball in balls:
        draw_points(ball)
    # drawShapes()
    glutSwapBuffers()

def animate():
    glutPostRedisplay()
    global func_flag
    if func_flag==False:
        return
    for ball in balls:
        ball.x += ball.dx
        ball.y += ball.dy
        if ball.x <= -window_width / 2 or ball.x >= window_width / 2: 
            # ball.dx = window_width / 2
            ball.dx = -ball.dx
        if ball.y <= -window_height / 2 or ball.y >= window_height / 2: 
            # ball.y = window_height /2
            ball.dy = -ball.dy
        # ball.x += ball.dx
        # ball.y += ball.dy

def init():
    glClearColor(0, 0, 0, 0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(104, 1, 1, 1000.0)

glutInit()
glutInitWindowSize(window_width, window_height)
glutInitWindowPosition(100, 150)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)

wind = glutCreateWindow(b"Ball douracche")
init()

glutDisplayFunc(display)
glutIdleFunc(animate)
glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseListener)

glutMainLoop()
