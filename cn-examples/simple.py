import aiml
import os
import sys

PY3 = sys.version_info[0] == 3

k = aiml.Kernel()

# for chinese
k.bootstrap(learnFiles="cn-startup.xml", commands="load aiml cn")

# if python 2
# while True: print(k.respond(raw_input("> ")))
# if python 3
while True: 
    if PY3:
        print(k.respond(input("> ")))
    else:
        print(k.respond(raw_input("> ")))