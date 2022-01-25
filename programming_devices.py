import pyautogui as pag
from time import sleep

scr_width, scr_height = pag.size()
ctr_x = scr_width/2
ctr_y = scr_height/2

buf_y = scr_height*0.15

focus_target = (ctr_x, ctr_y-buf_y)

old_app_shortcut = ['ctrl', 'alt', 'shift', '0']
new_app_shortcut = ['ctrl', 'alt', 'shift', '9']
app_load_time = 2

break_list = ['quit', 'q', 'exit', 'x']


def launch_enter_old_tool():
    pag.hotkey(*old_app_shortcut)
    sleep(6)
    pag.click(focus_target)
    pag.hotkey('shift', 'tab')
    pag.hotkey('shift', 'tab')
    pag.hotkey('backspace')
    pag.typewrite('password', 0.01)
    pag.typewrite(['tab', 'tab', 'space'], 0.05)
    sleep(2)

def program_old_tool():
    pag.hotkey('ctrl', 'l')
    sleep(0.5)
    pag.typewrite("AT+GTSRI=password,4,,1,udp.companylistener.com,10002,,0,,0,0,0,,,,FFFF$", 0.01)
    pag.hotkey('enter')
    sleep(2)
    pag.hotkey('alt', 'f4')
    pag.hotkey('alt', 'f4')
    pag.hotkey('alt', 'f4')
#    sleep(1)

def launch_enter_new_tool():
    pag.hotkey(*new_app_shortcut)
    sleep(app_load_time+1)
    pag.click(focus_target)
    pag.hotkey('shift', 'tab')
    pag.hotkey('shift', 'tab')
    pag.hotkey('shift', 'tab')
    pag.hotkey('home')
    pag.typewrite(['tab', 'tab', 'tab', 'space'], 0.05)
    sleep(1)

def program_new_tool():
    pag.hotkey('ctrl', 'l')
    sleep(0.5)
    pag.typewrite("AT+GTRES=password,2,device,1,0.0.0.0,10029,,,1,7F9F,,0,,0,30,,FFFF$", 0.01)
    pag.hotkey('enter')
    sleep(2)
    pag.hotkey('alt', 'f4')
    pag.hotkey('alt', 'f4')
    sleep(1)

if __name__ == "__main__":
    while True:
        s = input("Enter (or q to quit) --> ")
        if s in break_list:
            break
        launch_enter_old_tool()
        program_old_tool()
        launch_enter_new_tool()
        program_new_tool()