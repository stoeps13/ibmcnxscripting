#!/bin/bash

# Download the files from IBM
BASEPATH=`pwd`
mkdir download
cd download
FILEPATH=infolib.lotus.com/resources/connections/4.5.0/doc/accessible/admin/en_us

wget -mk http://infolib.lotus.com/resources/connections/4.5.0/doc/accessible/admin/en_us/acc_p1.html
wget -mk http://infolib.lotus.com/resources/connections/4.5.0/doc/accessible/admin/en_us/acc_p2.html
wget -mk http://infolib.lotus.com/resources/connections/4.5.0/doc/accessible/admin/en_us/acc_p3.html
wget -mk http://infolib.lotus.com/resources/connections/4.5.0/doc/accessible/admin/en_us/acc_p4.html
wget -mk http://infolib.lotus.com/resources/connections/4.5.0/doc/accessible/admin/en_us/acc_p5.html

# html tidy to separate the tags
cd $FILEPATH
for i in $(seq 1 5); do
    tidy -wrap 0 -c -i acc_p${i}.html > acc_p${i}_a.html 
done

# remove head and foot (incl toc)
for i in $(seq 1 5); do
    sed '1,/<div class="nested0" role="main"/d;/<\/body>/,$d' acc_p${i}_a.html > acc_p${i}_b.html
done
# Create proper css and put files together
# Create html header
sed '/<\/head>/,$d' acc_p1.html > head.html
sed -i 's/<link rel="stylesheet"[^>]*>//g' head.html
sed -i '/<title>/d' head.html
sed '/<\/body>/,$d' acc_p1.html > foot.html
echo '<link rel="stylesheet" type="text/css" href="custom.css" />' >> head.html
echo '<title>IBM Connections 4.5 CR1</title>' >> head.html
echo '<script type="text/javascript" src="toc.js"></script>' >> head.html
echo '</head><body>' >> head.html

# Create on html file for Documentation
cat head.html > cnx45documentation.html
for i in $(seq 1 5) ; do
    cat acc_p${i}_b.html >> cnx45documentation.html
done
cat foot.html >> cnx45documentation.html
sed -i -e 's/href="acc_p[1-5].html#/href="cnx45documentation.html#/g' cnx45documentation.html
# Now you should remove the temporary files :)
