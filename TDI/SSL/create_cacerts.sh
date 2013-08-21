#!/bin/bash
#
# Getting Root Certificate from port and store it 
# to cacerts file (jks format)
#
# JKS certificate files can be used in Tivoli Directory Integrator to 
# accept SSL connections to selfsigned ldaps connections
#
# Author: Christoph Stoettner
# E-Mail: christoph.stoettner@stoeps.de
#
# Licence: 

# Create temporary directory for storing files
TMP1=`mktemp -d` 
# Delete temp directory on exit (kill -9 will leave the temp files)
trap "rm -rf $TMP1" EXIT

# Set variables through script parameters
# -h, -p, -f are required

while getopts h:p:f:?: option
do
    case "${option}"
        in
        h) SERVERNAME=${OPTARG};;
        p) SERVERPORT=${OPTARG};;
        f) STORECACERTS=${OPTARG};;
        ?) echo "USAGE: `basename $0` -h hostname -p port -f Certfile\n"
           echo "You have to type a password for keyfile twice and set\n"
           echo "the key to trusted!"
            exit
            ;;
    esac
done

# Check if all required parameters are set
#
if [ -z "$SERVERNAME" ] | [ -z "$SERVERPORT" ] | [ -z "$STORECACERTS" ] ; then
        echo "USAGE: `basename $0` -h hostname -p port -f Certfile"
        echo "You have to type a password for keyfile twice and set\n"
        echo "the key to trusted!"
        exit
fi

openssl s_client -showcerts -connect $SERVERNAME:$SERVERPORT < /dev/null > $TMP1/cst-key.out
openssl x509 -outform DER < $TMP1/cst-key.out > $TMP1/cst-key.der
openssl x509 -inform der -in $TMP1/cst-key.der -out $TMP1/cst-key.pem
# Keytool from Connections Installer
# /opt/install/Wizards/jvm/linux/jre/bin/keytool -import -alias Selfsigned -keystore $PATHTOSTORECACERTS/cacerts -file $TMP1/cst-key.pem
# Local Keytool
keytool -import -alias Selfsigned -keystore $STORECACERTS -file $TMP1/cst-key.pem

