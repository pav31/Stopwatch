# template for "Stopwatch: The Game"
import simplegui
import random


interval = 100

success_msg = msg_init = "Try to stop at .0 ms"
msg_missed = ["Not very lucky...", "Keep trying ;)", "Ouch!", "Missed!","Nope...", "Maybe next time..."]
msg_alot = ["You are pretty stubborn ;)", "Not tired yet?", "It's just not your day...", "C'mon man....seriously?", "*@$#"]
msg_hit = ["GREAT SUCCESS!!!", "Very nice!", "WaWaWeeWa!!!", "It's a hit!", "Bravo!", "Bravissimo!!!", "I like!", "High five!", "Lucky B)"]
color = color_init = "Blue"


def format(t):
    '''
    Converts time in tenths of seconds into formatted string A:BC.D.
    Works correctly upto 60 minutes
    >>> format(0)
    0:00.0
    >>> print format(71999)
    59:59.9
    >>> print format(72000)
    0:00.0
    '''
    global mins, sec, msec
    mins = str(t // 600 % 60)
    sec = str(t // 10 % 60)
    msec = str(t % 10)
    if len(sec) < 2:
        sec = "0" + sec
    return  mins + ":" + sec + "." + msec


def start():
    '''Start timer button'''
    timer.start()


def stop():
    '''Stops the timer and calls update_score function'''
    if timer.is_running():
        timer.stop()
        update_score()


def reset():
    '''Stops the timer and sets time, hits and tries to 0.'''
    global time, hits, tries, success_msg, color
    color = color_init
    success_msg = msg_init
    timer.stop()
    time =  hits = tries = 0


def update_score():
    '''
    Updates the number of tries.
    Adds to hits if stopped on a whole second (1.0, 2.0, 3.0, etc.)
    '''
    global hits, tries, success_msg, color
    tries += 1
    msg = msg_missed
    color = "Red"
    if tries > 10:
        msg = msg_alot
    if time % 10 == 0:
        hits += 1
        msg = msg_hit
        color = "Green"

    # Pick random msg form msg_missed or msg_hit
    idx = random.randrange(len(msg))
    success_msg = msg[idx]



def hit_rate():
    '''Returns success rate, %'''
    if hits > 0:
        rate = hits * 100 / tries
    else:
       rate = 0
    return "Success rate: %d%" %rate


def print_score():
    '''Return the score in format hits/tries'''
    return str(hits) + "/" + str(tries)


def timer():
    global time
    time += 1

def draw(canvas):
    # Green box
    for x in range(110,183):
        canvas.draw_line((40, x), (260, x), 0.5, 'Green')
    # frame around stopwatch
    canvas.draw_line((10, 100), (290, 100), 2, 'Black')
    canvas.draw_line((10, 190), (290, 190), 2, 'Black')
    canvas.draw_line((30, 110), (30, 180), 1, 'Black')
    canvas.draw_line((270, 110), (270, 180), 1, 'Black')
    canvas.draw_line((10, 100), (30, 110), 1, 'Black')
    canvas.draw_line((10, 190), (30, 180), 1, 'Black')
    canvas.draw_line((290, 100), (270, 110), 1, 'Black')
    canvas.draw_line((290, 190), (270, 180), 1, 'Black')
    # stopwatch A:BB.C
    canvas.draw_text(format(time), (60, 170), 70, "White")
    #score x/y
    canvas.draw_text(print_score(), (250,40), 20, "Blue")
    # Success rate, %
    canvas.draw_text(hit_rate(), (10,40), 20, "Green")
    canvas.draw_text(success_msg.center(50), (0,250), 20, color)


frame = simplegui.create_frame('Stopwatch', 300, 300)
frame.set_canvas_background("White")
frame.set_draw_handler(draw)

timer = simplegui.create_timer(interval, timer)

frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)

reset()

frame.start()