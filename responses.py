import re

list_message=[]

def reset_message():
    list_message.clear()

def get_response(message):
    list_message.append(message)
    return list_message

# Test your system
# get_response('What is your name bruv?')
# get_response('Can you help me with something please?')