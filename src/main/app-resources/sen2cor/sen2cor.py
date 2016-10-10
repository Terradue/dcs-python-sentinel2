#!/opt/anaconda/bin/python

import cioppy

ciop = cioppy.Cioppy()

def sen2cor(reference, product):
    """
    SEN2COR is a prototype processor for Sentinel-2 Level 2A product formatting 
    and processing. The processor performs the tasks of atmospheric, terrain and
    cirrus correction and a scene classification of Level 1C input data.
    """

    resolution = ciop.getparam('resolution')
