import os

context = os.getenv('context', 'bstack')
bstack_userName = os.getenv('bstack_userName', os.getenv('USER_NAME'))
bstack_accessKey = os.getenv('bstack_accessKey', os.getenv('ACCESS_KEY'))
