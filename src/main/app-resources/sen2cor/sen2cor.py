#!/opt/anaconda/bin/python

import cioppy
import subprocess
import os
import glob
from shutil import copyfile
from osgeo import gdal

ciop = cioppy.Cioppy()

def sen2cor(reference, product):
    """
    SEN2COR is a prototype processor for Sentinel-2 Level 2A product formatting 
    and processing. The processor performs the tasks of atmospheric, terrain and
    cirrus correction and a scene classification of Level 1C input data.
    """
    resolution = ciop.getparam('resolution')    
    identifier = subprocess.check_output('opensearch-client -m EOP "' + reference + '"' + ' identifier', shell=True)
    identifier = identifier.strip('\n')
    
    # Setting sen2cor environment
    os.environ['SEN2COR_BIN'] = '/opt/anaconda/lib/python2.7/site-packages/sen2cor'
    os.environ['GDAL_DATA'] = '/opt/anaconda/share/gdal'
    os.environ['PATH'] = '/opt/anaconda/bin/' + os.pathsep + os.environ['PATH']
    os.environ['SEN2COR_HOME'] = os.environ['TMPDIR'] + '/sen2cor'
    cfg = os.environ['SEN2COR_HOME'] + '/cfg'
    if not os.path.exists(cfg):
        os.makedirs(cfg)
        
    copyfile(os.environ['SEN2COR_BIN'] + '/cfg/L2A_GIPP.xml', cfg + '/L2A_GIPP.xml')
    copyfile(os.environ['SEN2COR_BIN'] + '/cfg/L2A_CAL_AC_GIPP.xml', cfg + '/L2A_CAL_AC_GIPP.xml')
    copyfile(os.environ['SEN2COR_BIN'] + '/cfg/L2A_CAL_SC_GIPP.xml', cfg + '/L2A_CAL_SC_GIPP.xml')
    
    ciop.log('INFO', '[sen2cor function] Invoke SEN2COR L2A_Process')
    
    args = ["L2A_Process"+" --resolution "+resolution+" "+product]
    p = subprocess.call(args,shell=True)
    
    level_2a = identifier.replace('L1C', 'L2A')
    level_2a = level_2a.replace('OPER', 'USER')
    level_2a_path = os.path.join(ciop.tmp_dir, level_2a+'.SAFE')
    
    os.chdir(level_2a_path)
    metadata = glob.glob("S2A*.xml")[0]

    src = gdal.Open(metadata,gdal.GA_ReadOnly)
    subset = src.GetSubDatasets()[0][0]
    
    src = None
    
    ciop.log('INFO', '[sen2cor function] Process '+ subset)
    output = os.path.join(ciop.tmp_dir, level_2a+'_'+resolution+'.TIF')
    
    # TODO: Perform this step using the GDAL Python classes
    args = ["gdal_translate "+subset+" "+output]
    p = subprocess.call(args,shell=True)
    
    return output

