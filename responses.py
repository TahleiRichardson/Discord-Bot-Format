import random

def response(msg) ->str:

    #These can be Cphanged or Deleted

    p_msg = msg.lower()

    if p_msg == '!hello':
        return 'Hello There!'

    elif p_msg == '!roll':
        return str(random.randint(1,6))
    
    elif p_msg == '!help':
        return 'This is a message that can be changed in the future.'
    
    #Add Further Responses Here
    
