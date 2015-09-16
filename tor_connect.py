import sys
import getpass

import stem
import stem.connection

#thanks, example code
#https://stem.torproject.org/api/control.html

from stem.control import Controller

if __name__=='__main__':
    with Controller.from_port() as control:
        control.authenticate()
        print "I guess we're connected?"
        print control.get_version()

        control.close()

        




