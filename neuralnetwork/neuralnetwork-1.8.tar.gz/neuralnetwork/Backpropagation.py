import logging
import timeit
from dotenv import load_dotenv
import os
load_dotenv(os.getcwd()+'/.env')

class Backpropagation:
    nodeDeltas = []
    gradients = []
    biasGradients = []
    learningRate = []
    momentum = []
    weightUpdates = []
    biasWeightUpdates = []
    minimumError = ''
    maxNumEpochs = ''
    numEpochs = ''
    network = []
    globalError = ''
    trainingTime = ''

    def __init__(self, network, learningRate, momentum, minimumError = 0.005, maxNumEpochs = 2000):
        self.network = network
        self.learningRate = learningRate
        self.momentum = momentum
        self.minimumError = minimumError
        self.maxNumEpochs = maxNumEpochs
        self.initialise()

    def initialise(self):
        self.network.initialise()
        self.nodeDeltas = []
        self.gradients = []
        self.biasGradients = []

        totalNumNodes = self.network.getTotalNumNodes()
        self.weightUpdates = [0] * totalNumNodes
        for i in range(totalNumNodes):
            self.weightUpdates[i] = [0] * totalNumNodes
    
        self.biasWeightUpdates = [0] * totalNumNodes
        for i in range(totalNumNodes):
            self.biasWeightUpdates[i] = [0] * totalNumNodes

        self.gradients = [0] * totalNumNodes
        for i in range(totalNumNodes):
            self.gradients[i] = [0] * totalNumNodes

        self.biasGradients = [0] * totalNumNodes
        for i in range(totalNumNodes):
            self.biasGradients[i] = [0] * totalNumNodes

        self.initialiseValues()
        self.initialiseWeights()

    def initialiseValues(self):
        self.nodeDeltas = [0.00] * self.network.getTotalNumNodes()

    def initialiseWeights(self):
        networkLayers = self.network.getNetworkLayers()
        for num, layer in enumerate(networkLayers):
            if(num < len(networkLayers) - 1):
                for i in range(layer['start_node'], layer['end_node'] + 1):
                    for j in range(networkLayers[num + 1]['start_node'], networkLayers[num + 1]['end_node'] + 1):
                        self.weightUpdates[i][j] = 0.0

                for b in range(networkLayers[num+1]['start_node'],networkLayers[num+1]['end_node']+1):
                    self.biasWeightUpdates[num][b] = 0.0
                    
    def train(self, trainingSets):
        self.numEpochs = 1
        self.globalError = ''
        networkLayers = self.network.getNetworkLayers()

        starttime = timeit.default_timer()

        if(os.getenv("LOG_TRAINING")=='true'):
            logging.basicConfig(filename=os.getcwd()+'/training.log', level=logging.DEBUG)
        while True:
            if(self.numEpochs > self.maxNumEpochs):
                self.trainingTime = timeit.default_timer() - starttime
                return False

            sumNetworkError = 0
            for i in range(len(trainingSets)):
                self.network.activate(trainingSets[i])
                self.calculateNodeDeltas(trainingSets[i])
                self.calculateGradients()
                self.calculateWeightUpdates()
                self.applyWeightChanges()
                sumNetworkError += self.calculateNetworkError(trainingSets[i])

                if(os.getenv("LOG_TRAINING")=='true' and os.getenv("LOG_LEVEL")=='2'):
                    logging.info('--------------------------------')
                    logging.info("Inputs: {}, Outputs: {}, Network Error: {}".format(trainingSets[i],self.network.getOutputs(),self.calculateNetworkError(trainingSets[i])))
                
            
            self.globalError = sumNetworkError/(len(trainingSets) * networkLayers[len(networkLayers)-1]['num_nodes'])
                        
            if(os.getenv("LOG_TRAINING")=='true'):
                logging.info("Num Epochs: {}".format(self.numEpochs))
                logging.info("Global Error: {}".format(self.globalError))

            self.numEpochs = self.numEpochs + 1

            if(self.globalError < self.minimumError):
                self.trainingTime = timeit.default_timer() - starttime
                break

        return True
        
    def calculateNodeDeltas(self,trainingSet):
        networkLayers = self.network.getNetworkLayers()
        idealOutputs = trainingSet[-1 * networkLayers[len(networkLayers)-1]['num_nodes']:]
        startNode = networkLayers[len(networkLayers)-1]['start_node']
        endNode = networkLayers[len(networkLayers)-1]['end_node']
        activation = self.network.getActivation()

        j=0
        for i in range(startNode,endNode+1):
            if(isinstance(idealOutputs,list)):
                error = self.network.getValue(i) - idealOutputs[j]
            else:
                error = self.network.getValue(i) - idealOutputs
            self.nodeDeltas[i] = (-1 * error) * activation.getDerivative(self.network.getNet(i))
            j=j+1

        for k in range(len(networkLayers)-2,0, -1):
            startNode = networkLayers[k]['start_node']
            endNode = networkLayers[k]['end_node']
            for z in range(startNode,endNode+1):
                sum = 0
                for connectNode,weight in enumerate(self.network.getWeight(z)):
                    sum += weight * self.nodeDeltas[connectNode]
                self.nodeDeltas[z] = activation.getDerivative(self.network.getNet(z)) * sum

    def calculateGradients(self):
        networkLayers = self.network.getNetworkLayers()
        for num,layer in enumerate(networkLayers):
            if(num < len(networkLayers) - 1):
                for i in range(layer['start_node'],layer['end_node']+1):
                    for j in range(networkLayers[num+1]['start_node'],networkLayers[num+1]['end_node']+1):
                        self.gradients[i][j] = float(self.network.getValue(i)) * self.nodeDeltas[j]

                for b in range(networkLayers[num+1]['start_node'],networkLayers[num+1]['end_node']+1):
                    self.biasGradients[num][b] = self.nodeDeltas[b]

    def calculateWeightUpdates(self):
        networkLayers = self.network.getNetworkLayers()
        for num,layer in enumerate(networkLayers):
            if(num < len(networkLayers) - 1):
                for i in range(layer['start_node'],layer['end_node']+1):
                    for j in range(networkLayers[num+1]['start_node'],networkLayers[num+1]['end_node']+1):
                        self.weightUpdates[i][j] = (self.learningRate * self.gradients[i][j]) + (self.momentum * self.weightUpdates[i][j])

                for b in range(networkLayers[num+1]['start_node'],networkLayers[num+1]['end_node']+1):
                    self.biasWeightUpdates[num][b] = (self.learningRate * self.biasGradients[num][b]) + (self.momentum * self.biasWeightUpdates[num][b])


    def applyWeightChanges(self):
        networkLayers = self.network.getNetworkLayers()
        for num,layer in enumerate(networkLayers):
            if(num < len(networkLayers) - 1):
                for i in range(layer['start_node'],layer['end_node']+1):
                    for j in range(networkLayers[num+1]['start_node'],networkLayers[num+1]['end_node']+1):
                        self.network.updateWeight(i,j,self.weightUpdates[i][j])

                for b in range(networkLayers[num+1]['start_node'],networkLayers[num+1]['end_node']+1):
                    self.network.updateBiasWeight(num, b, self.biasWeightUpdates[num][b])


    def calculateNetworkError(self,trainingSet):
        networkLayers = self.network.getNetworkLayers()
        idealOutputs = trainingSet[-1 * networkLayers[len(networkLayers)-1]['num_nodes']:]
        startNode = networkLayers[len(networkLayers)-1]['start_node']
        endNode = networkLayers[len(networkLayers)-1]['end_node']
        j=0
        sum=0
        for i in range(startNode,endNode+1):
            if(isinstance(idealOutputs,list)):
                error = idealOutputs[j] - self.network.getValue(i)
            else:
                error = idealOutputs - self.network.getValue(i)

            sum += error * error
            j = j+1

        return sum

    def getNodeDeltas(self):
        return self.nodeDeltas

    def getGradients(self):
        return self.gradients

    def getBiasGradients(self):
        return self.biasGradients

    def getWeightUpdates(self):
        return self.weightUpdates

    def getBiasWeightUpdates(self):
        return self.biasWeightUpdates

    def getGlobalError(self):
        return self.globalError

    def getNumEpochs(self):
        return self.numEpochs

    def getTrainingTime(self):
        return self.trainingTime

        

