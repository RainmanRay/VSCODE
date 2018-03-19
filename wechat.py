import itchat
from itchat.content import TEXT

@itchat.msg_register(TEXT)
def reply(msg):
    dir(msg)
    itchat.send('I have recieved you message, may you have a good day!', toUserName='filehelper')
    return('i received: {}'.format(msg['Text']))

# @itchat.msg_register(TEXT,isFriendChat=True)
# def text_reply(msg):
#     msg.user.send('{} {}'.format(msg.type,msg.text))



itchat.auto_login(hotReload=True)
# itchat.send('I have recieved you message, may you have a good day!', toUserName='filehelper')
itchat.run()

#
# import itchat
# from itchat.content import *
#
# itchat.auto_login(hotReload=True)
#
# @itchat.msg_register
# def general_reply(msg):
#     return('I received a %s' % msg.type)
#
# @itchat.msg_register(TEXT)
# def text_reply(msg):
#     print('{}'.format(msg['Text']))
#     return('You said to me one to one: %s' % msg.text)
#
# itchat.run()