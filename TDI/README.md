# Scripts to use with openssl

## create_cacerts.sh

This script check the ROOT CA of given hostname and port. This certificate is then stored in a jks formated keystore. 

You can use this keystore file within IBM Connections and TDI to access selfsigned LDAPS.

The cacerts file can be set within populationWizard, you will be asked, when you select a ssl encrypted LDAP connection. Or you can add it within your TDISOLUTION Directory in `solution.properties`.

    javax.net.ssl.trustStore=/opt/install/cacerts`

### Prerequists

This scripts assume that keytool (java tool to create and edit keystores) is in your $PATH! You can edit the script to change to keytool within TDI or IBM Connections Wizard.

### Usage

    ./create_cacerts.sh -h hostname -p port -f path/filename

### Example

    ./create_cacerts.sh -h mail.stoeps.local -p 636 -f ~/cacert-neu2
    depth=0 C = DE, ST = Bavaria, L = Rosenheim, O = Stoeps Inc., CN = mail.stoeps.local
    verify error:num=18:self signed certificate
    verify return:1
    depth=0 C = DE, ST = Bavaria, L = Rosenheim, O = Stoeps Inc., CN = mail.stoeps.local
    verify return:1
    DONE
    Enter keystore password: ***
    Re-enter new password: ***
    Owner: CN=mail.stoeps.local, O=Stoeps Inc., L=Rosenheim, ST=Bavaria, C=DE
    Issuer: CN=mail.stoeps.local, O=Stoeps Inc., L=Rosenheim, ST=Bavaria, C=DE
    Serial number: 51b9a689
    Valid from: Wed Jun 12 02:00:00 CEST 2013 until: Mon Jun 13 01:59:00 CEST 2033
    Certificate fingerprints:
         MD5:  30:FF:B0:46:2F:4E:56:3D:86:36:D4:57:37:C3:19:BA
         SHA1: 33:0A:77:21:64:03:A5:E7:35:5C:6A:41:91:E9:6F:D5:9B:AB:33:10
         SHA256: E1:3C:5E:59:06:76:BF:BE:7D:DC:A3:EE:5C:5B:EE:DB:30:C3:58:A3:21:EF:A1:A0:84:0D:CC:C4:BA:28:9C:27
         Signature algorithm name: MD5withRSA
         Version: 3
    Trust this certificate? [no]:  yes
    Certificate was added to keystore
    
    
