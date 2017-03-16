import sys
import zmq
import time
import multiprocessing
from multiprocessing import *

############################################################################
global Router
global graph
global As_numbers_dict


#############################################################################Publisher C

def Publisher():
    portPC = '12771'
    #if len(sys.argv) > 1:
        #portPB = sys.argv[1]
        #int(portPB)
    context = zmq.Context()
    socketPC = context.socket(zmq.PUB)
    socketPC.bind('tcp://127.0.0.1:%s' % portPC)

    while True:
        socketPC.send(('I am Publish C'.encode('utf-8')))
        time.sleep(1)
################################################################################### C subscribe on A
def Subscriber1():
    portSCA = '10771'  # listen to Router A

    context = zmq.Context()
    socketCA = context.socket(zmq.SUB)
    socketCA.connect('tcp://localhost:%s' % portSCA)
    while True:

        socketCA.setsockopt(zmq.SUBSCRIBE, ''.encode('utf-8'))
        messageCB = socketCA.recv()
        print('message A to C'+str(messageCB))
        time.sleep(4)

    ################################################################################### C subscribe on B
def Subscriber2():
        portSCB = '11771'  # connection to Router B

        context = zmq.Context()
        socketCB = context.socket(zmq.SUB)
        socketCB.connect('tcp://localhost:%s' % portSCB)

        while True:
            socketCB.setsockopt(zmq.SUBSCRIBE, ''.encode('utf-8'))
            messageCB = socketCB.recv()
            print('message B to C' + str(messageCB))
            time.sleep(4)
#################################################################################################
def main():
    Process(target=Publisher).start()

    # Now we can connect a client to all these servers
    Process(target=Subscriber1).start()

    Process(target=Subscriber2).start()


if __name__ == '__main__':
    main()