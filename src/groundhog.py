#!/usr/bin/env python3

from statistics import *
from collections import OrderedDict
import statistics as stats
import sys
import math
import random
import operator

class Groundhog:
    def __init__(self):
        self.temp = int(0)
        self.boucle = int(0)
        self.s_deviation = float(0)
        self.t_evolution = float(0)
        self.g_increase = float(0)
        self.switch = int(0)
        self.weird = int(0)
    def switch_detector(self):
        if (len(self.temp) <= self.boucle + 1):
            return ""
        try:
            a =  round((self.temp[-1] / self.temp[-1-self.boucle] - 1) * 100)
            b =  round((self.temp[-2] / self.temp[-2-self.boucle] - 1) * 100)
        except (ValueError, FloatingPointError, ZeroDivisionError, TypeError):
            return ""
        if (abs(a+b) != abs(b)+abs(a)):
            return "\ta switch occurs"
        return ""

    def help():
        print("SYNOPSIS")
        print("\t./groundhog period")
        print("\nDESCRIPTION")
        print("\tperiod\tthe number of days defining a period")

    def standard_deviation(self):
        if (len(self.temp) > self.boucle):
            moy = sum(self.temp[-self.boucle:]) / self.boucle
            i = 0
            tot = 0
            while i != self.boucle:
                tot += (self.temp[len(self.temp) - self.boucle + i] - moy)**2
                i += 1
            self.s_deviation = format(round(math.sqrt(tot / self.boucle), 2), '0.2f')
        else:
            self.s_deviation = "nan"

    def temperature_evolution(self):
        if (len(self.temp) > self.boucle):
            a = self.temp[len(self.temp) - self.boucle - 1]
            if a == 0:
                self.t_evolution = "man"
            if a != 0:
                self.t_evolution = round(((self.temp[-1] - a) / a)* 100)
        else:
            self.t_evolution = "nan"

    def increase_average(self):
        if (len(self.temp) > self.boucle):
            g = 0
            top = 0
            count = len(self.temp) - self.boucle
            while count != len(self.temp):
                top = self.temp[count] - self.temp[count-1]
                if (top < 0):
                    top = 0
                g += top
                count += 1
            self.g_increase = format(round(g/self.boucle, 2), '0.2f')
        else:
            self.g_increase = "nan"

    def calcul_weird(self, s):
        if (len(self.temp) <= self.boucle):
            return [self.temp[-1], 0]
        size = len(self.temp)
        diff = abs(self.temp[size-1] - self.temp[size-2])
        percent = 0
        try:
            percent = diff / float(s)
        except ZeroDivisionError:
                self._g = 0
        if (percent >= 2):
            percent = 0
        return [self.temp[-1], round(percent, 2)]

    def get_weird( self, weird):
        weird.sort(key = lambda x : x[1], reverse=True)
        return weird[:5]

    def args_handle(self):
        if (len(sys.argv) != 2):
            help()
            exit (84)
        if (sys.argv[1] == "-h"):
            help()
            exit (0)
        try:
            int(sys.argv[1])
        except ValueError:
            print("That's not a number !")
            exit (84)
        a = int(sys.argv[1])
        if a <= 0:
            print("That's not a valid number !")
            exit (84)
        return a

    def printer(self):
        print("Global tendency switched " + str(self.switch) + " times")
        five_weird = self.get_weird(self.weird)
        print("5 weirdest values are [", end="")
        i = 0
        while i < 5:
            print(five_weird[i][0], end="")
            if i < 4:
                print(", ", end="")
            i += 1
        print("]")
    def start(self):
        self.boucle = self.args_handle()
        try:
            arg = input()
        except (EOFError, KeyboardInterrupt):
            exit (84)
        self.temp = []
        self.weird = []
        r = 0
        while (arg != "STOP"):
            try:
                float(arg)
            except (ValueError, TypeError):
                print("That's not a number !")
                exit (84)
            self.temp.append(float(arg))
            if (self.boucle != 0):
                self.increase_average()
                self.temperature_evolution()
                self.message = self.switch_detector()
                self.standard_deviation()
                self.weird.append(self.calcul_weird(self.s_deviation))
            else:
                self.g_increase = "man"
                self.t_evolution = "man"
                self.s_deviation = "man"
            if (self.message != ""):
                self.switch += 1
            print("g=" + str(self.g_increase) + "\tr=" + str(self.t_evolution) + "%\ts="+ str(self.s_deviation) + self.message)
            try:
                arg = input()
            except (EOFError, KeyboardInterrupt):
                exit (84)
        if (len(self.temp) <= self.boucle):
            print("Not enought numbers")
            exit(84)
        self.printer()
        return 0
