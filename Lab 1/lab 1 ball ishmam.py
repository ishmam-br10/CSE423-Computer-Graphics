from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

window_width = 500
window_height = 500

balls = []
speed = random.randint(1,5)
ball_size = random.randint(4,8)
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
        self.ball_size = random.randint(4,8)
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
