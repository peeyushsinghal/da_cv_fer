from pathlib import Path
import torch
import torch.optim as optim
import torch.nn as nn
import os

class RunConfig:
    def __init__(self) -> None:
        self.EPOCHS = 1
        self.NUM_EPOCHS = 1
        self.IN_COLAB = False
        if os.path.exists('/content'): # check for google colab
            self.IN_COLAB = True
        
        if self.IN_COLAB:
            self.EPOCHS = 100
            self.NUM_EPOCHS = 100  
        # self.optimizer = None
        self.lr_strategy = None
        self.inital_lr = 0.005
        self.use_cuda = torch.cuda.is_available()
        self.device = torch.device("cuda" if self.use_cuda else "cpu")
        self.criterion_class = nn.CrossEntropyLoss() # we are not doing log_softmax or softmax
        self.criterion_domain = nn.BCEWithLogitsLoss() # we can also use nn.CrossEntropyLoss() - we are not doing log_softmax or softmax


        self.EWC_LAMBDA = 0.4
        


if __name__ =='__main__':
    runconfig = RunConfig()
    print(runconfig.EPOCHS)
    print(runconfig.device)
    
