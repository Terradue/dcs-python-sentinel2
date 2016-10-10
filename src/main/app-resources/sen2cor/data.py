#!/opt/anaconda/bin/python

import cioppy

ciop = cioppy.Cioppy()

def get_data(reference, target):
    """
    Get data from an opensearch url
    """

    ciop.log('INFO', 'processing input: ' + reference)
    
def publish_data(output):
    """
    Publish data as result of the process, storing it on HDFS
    """

    ciop.publish(output, mode='silent')