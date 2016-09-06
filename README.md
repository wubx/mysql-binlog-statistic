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

# pasrebinlog_stat.py


###### 1. 安装需要的 Python 模块

```
pip install xlwt
pip install pandas
```

###### 2. 创建使用 pasrebinlog 解析后生成文件的存放位置
注意: 每一个binlog生成一个统计文件

```
mkdir -p /tmp/binlog_parse
```

###### 3. pasrebinlog 使用 pasrebinlog 生成统计文件保存到 /tmp/binlog_parse 目录中

```
ll /u01/other/backup/app_db/binlog/ | \
    awk '{print "/home/manager/script/mysql-binlog-statistic/bin/pasrebinlog /u01/other/backup/app_db/binlog/" $9 "> /tmp/binlog_parse/" $9 ".log"}' | \
    /bin/bash

```

###### 4. 使用 pasrebinlog_stat.py 生成相关

```
python pasrebinlog_stat.py /tmp/binlog_parse > format.txt
```

###### 5.查看生成的文件

```
ll
-rw-rw-r-- 1 manager manager  58191 Sep  6 17:18 format.txt
-rw-rw-r-- 1 manager manager 100352 Sep  6 17:18 sort_by_delete.xls
-rw-rw-r-- 1 manager manager 100352 Sep  6 17:18 sort_by_insert.xls
-rw-rw-r-- 1 manager manager 100352 Sep  6 17:18 sort_by_total.xls
-rw-rw-r-- 1 manager manager 100352 Sep  6 17:18 sort_by_update.xls
```
