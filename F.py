import sys
import zmq
import time
import multiprocessing
from multiprocessing import*
############################################################################
global Router
global graph
global As_numbers_dict

############################################################################# Publish F

def Publisher():
        portPF='15771'
        context = zmq.Context()
        socketPF = context.socket(zmq.PUB)
        socketPF.bind('tcp://127.0.0.1 '+':'+ portPF)
        while True:
            socketPF.send(('I am publish F'.encode('utf-8')))
            time.sleep(1)

############################################################################### F subscribe on D
def Subscriber1():
        portSFD='13771' # listen  to Router D
        context = zmq.Context()
        socketFD = context.socket(zmq.SUB)
        socketFD.connect('tcp://localhost:%s' % portSFD)

        while True:
            socketFD.setsockopt(zmq.SUBSCRIBE, ''.encode('utf-8'))
            messageFD = socketFD.recv()
            print('message D to F ' + str(messageFD))
            time.sleep(5)
###############################################################################F subscribe on E
def Subscriber2():
        portSFE='14771' # listen  to Router E
        context = zmq.Context()
        socketFE = context.socket(zmq.SUB)
        socketFE.connect('tcp://localhost:%s' % portSFE)
        while True:
            socketFE.setsockopt(zmq.SUBSCRIBE, ''.encode('utf-8'))
            messageFE = socketFE.recv()
            print('message E to F ' + str(messageFE))
            time.sleep(5)

############################################################################### F subscribe on I
def Subscriber3():
        portSFI='18771' # listen  to Router I
        context = zmq.Context()
        socketFI = context.socket(zmq.SUB)
        socketFI.connect('tcp://localhost:%s' % portSFI)
        while True:
            socketFI.setsockopt(zmq.SUBSCRIBE, ''.encode('utf-8'))
            messageFI= socketFI.recv()
            print('message I to F ' + str(messageFI))
            time.sleep(5)
################################################################################Main()

def main():
    Process(target=Publisher).start()

    # Now we can connect a client to all these servers
    Process(target=Subscriber1).start()
    Process(target=Subscriber2).start()
    Process(target=Subscriber3).start()




if __name__ == '__main__':
         main()