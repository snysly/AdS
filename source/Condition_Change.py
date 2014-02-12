import os
pID = os.environ['PBS_ARRAYID']

def Change_eps(ieps):
	return ieps + (float(pID)-1)*(0.9/100.0)

def Change_sigma(isigma):
	return isigma + (float(pID)-1)*(0.9/100)
