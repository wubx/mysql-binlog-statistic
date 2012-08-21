mysql-binlog-statistic
======================
#parsebinlog

Help you find tables which was change by binlog statistic

通过binlog的分析统计，帮助你了解MySQL tables的变化

#dependency
/usr/local/mysql/bin/mysqlbinlog

perl


#how-to use
cd bin
chmod +x pasrebinlog
./parsebinlog /u1/mysql/logs/mysql-bin.000345

#format
output like :
...
----   -----
Table XX_db.XXinfo:
Type INSERT opt：  6 
Type UPDATE opt：  601 
10 col :  7 
12 col :  14 
13 col :  92 
14 col :  61 
16 col :  6 
18 col :  97 
19 col :  1 
2 col :  39 
3 col :  22 
4 col :  3 
5 col :  3 
6 col :  144 
8 col :  37 
9 col :  75 
...

#
