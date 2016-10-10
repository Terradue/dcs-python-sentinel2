#!/opt/anaconda/bin/python

import cioppy

ciop = cioppy.Cioppy()

def get_data(reference, target):
    """
    Get data from an opensearch url
    """

    enclosure = subprocess.check_output("opensearch-client "+identifier+"&do="+os.environ['HOSTNAME']+" enclosure", shell=True)
    enclosure = enclosure.strip('\n')
    
    ciop.log('INFO', '[get_data function] Data enclosure url: ' + enclosure)
    
    local_file = ciop.copy(enclosure, ciop.tmp_dir)
    assert(local_file)
    
    return local_file
    
def publish_data(output):
    """
    Publish data as result of the process, storing it on HDFS
    """

    ciop.publish(output, metalink=True)