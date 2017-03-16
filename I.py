import sys
import zmq
import time
import multiprocessing
from multiprocessing import *

############################################################################
global Router
global graph
global As_numbers_dict


############################################################################# I publisher

def Publisher():
    portPI = '18771'
    context = zmq.Context()
    socketPI = context.socket(zmq.PUB)
    socketPI.bind('tcp://127.0.0.1:%s' % portPI)
    while True:
        socketPI.send(('I am Publish  I'.encode('utf-8')))
        time.sleep(1)

###############################################################subscribe I on F

def Subscriber1():

    portSIF = '15771'  # listen  to Router F
    context = zmq.Context()
    socketIF = context.socket(zmq.SUB)
    socketIF.connect('tcp://localhost:%s' % portSIF)
    while True:
        socketIF.setsockopt(zmq.SUBSCRIBE,''.encode('utf-8'))
        messageIF = socketIF.recv()

        print('message F to I '+str(messageIF))

        time.sleep(1)

################################################################################### Main()
def main():
    Process(target=Publisher).start()

    # Now we can connect a client to all these servers
    Process(target=Subscriber1).start()



if __name__ == '__main__':
    main()