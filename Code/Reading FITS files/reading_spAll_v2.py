#!/usr/bin/env python

import numpy as np
import fitsio

filename = "spAll-v5_10_0.fits"
output_filename = "qso_matches.txt"

# open file - don't read it all into memory!
hduList = fitsio.FITS(filename, iter_row_buffer=2000) # read rows 2000 at a time
tableHDU = hduList[1]

# open output file
qso_output_file = open(output_filename, 'w')

qso_target_mask_bits = [10,11,12,13,14,15,16,17,18,19,40,41,42,43,44]
qso_target_mask_values = [2**bit for bit in qso_target_mask_bits]

for row in tableHDU:

	# check for QSO flags
	for flag in qso_target_mask_values:
		if (row['BOSS_TARGET1'] & flag) > 0:
			qso_output_file.write("{0}\n".format(row['THING_ID'])) # or whatever
			break # stop when any flag is found
	
	# check for other flags
	# ... add code here ...
