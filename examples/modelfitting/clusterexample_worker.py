'''
Model fitting example using a cluster.

Fits an integrate-and-fire model to an in-vitro electrophysiological 
recording over one second.

This script is the 'worker' script and should be run on each worker machine
before the manager script is run.
'''
from brian.library.modelfitting import *
if __name__=='__main__':
    modelfitting_worker(max_cpu=2)