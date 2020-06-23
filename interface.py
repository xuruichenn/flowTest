"""
@author: Xurui (Rachel) Chen
"""
import FlowCal
from rpy2.robjects.packages import STAP
from rpy2.robjects.packages import importr
from rpy2 import robjects
from rpy2.robjects import r
flowCore = importr("flowCore")
flowCut = importr("flowCut")

#takes FlowCal.io.FCSData input from user
print("Enter FlowCal.io.FCSData")
flowCalioFCSDataINPUT = input()


#takes figures path from user
print("Enter figures_save_path")
figuressavepath = input()


flowCalfcsdata = FlowCal.io.FCSData(flowCalioFCSDataINPUT)
flowCalflowcutdata = flowCut(flowCalfcsdata, MaxPercCut=0.5, UseOnlyWorstChannels=True, figuresavepath)


