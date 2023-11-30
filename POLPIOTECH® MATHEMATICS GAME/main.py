from random import randint
from os import system, close
from time import sleep
from termcolor import cprint


class Math():
    def subtraction(self):
        v1 = int(input("ENTER FIRST RANGE FOR VARIBLE: "))
        v2 = int(input("ENTER SECOND RANGE FOR VARIBLE: "))
        r = int(input("ENTER NUMBER OF ROUNDS: "))
        system("clear")
        cprint(" -- MATHEMATICAL OPERATION --", "white", "on_blue")
        print()
        for i in range(r):
            a = randint(v1, v2)
            b = randint(v1, v2)
            if b < 0:
                answer = int(input(str(a)+"-"+"("+str(b)+")"+"="))
            else:
                answer = int(input(str(a)+"-"+str(b)+"="))
            if a-b == answer:
                cprint("True answer!", "green")
                sleep(2)
                print()
            else:
                cprint("False answer!", "red")
                sleep(2)
                print()

    def addition(self):
        v1 = int(input("ENTER FIRST RANGE FOR VARIBLE: "))
        v2 = int(input("ENTER SECOND RANGE FOR VARIBLE: "))
        r = int(input("ENTER NUMBER OF ROUNDS: "))
        system("clear")
        cprint(" -- MATHEMATICAL OPERATION --", "white", "on_blue")
        print()
        for i in range(r):
            a = randint(v1, v2)
            b = randint(v1, v2)
            if b < 0:
                answer = int(input(str(a)+"+"+"("+str(b)+")"+"="))
            else:
                answer = int(input(str(a)+"+"+str(b)+"="))
            if a+b == answer:
                cprint("True answer!", "green")
                sleep(2)
                print()
            else:
                cprint("False answer!", "red")
                sleep(2)
                print()

try:
    function = Math()
    system("clear")
    cprint("         POLPIOTECH®        ", "black", "on_white")
    cprint("   -- MATHEMATICS GAME --   ", "white", "on_blue")
    cprint("   ─────█─▄▀█──█▀▄─█─────   ", "black", "on_white")
    cprint("   ────▐▌──────────▐▌────   ", "black", "on_white")
    cprint("   ────█▌▀▄──▄▄──▄▀▐█────   ", "black", "on_white")
    cprint("   ───▐██──▀▀──▀▀──██▌───   ", "black", "on_white")
    cprint("   ──▄████▄──▐▌──▄████▄──   ", "black", "on_white")
    cprint("  -- I LOOKING FOR YOU! --  ", "white", "on_blue")
    print()
    print("WHAT DO YOU WANT TO CHOOSE?")
    print("=="*14)
    print(" (1) Subtraction.")
    print(" (2) Addition.")
    print(" (0) Exit.")
    print("=="*14)
    choice = int(input("YOUR CHOICE: "))
    if choice == 1:
        system("clear")
        cprint("         POLPIOTECH®        ", "black", "on_white")
        cprint("   -- MATHEMATICS GAME --   ", "white", "on_blue")
        cprint("   ─────█─▄▀█──█▀▄─█─────   ", "black", "on_white")
        cprint("   ────▐▌──────────▐▌────   ", "black", "on_white")
        cprint("   ────█▌▀▄──▄▄──▄▀▐█────   ", "black", "on_white")
        cprint("   ───▐██──▀▀──▀▀──██▌───   ", "black", "on_white")
        cprint("   ──▄████▄──▐▌──▄████▄──   ", "black", "on_white")
        cprint("      -- Subtraction --     ", "white", "on_blue")
        print()
        function.subtraction()
        system("clear")
        system("python3 main.py")
    elif choice == 2:
        system("clear")
        cprint("         POLPIOTECH®        ", "black", "on_white")
        cprint("   -- MATHEMATICS GAME --   ", "white", "on_blue")
        cprint("   ─────█─▄▀█──█▀▄─█─────   ", "black", "on_white")
        cprint("   ────▐▌──────────▐▌────   ", "black", "on_white")
        cprint("   ────█▌▀▄──▄▄──▄▀▐█────   ", "black", "on_white")
        cprint("   ───▐██──▀▀──▀▀──██▌───   ", "black", "on_white")
        cprint("   ──▄████▄──▐▌──▄████▄──   ", "black", "on_white")
        cprint("       -- Addition --       ", "white", "on_blue")
        print()
        function.addition()
        system("clear")
        system("python3 main.py")
    elif choice == 0:
        system("clear")
        close(0)
        system("clear")
        cprint("         POLPIOTECH®        ", "black", "on_white")
        cprint("   -- MATHEMATICS GAME --   ", "white", "on_blue")
        cprint("   ─────█─▄▀█──█▀▄─█─────   ", "black", "on_white")
        cprint("   ────▐▌──────────▐▌────   ", "black", "on_white")
        cprint("   ────█▌▀▄──▄▄──▄▀▐█────   ", "black", "on_white")
        cprint("   ───▐██──▀▀──▀▀──██▌───   ", "black", "on_white")
        cprint("   ──▄████▄──▐▌──▄████▄──   ", "black", "on_white")
        cprint("       -- GAME OVER --      ", "white", "on_blue")
        print()
    else:
        system("clear")
        system("python3 main.py")
except ValueError:
    print()
    cprint("INCORECT VALUE!", "red")
    sleep(4)
    for i in range(101):
        print("\rRELOADING {}%".format(i), end="")
        sleep(0.03)
    system("python3 main.py")
except TypeError:
    print()
    cprint("INCORET TYPE! VARIABLE!")
    sleep(4)
    for i in range(101):
        print("\rRELOADING {}%".format(i), end="")
        sleep(0.03)
    system("python3 main.py")
except Exception as otherExcepts:
    print()
    print(f"AN ERROR HAS OCCURED {otherExcepts}", "red")
    sleep(4)
    for i in range(101):
        print("\rRELOADING {}%".format(i), end="")
        sleep(0.03)
    system("python3 main.py")