import curses
from curses import wrapper
import time
from random import choice

class WPM_Typing_Test:
    def start_scrn(self, stdscr):
        stdscr.clear()
        stdscr.addstr("Welcome to Speed Typing Test!")
        stdscr.addstr("\nPress any key to start typing!")
        stdscr.addstr("\nTo close the app in while runing please pess ESC key.")
        stdscr.refresh()
        stdscr.getkey()

    def display_input(self, stdscr, target, currnt, wpm = 0):
        stdscr.addstr(target)
        stdscr.addstr(1, 0, f"WPM :- {wpm}")

        for i, char in enumerate(currnt):
            color = curses.color_pair(2)
            correct_char = target[i]
            if char != correct_char:
                color = curses.color_pair(3)
            stdscr.addstr(0, i, char, color)


    def wpm_tester(self, stdscr):
        target = choice(["Hello World this is some test text for this app.", "The quick brown fox jumps over the lazy dog.", "She sells seashells by the seashore.", "A journey of a thousand miles begins with a single step.", "In the midst of chaos, there is also opportunity."])
        currnt = []
        wpm = 0
        start_time = time.time()
        stdscr.nodelay(True)

        while True:
            time_elapsed = max(time.time() - start_time, 1)
            wpm = round((len(currnt)/(time_elapsed/60))/5)
            stdscr.clear()
            self.display_input(stdscr, target, currnt, wpm)
            
            if len(currnt) == len(target):
                stdscr.nodelay(False)
                break

            try:
                key = stdscr.getkey()
            except:
                continue

            if ord(key) == 27:
                break
            
            if key in ('KEY_BACKSPACE', '\b', '\x7f'):
                if len(currnt) > 0:
                    currnt.pop()
            elif len(currnt) < len(target):
                currnt.append(key)
        return wpm       
    


    def main(self, stdscr):
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
        self.start_scrn(stdscr)
        while True:
            wpm = self.wpm_tester(stdscr)
            stdscr.addstr(2, 0, f"Your WPM Typing test score is {wpm}")
            stdscr.addstr(3, 0, "Press any key to continue playing and q to quit the app!: ")
            key = stdscr.getkey().lower()
            if key == 'q':
                break
        
if __name__ == "__main__":
    code = WPM_Typing_Test()
    wrapper(code.main)