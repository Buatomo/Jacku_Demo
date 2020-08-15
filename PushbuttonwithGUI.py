import tkinter
import RPi.GPIO as GPIO
# BoxParameter  class named as BP
class bp:
    x1_base = 25
    y1_base = 25
    x2_base = 95
    y2_base = 95
    gapx_space = 25
    gapy_space = 120
    box_size = 70
    spacing = gapx_space+box_size
    push_flag = 0
    current_box = 0
    last_state = 0
class BoxClass:
    Demo = tkinter.Tk()
    canvas = tkinter.Canvas(Demo, bg="grey", height=500, width=500)
    box = canvas.create_rectangle(bp.x1_base, bp.y1_base, bp.x2_base, bp.y2_base, fill="blue")
    for i in range(1,5):
        box = canvas.create_rectangle(bp.x1_base + (i * bp.spacing), bp.y1_base, bp.x2_base + (i * bp.spacing),
                                      bp.y2_base, fill="blue")
    box = canvas.create_rectangle(bp.x1_base, bp.y1_base+bp.gapy_space, bp.x2_base, bp.y2_base+bp.gapy_space, fill="blue")
    for i in range(1,5):
        box = canvas.create_rectangle(bp.x1_base + (i * bp.spacing), bp.y1_base + bp.gapy_space, bp.x2_base + (i * bp.spacing),
                                      bp.y2_base+bp.gapy_space, fill="blue")
    canvas.pack(side = "top")


