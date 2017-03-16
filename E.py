import sys
import zmq
import time
import multiprocessing
from multiprocessing import*
############################################################################
global Router
global graph
global As_numbers_dict

############################################################################# Publish E

def Publisher():
        portPE='14771'
        context = zmq.Context()
        socketPE = context.socket(zmq.PUB)
        socketPE.bind('tcp://127.0.0.1 '+':'+ portPE)
        while True:
            socketPE.send(('I am publish E'.encode('utf-8')))
            time.sleep(1)

############################################################################### E subscribe on D
def Subscriber1():
        portSED='13771' # listen  to Router D
        context = zmq.Context()
        socketED = context.socket(zmq.SUB)
        socketED.connect('tcp://localhost:%s' % portSED)

        while True:
            socketED.setsockopt(zmq.SUBSCRIBE, ''.encode('utf-8'))
            messageED = socketED.recv()
            print('message D to E ' + str(messageED))
            time.sleep(5)
###############################################################################E subscribe on F
def Subscriber2():
        portSEF='15771' # listen  to Router F
        context = zmq.Context()
        socketEF = context.socket(zmq.SUB)
        socketEF.connect('tcp://localhost:%s' % portSEF)
        while True:
            socketEF.setsockopt(zmq.SUBSCRIBE, ''.encode('utf-8'))
            messageEF = socketEF.recv()
            print('message F to E ' + str(messageEF))
            time.sleep(5)

############################################################################### E subscribe on G
def Subscriber3():
        portSEG='16771' # listen  to Router G
        context = zmq.Context()
        socketEG = context.socket(zmq.SUB)
        socketEG.connect('tcp://localhost:%s' % portSEG)
        while True:
            socketEG.setsockopt(zmq.SUBSCRIBE, ''.encode('utf-8'))
            messageEG = socketEG.recv()
            print('message G to E' + str(messageEG))
            time.sleep(5)

############################################################################### E subscribe to H
def Subscriber4():
        portSEH='17771' # listen to  Router H
        context = zmq.Context()
        socketEH = context.socket(zmq.SUB)
        socketEH.connect('tcp://localhost:%s' % portSEH)
        while True:
            socketEH.setsockopt(zmq.SUBSCRIBE, ''.encode('utf-8'))
            messageEH = socketEH.recv()
            print('message H to E' + str(messageEH))
            time.sleep(5)

################################################################################Main()

def main():
    Process(target=Publisher).start()

    # Now we can connect a client to all these servers
    Process(target=Subscriber1).start()
    Process(target=Subscriber2).start()
    Process(target=Subscriber3).start()
    Process(target=Subscriber4).start()




if __name__ == '__main__':
         main()