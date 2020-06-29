# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 13:58:58 2020

@author: WillyAHEAD
"""

import FlowCal
import _pickle as pickle
import pandas as pd
import numpy as np
import rpy2.rinterface as ri
from rpy2.robjects.packages import STAP
from rpy2.robjects.packages import importr
from rpy2 import robjects
from rpy2.robjects import r
importr("flowCore")
importr("flowCut")
importr("flowFrame")

#to convert numpy array to r's matrix object
import rpy2.robjects as ro
import rpy2.robjects.numpy2ri
rpy2.robjects.numpy2ri.activate()
nr,nc = B.shape
Br = ro.r.matrix(B, nrow=nr, ncol=nc)
ro.r.assign("B", Br)

fcs_path = ("/home/willy/test_files_flowcut/fcs_files"
            "/vgh_00630_flow_001(BM)_AML,2f,MDS+M6_003_TdT_CD56_CD7_CD19_003.fcs")
r_fcs_path = r["file.path"](fcs_path)
fcs_data = FlowCal.io.FCSData(fcs_path)
#ignore: r_fcs_data = r["read.FCS"](r_fcs_path, transformation = False)

#transform function that fcsdata -> flowframe (input to flowcut)
#convert fcs_data which is of type numpy array into r's matrix object
#calls flowframe(fcs_data)
fcs_data = flowFrame(fcs_data)


r_fct_string = '''
    return_flagged_index = function(fcs_path){    
        r_fcs_path = file.path({fcs_path})
        r_fcs_data = read.FCS(r_fcs_path)
        res_flowcut = flowCut(r_fcs_data, MaxPercCut = 0.5, UseOnlyWorstChannels = TRUE)
        
        res_flowcut$ind
    }
'''
pyflowcut = STAP(r_fct_string, "pyflowcut")
flagged_index = list(pyflowcut.return_flagged_index(fcs_path))
flowcut_data = np.delete(fcs_data, flagged_index, axis = 0)