def changeColor():
    bp.push_flag ^= 1
    bp.push_flag &= 0x01

    if(bp.current_box == 0):
        if (bp.push_flag == 0):
            BoxClass.box = BoxClass.canvas.create_rectangle(bp.x1_base, bp.y1_base, bp.x2_base, bp.y2_base, fill="blue")
        elif (bp.push_flag == 1):
            BoxClass.box = BoxClass.canvas.create_rectangle(bp.x1_base, bp.y1_base, bp.x2_base, bp.y2_base, fill="red")

    elif(bp.current_box == 1):
        if (bp.push_flag == 0):
            BoxClass.box = BoxClass.canvas.create_rectangle(bp.x1_base+(bp.current_box * bp.spacing), bp.y1_base, bp.x2_base+(bp.current_box * bp.spacing), bp.y2_base, fill="blue")
        elif (bp.push_flag == 1):
            BoxClass.box = BoxClass.canvas.create_rectangle(bp.x1_base+(bp.current_box * bp.spacing), bp.y1_base, bp.x2_base+(bp.current_box * bp.spacing), bp.y2_base, fill="red")
    elif(bp.current_box == 2):
        if (bp.push_flag == 0):
            BoxClass.box = BoxClass.canvas.create_rectangle(bp.x1_base+(bp.current_box * bp.spacing), bp.y1_base, bp.x2_base+(bp.current_box * bp.spacing), bp.y2_base, fill="blue")
        elif (bp.push_flag == 1):
            BoxClass.box = BoxClass.canvas.create_rectangle(bp.x1_base+(bp.current_box * bp.spacing), bp.y1_base, bp.x2_base+(bp.current_box * bp.spacing), bp.y2_base, fill="red")
    elif(bp.current_box == 3):
        if (bp.push_flag == 0):
            BoxClass.box = BoxClass.canvas.create_rectangle(bp.x1_base+(bp.current_box * bp.spacing), bp.y1_base, bp.x2_base+(bp.current_box * bp.spacing), bp.y2_base, fill="blue")
        elif (bp.push_flag == 1):
            BoxClass.box = BoxClass.canvas.create_rectangle(bp.x1_base+(bp.current_box * bp.spacing), bp.y1_base, bp.x2_base+(bp.current_box * bp.spacing), bp.y2_base, fill="red")
    elif(bp.current_box == 4):
        if (bp.push_flag == 0):
            BoxClass.box = BoxClass.canvas.create_rectangle(bp.x1_base+(bp.current_box * bp.spacing), bp.y1_base, bp.x2_base+(bp.current_box * bp.spacing), bp.y2_base, fill="blue")
        elif (bp.push_flag == 1):
            BoxClass.box = BoxClass.canvas.create_rectangle(bp.x1_base+(bp.current_box * bp.spacing), bp.y1_base, bp.x2_base+(bp.current_box * bp.spacing), bp.y2_base, fill="red")
    # second row
    elif(bp.current_box == 5):
        if (bp.push_flag == 0):
            BoxClass.box = BoxClass.canvas.create_rectangle(bp.x1_base + (0 * bp.spacing), bp.y1_base + bp.gapy_space,
                                          bp.x2_base + (0 * bp.spacing),
                                          bp.y2_base + bp.gapy_space, fill="blue")
        elif (bp.push_flag == 1):
            BoxClass.box = BoxClass.canvas.create_rectangle(bp.x1_base + (0 * bp.spacing), bp.y1_base + bp.gapy_space,
                                          bp.x2_base + (0 * bp.spacing),
                                          bp.y2_base + bp.gapy_space, fill="red")
    elif (bp.current_box == 6):
        if (bp.push_flag == 0):
            BoxClass.box = BoxClass.canvas.create_rectangle(bp.x1_base + (1 * bp.spacing), bp.y1_base + bp.gapy_space,
                                                            bp.x2_base + (1 * bp.spacing),
                                                            bp.y2_base + bp.gapy_space, fill="blue")
        elif (bp.push_flag == 1):
            BoxClass.box = BoxClass.canvas.create_rectangle(bp.x1_base + (1 * bp.spacing), bp.y1_base + bp.gapy_space,
                                                            bp.x2_base + (1 * bp.spacing),
                                                            bp.y2_base + bp.gapy_space, fill="red")
    elif (bp.current_box == 7):
        if (bp.push_flag == 0):
            BoxClass.box = BoxClass.canvas.create_rectangle(bp.x1_base + (2 * bp.spacing), bp.y1_base + bp.gapy_space,
                                                            bp.x2_base + (2 * bp.spacing),
                                                            bp.y2_base + bp.gapy_space, fill="blue")
        elif (bp.push_flag == 1):
            BoxClass.box = BoxClass.canvas.create_rectangle(bp.x1_base + (2 * bp.spacing), bp.y1_base + bp.gapy_space,
                                                            bp.x2_base + (2 * bp.spacing),
                                                            bp.y2_base + bp.gapy_space, fill="red")
    elif (bp.current_box == 8):
        if (bp.push_flag == 0):
            BoxClass.box = BoxClass.canvas.create_rectangle(bp.x1_base + (3 * bp.spacing), bp.y1_base + bp.gapy_space,
                                                            bp.x2_base + (3 * bp.spacing),
                                                            bp.y2_base + bp.gapy_space, fill="blue")
        elif (bp.push_flag == 1):
            BoxClass.box = BoxClass.canvas.create_rectangle(bp.x1_base + (3 * bp.spacing), bp.y1_base + bp.gapy_space,
                                                            bp.x2_base + (3 * bp.spacing),
                                                            bp.y2_base + bp.gapy_space, fill="red")
    elif (bp.current_box == 9):
        if (bp.push_flag == 0):
            BoxClass.box = BoxClass.canvas.create_rectangle(bp.x1_base + (4 * bp.spacing), bp.y1_base + bp.gapy_space,
                                                            bp.x2_base + (4 * bp.spacing),
                                                            bp.y2_base + bp.gapy_space, fill="blue")
        elif (bp.push_flag == 1):
            BoxClass.box = BoxClass.canvas.create_rectangle(bp.x1_base + (4 * bp.spacing), bp.y1_base + bp.gapy_space,
                                                            bp.x2_base + (4 * bp.spacing),
                                                            bp.y2_base + bp.gapy_space, fill="red")
def changeBox():
    bp.push_flag = 0
    bp.current_box += 1
    if(bp.current_box == 10):
        bp.current_box = 0
    print(bp.push_flag)
    print(bp.current_box)
Canvas1 = BoxClass()
B  = tkinter.Button(Canvas1.Demo, text="change", command=changeColor)
B2 = tkinter.Button(Canvas1.Demo, text="move", command=changeBox)
B.pack(side = "left")
B2.pack(side = "right")
Canvas1.Demo.title("Nurse Call Demo")
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(4, GPIO.FALLING)
GPIO.add_event_callback(4, changeColor)

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(16, GPIO.FALLING)
GPIO.add_event_callback(16, changeBox)
Canvas1.Demo.mainloop()
