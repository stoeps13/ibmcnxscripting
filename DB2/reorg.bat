FOR %A IN (activities blogs cognos communities dogear files forum libraries.gcd libraries.os metrics mobile wikis) DO db2 -td@ -vf %A\db2\reorg.sql

FOR %A IN (homepage profiles) DO db2 -tvf %A\db2\reorg.sql
