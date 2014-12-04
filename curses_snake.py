#!/usr/bin/env python

#up is 259
#left is 260
#right is 261
#down is 258
#timeout is -1

import curses
import curses.wrapper

from random import randint
from time import sleep
from math import exp

def snakeLoop(stdscr):
    stdscr.nodelay(1)
    curses.curs_set(0)
    
    ylim, xlim = stdscr.getmaxyx()
    
    x = xlim/2
    y = ylim/2
    
    snakey = [y]
    snakex = [x]
    
    lastdir = 259
    
    doty, dotx = newDot(stdscr, ylim, xlim, snakey, snakex)
    
    timedenom = 10.
    
    while True:
        
        c = stdscr.getch()
        if not 258 <= c <= 261:
            c = lastdir
        if c == 259: # up
            y -= 1
        elif c == 260: # left
            x -= 1
        elif c == 261: # right
            x += 1
        elif c == 258: # down
            y += 1
        lastdir = c
        
        if (x < 0) or (x >= xlim) or (y < 0) or (y >= ylim) or snakeHere(y,x,snakey,snakex):
            stdscr.addstr(0,0,"You Lose")
            stdscr.refresh()
            stdscr.nodelay(0)
            stdscr.getch()
            quit();

        snakey.append(y)
        snakex.append(x)
        stdscr.addstr(y, x, 'O')
        
        if y == doty and x == dotx:
            doty, dotx = newDot(stdscr, ylim, xlim, snakey, snakex)
        else:
            lasty = snakey[0]
            lastx = snakex[0]
            snakey = snakey[1:]
            snakex = snakex[1:]
            stdscr.addstr(lasty, lastx, ' ')
             
     
        stdscr.refresh()
        sleep(exp(1/timedenom)-1)
        timedenom += .001

def newDot(stdscr, maxy, maxx, snakey, snakex):
    while True:
        conflict = True
        newy = randint(0,maxy-1)
        newx = randint(0,maxx-1)
        if not snakeHere(newy, newx, snakey, snakex):
            stdscr.addstr(newy, newx, 'x')
            return (newy, newx)

def snakeHere(y, x, snakey, snakex):
    lasthit = 0
    while True:
        try: 
            yind = snakey.index(y, lasthit)
            lasthit = yind+1
            if snakex[yind] == x:
                return True
        except ValueError:
            return False    
    
if __name__ == '__main__':
    curses.wrapper(snakeLoop)

