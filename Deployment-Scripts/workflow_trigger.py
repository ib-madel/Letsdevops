
import os
import requests
import sys

TOKEN= str(sys.argv[1])
OWNER= str(sys.argv[2])
REPO= str(sys.argv[3])
Workflow_Name= str(sys.argv[4])
pl_Baseline_Number= str(sys.argv[5])
pl_Baseline_Revision = str(sys.argv[6])


print( "the toke value is")
