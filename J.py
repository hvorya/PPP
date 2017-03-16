import sys
import zmq
import time
import multiprocessing
from multiprocessing import *

############################################################################
global Router
global graph
global As_numbers_dict


#############################################################################Publisher J

def Publisher():
    portPJ = '19771'
    context = zmq.Context()
    socketPJ = context.socket(zmq.PUB)
    socketPJ.bind('tcp://127.0.0.1:%s' % portPJ)

    while True:
        socketPJ.send(('I am Publish J'.encode('utf-8')))
        time.sleep(1)
################################################################################### J subscribe on D
def Subscriber1():
    portSJD = '13771'  # listen to Router D

    context = zmq.Context()
    socketJD = context.socket(zmq.SUB)
    socketJD.connect('tcp://localhost:%s' % portSJD)
    while True:

        socketJD.setsockopt(zmq.SUBSCRIBE, ''.encode('utf-8'))
        messageCB = socketJD.recv()
        print('message D to J '+str(messageCB))
        time.sleep(4)

    ################################################################################### J subscribe on H
def Subscriber2():
        portSJH = '17771'  # listen to to Router H

        context = zmq.Context()
        socketJH = context.socket(zmq.SUB)
        socketJH.connect('tcp://localhost:%s' % portSJH)

        while True:
            socketJH.setsockopt(zmq.SUBSCRIBE, ''.encode('utf-8'))
            messageJH = socketJH.recv()
            print('message J to H ' + str(messageJH))
            time.sleep(4)
#################################################################################################
def main():
    Process(target=Publisher).start()

    # Now we can connect a client to all these servers
    Process(target=Subscriber1).start()

    Process(target=Subscriber2).start()


if __name__ == '__main__':
    main()