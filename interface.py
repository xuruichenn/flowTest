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
flowCalioFCSData = flowCore.flowFrame('''INSERT FILEPATH HERE''')

#takes figures path from user
figuressavepath = '''INSERT FILEPATH HERE'''


flowCalfcsdata = FlowCal.io.FCSData(flowCalioFCSData)
flowCalflowcutdata = flowCut(flowCalfcsdata, MaxPercCut=0.5, UseOnlyWorstChannels=True, figuressavepath)


