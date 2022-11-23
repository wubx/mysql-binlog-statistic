#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import re
import copy
import pandas as pd

file_dir = '/tmp/binlog_parse'
def main(file_dir=None):
    if not file_dir:
        print 'Can not find directory'

    table_stat = {}
    for file_name in os.listdir(file_dir):
        file_path = '{dir}/{file_name}'.format(
                                 dir = file_dir,
                                 file_name = file_name)
        with open(file_path, 'r') as f:
            table_name = '' # 初始化当前表名
            for line in f: # 读取文件每一行
                if line.startswith('Table'): # 如果该行是 Table 开头说明解析到表了
                    table_name = line.split().pop().rstrip(':')
                    if table_stat.has_key(table_name):
                        continue
                    table_stat[table_name] = {
                        'table_name': table_name,
                        'insert': 0,
                        'update': 0,
                        'delete': 0,
                        'total': 0
                    }
                elif line.startswith('Type INSERT opt'): # 如果该行是 Type INSERT opt 开头说明解析到插入
                    insert_count = line.split().pop()
                    table_stat[table_name]['insert'] += int(insert_count)
                    table_stat[table_name]['total'] += int(insert_count)
                elif line.startswith('Type UPDATE opt'): # 如果该行是 Type UPDATE opt 开头说明解析到更新
                    update_count = line.split().pop()
                    table_stat[table_name]['update'] += int(update_count)
                    table_stat[table_name]['total'] += int(update_count)
                elif line.startswith('Type DELETE opt'): # 如果该行是 Type DELETE opt 开头说明解析到删除
                    delete_count = line.split().pop()
                    table_stat[table_name]['delete'] += int(delete_count)
                    table_stat[table_name]['total'] += int(delete_count)
                elif re.search('^\d*', line).group(): # 解析到操作的行
                    col_name = line.split(':')[0].strip() # 哪一个列
                    op_count = line.split(':').pop().strip() # 操作次数
                    if table_stat[table_name].has_key(col_name): # 已经有该列了
                        table_stat[table_name][col_name] += int(op_count)
                    else: # 还没有该列
                        table_stat[table_name][col_name] = int(op_count)

    print_table_stat = copy.deepcopy(table_stat) # 用于打印的表统计

    # 按解析的格式打印(原格式)
    for row_stat in print_table_stat.values():
        print '===================================='
        if row_stat.has_key('table_name'): # 打印表名称
            print 'Table {table_name}:'.format(table_name = row_stat.pop('table_name'))
        if row_stat.has_key('total'): # 打印更新操作数量
            print 'Type TOTAL opt:  {total}'.format(total = row_stat.pop('total'))
        if row_stat.has_key('insert'): # 打印插入操作数量
            print 'Type INSERT opt:  {insert}'.format(insert = row_stat.pop('insert'))
        if row_stat.has_key('delete'): # 打印删除操作数量
            print 'Type DELETE opt:  {delete}'.format(delete = row_stat.pop('delete'))
        if row_stat.has_key('update'): # 打印更新操作数量
            print 'Type UPDATE opt:  {update}'.format(update = row_stat.pop('update'))
        for item in row_stat.items(): # 打印列操作的情况
            print '{col} :  {count}'.format(col = item[0], count = item[1])
        print '===================================='

    ############################################
    # 排序并输出成excel
    ############################################
    df = pd.DataFrame(table_stat.values())
    df2 = df.set_index('table_name')

    sort_by_total = df2.sort_values(by = ['total'], ascending = [False])
    sort_by_update = df2.sort_values(by = ['update'], ascending = [False])
    sort_by_insert = df2.sort_values(by = ['insert'], ascending = [False])
    sort_by_delete = df2.sort_values(by = ['delete'], ascending = [False])

    sort_by_total.to_excel('sort_by_total.xls')
    sort_by_update.to_excel('sort_by_update.xls')
    sort_by_insert.to_excel('sort_by_insert.xls')
    sort_by_delete.to_excel('sort_by_delete.xls')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Usage: python pasrebinlog_stat.py <dir>'
        sys.exit(1)

    main(sys.argv[1])
