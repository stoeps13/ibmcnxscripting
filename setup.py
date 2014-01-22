

import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read( fname ):
    return open( os.path.join( os.path.dirname( __file__ ), fname ) ).read()

setup( 
    name = "ibmcnx_wasadmin_scripts",
    version = "0.2",
    author = "Christoph Stoettner",
    author_email = "christoph.stoettner@stoeps.de",
    description = ( "Some scripts to speed up configuration and troubleshooting"
                                   "for IBM Connections and IBM WebSphere" ),
    license = "Apache 2.0",
    keywords = "ibmcnx connections ibm",
    url = "http://github.com/stoeps13/ibmcnxscripting",
    packages = ['WebSphere'],
    long_description = read( 'README' ),
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Topic :: Utilities",
        "License :: OSI Approved :: Apache Licence",
    ],
 )

