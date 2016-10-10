#!/opt/anaconda/bin/python

import cioppy
import subprocess
import os
import socket
import zipfile

ciop = cioppy.Cioppy()

def get_data(reference, target):
    """
    Get data from an opensearch url
    """

    enclosure = subprocess.check_output('opensearch-client "'+reference+'&do='+socket.gethostname()+'" enclosure', shell=True)
    enclosure = enclosure.strip('\n')
    
    ciop.log('INFO', '[get_data function] Data enclosure url: ' + enclosure)
    
    local_file = ciop.copy(enclosure, ciop.tmp_dir)
    assert(local_file)

    zip = zipfile.ZipFile(local_file, 'r')
    zip.extractall(ciop.tmp_dir)
    zip.close()
    
    return local_file+'.SAFE'
    
def publish_data(output):
    """
    Publish data as result of the process, storing it on HDFS
    """

    ciop.publish(output, metalink=True)
