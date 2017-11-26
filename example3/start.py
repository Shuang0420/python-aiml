# -*- coding: utf-8 -*-

import sys
import atexit
sys.path.insert(0, "../")
import shelve

from aiml.constants import *
import aiml


template = open("cn-login.aiml", "r").readlines()

template = ''.join(template[:-2]) + '{rule}</aiml>'


category_template = """
<category>
<pattern>*</pattern>
<that>你的密码是</that>
<template>
<think><set name="password"><formal><star/></formal></set></think>
  <condition>
    <li name="password" value={password}>密码正确, 已通过验证.</li>
    <li name="password" value="">请登陆.</li>
  </condition>
</template>
</category>
"""



db = shelve.open("session.db", "c", writeback=True)

# The Kernel object is the public interface to
# the AIML interpreter.
k = aiml.Kernel(sessionStore=db)

atexit.register(lambda : k.saveBrain('brain.sav'))


# Use the 'learn' method to load the contents
# of an AIML file into the Kernel.
k.learn("cn-startup.xml")

# Use the 'respond' method to compute the response
# to a user's input string.  respond() returns
# the interpreter's response, which in this case
# we ignore.
k.respond("load aiml cn")


# Loop forever, reading user input from the command
# line and printing responses.
while True:
    if PY3:
        print(k.respond(input("> ")))
    else:
        print(k.respond(raw_input("> ")))
    db.sync()