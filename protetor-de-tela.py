from os import system
import datetime
from time import sleep

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def cls(n = 0):
    if n == 0:
        print("\033c")
    else:
        print('\b'*n)

max_char = 80
i = 0

def standby():
    global i
    while 1:
        tempo = datetime.datetime.now()
        try:        
                
                if not i > 80:
                    print(bcolors.OKBLUE+' '*(80-i)+'*'+bcolors.ENDC)
                    
                elif not i>160:
                    print(bcolors.OKCYAN+' '*(160-i)+'.'+bcolors.ENDC)
                    
                if 19 > i:
                    print(bcolors.OKGREEN+' '*(19-i)+'o'+bcolors.ENDC)
                elif i < 98:
                    print(bcolors.OKBLUE+' '*(98-i)+'.'+bcolors.ENDC)
                else:
                    print(bcolors.OKGREEN+' '*(177-i)+'o'+bcolors.ENDC)
                
                if 40 > i:
                    print(bcolors.OKBLUE+' '*(40-i)+'-'+bcolors.ENDC)
                elif i < 119:
                    print(bcolors.OKGREEN+' '*(119-i)+'*'+bcolors.ENDC)
                else:
                    print(bcolors.OKBLUE+' '*(198-i)+'-'+bcolors.ENDC)

                if 62 > i:
                    print(bcolors.FAIL+' '*(62-i)+'.'+bcolors.ENDC)
                elif i < 141:
                    print(bcolors.FAIL+' '*(141-i)+'*'+bcolors.ENDC)
                else:
                    print(bcolors.FAIL+' '*(220-i)+'.'+bcolors.ENDC)

                if 52 > i:
                    print(' '*(52-i)+'-')
                elif i < 131:
                    print(bcolors.OKCYAN+' '*(131-i)+'Ø'+bcolors.ENDC)
                else:
                    print(' '*(210-i)+'-')

                if 21 > i:
                    print(bcolors.FAIL+' '*(21-i)+'*'+bcolors.ENDC)
                elif i < 100:
                    print(' '*(100-i)+'-')
                else:
                    print(bcolors.FAIL+' '*(179-i)+'*'+bcolors.ENDC)

                if 65 > i:
                    print(bcolors.OKCYAN+' '*(65-i)+'.'+bcolors.ENDC)
                elif 144 > i:
                    print(bcolors.WARNING+' '*(144-i)+'-'+bcolors.ENDC)
                else:
                    print(bcolors.OKCYAN+' '*(223-i)+'.'+bcolors.ENDC)

                if (i%2) == 0:
                    print(bcolors.OKGREEN+' '*32+'Standby Mode: ON'+' '*32+bcolors.ENDC)
                    print(' '*36+str(tempo.hour) +'   '+str(tempo.minute)+' '*36)
                elif (i%2) == 1:
                    print(bcolors.OKGREEN+' '*31+'>Standby Mode: ON<'+' '*31+bcolors.ENDC)
                    print(' '*36+str(tempo.hour) +' : '+str(tempo.minute)+' '*36)

                sleep(0.01)
                cls()

                i+=1                

                if i >= 160:
                    i=0

        except KeyboardInterrupt:
            system('cls')
            print('\n'*7)
            print(bcolors.FAIL+' '*32+'Standby Mode: OFF'+' '*30+bcolors.ENDC)
            stop()
            break


def stop():
    while 1:
        try:
            a = 1
            a + 1
            a - 1       
        except KeyboardInterrupt:
            standby()
            break

standby()