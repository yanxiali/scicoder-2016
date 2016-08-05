#!/usr/bin/env python

'''
Script to search 12 GB SDSS spAll catalog file, located here:

https://data.sdss.org/sas/ebosswork/eboss/spectro/redux/v5_10_0/

The script takes many hours to run.

'''

import numpy as np
import pyfits
print "Loading..."
fi=pyfits.open ('spAll-v5_10_0.fits', memmap=True)
da=fi[1].data
print "done"

# find matching masks for BOSS
bt1=[10,11,12,13,14,15,16,17,18,19,40,41,42,43,44] ## these are the qso target mask bits 
w_qso = np.zeros(len(da),dtype=bool)
for b in bt1:
    w_qso = w_qso | ((da.BOSS_TARGET1 & 2**b) > 0)
print "Found ",w_qso.sum(), "BOSS objects."

# find matching masks for SEQUELS/eBOSS
ebt1=[10,11,12,13,14,15,16,17,18] ## these are the qso target mask bits 
ew_qso = np.zeros(len(da),dtype=bool)
for b in ebt1:
    # SEQUELS
    ew_qso = ew_qso | ((da.EBOSS_TARGET0 & 2**b) > 0)
    # EBOSS proper
    ew_qso = ew_qso | ((da.EBOSS_TARGET1 & 2**b) > 0)

print "Found ",ew_qso.sum(), "eBOSS objects."

w_tot=w_qso|ew_qso
print "Found", len(frozenset(da[w_qso].THING_ID)), "unique BOSS objects."
print "Found", len(frozenset(da[ew_qso].THING_ID)), "unique eBOSS objects."
print "Found", len(frozenset(da[w_tot].THING_ID)), "unique total objects."