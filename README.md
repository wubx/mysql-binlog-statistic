#mysql-binlog-statistic#
***

#parsebinlog

Help you find tables which was change by binlog statistic

通过binlog的分析统计，帮助你了解MySQL tables的变化

#dependency
***

	`binlog_format           = mixed
	
	/usr/local/mysql/bin/mysqlbinlog
	
	perl`


#how-to use
***

    cd bin

    chmod +x pasrebinlog

    ./parsebinlog /u1/mysql/logs/mysql-bin.000345

#format
output like :



	`Table XX_db.XXinfo:

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
	
	9 col :  75 `

**cutlogbytime**
##用于从慢日志用截取一个时间段的日志方便分析##
    ./cutlogbytime /path/slowlogfile  starttime endtime
时间需要写时戳


    mysql> select unix_timestamp('2013-04-05');
	+------------------------------+
	| unix_timestamp('2013-04-05') |
	+------------------------------+
	|                   1365091200 | 
	+------------------------------+
	1 row in set (0.00 sec)
    
    mysql> select unix_timestamp('2013-04-06');
	+------------------------------+
	| unix_timestamp('2013-04-06') |
	+------------------------------+
	|                   1365177600 | 
	+------------------------------+
	1 row in set (0.00 sec)
***
    ./cutlogbytime /path/slowlogfile 1365091200 1365177600 > 20130405_slow.log 

#
mysqlbinlog 
================================
支持flashback功能

    ./mysqlbinlog -B |mysql
