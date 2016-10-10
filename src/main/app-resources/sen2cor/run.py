#!/opt/anaconda/bin/python

import sys
import os
import cioppy
from data import get_data
from data import publish_data
from sen2cor import sen2cor

ciop = cioppy.Cioppy()

# Input references come from STDIN (standard input) and they are retrieved
# line-by-line.
for reference in sys.stdin:
  
    ciop.log('INFO', '**** Sentinel-2 Atmospheric Correction ****')
    ciop.log('INFO', '------------------------------------------------------------')
    ciop.log('INFO', 'Input S-2 L1C product reference: ' + reference)
    ciop.log('INFO', '------------------------------------------------------------')
    
    ciop.log('INFO', 'STEP 1: Getting input product')
    local_product = get_data(reference.strip('\n'), os.environ['TMPDIR'])
    ciop-log "INFO" "------------------------------------------------------------"
    
    ciop.log('INFO', 'STEP 2: SEN2COR tool')
    output = sen2cor(reference, local_product)
    ciop-log "INFO" "------------------------------------------------------------"
    
    ciop.log('INFO', 'STEP 3: Publishing results')
    publish_data(output)
    ciop-log "INFO" "------------------------------------------------------------"