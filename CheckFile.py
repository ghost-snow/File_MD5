#coding=utf-8

import hashlib
import os
import time
import datetime
import sys
#import getopt
import argparse
import difflib

#手动设置递归深度，防止超出列表默认递归值
sys.setrecursionlimit(1000000)
#获取文件绝对路径
def get_File_Path(file_Path):
    File_Path = os.path.abspath(file_Path)
    return File_Path

#计算文件md5值
def Md5(file_Path):
    m = hashlib.md5()
    m.update(file_Path.encode('utf-8'))
    return m.hexdigest()
#print(Md5(file_Path))

#计算文件大小,单位为MB
def get_FileSize(file_Path):
    file_size = os.path.getsize(file_Path)
    file_size = file_size/(1000*1000)
#    print('文件大小' + str(file_size))
    return round(file_size,4)
#print(get_FileSize(file_Path))

#把时间戳转换为标准时间
def TimeStampToTime(timestamp):
    timeStruct = time.localtime(timestamp)
    return str(time.strftime('%Y-%m-%d %H:%M:%S',timeStruct))
#获取文件的修改时间
def get_FileModifyTime(file_Path):
#    filePath = unicode(file_Path,'utf8')
    t = os.path.getmtime(file_Path)
    return TimeStampToTime(t)
#print(get_FileModifyTime(file_Path))

#遍历文件夹及文件夹下的文件
def IterateFiles(directory):
    assert os.path.isdir(directory),'Make sure directory argument should be a directory.'
    result = []
    for root,dirs,files in os.walk(directory, topdown=True):
        for fl in files:
            result.append(os.path.join(root,fl))
    #Ver 1.0
    for i in range(0,len(result)):
         with open('File_MD5.txt','a') as f:

             f.write('\n' + str(Md5(result[i])) + '  ' + str(get_FileModifyTime(result[i])) + "  "
                       + str(get_FileSize(result[i])) + 'MB ' + str(get_File_Path(result[i])) +'\n' )
    return result
#输出结果文件
def OutFiles(outfile):
    with open('File_MD5.txt','r') as old:
        for line in old.readlines():
            with open(args.outfile,'a') as newfile:
                newfile.write(line)
#
#比较两次计算结果文件差异
def FileCMP(file1,file2):
    pass

if __name__ == '__main__':
    datetime = datetime.datetime.now()
    # Ver 0.9
    # opts, args = getopt.getopt(sys.argv[1:], '-h-d:-v', ['help','Dirs =', 'version'])
    # for opt_name,opt_value in opts:
    #     if opt_name in ('-h', '--help'):
    #         print(r'[*] NOTE: Please run this program under the Python3.X.')
    #         print(r'[*] For example：''\n''[*] python CheckFile.py -d D:\\TEST\One')
    #         exit()
    #     if opt_name in ('-v', '--version'):
    #         print('[*]The version is 1.0')
    #         exit()
    #     if opt_name in ('-d', '--dirs'):
    #         dirs = opt_value
    #         IterateFiles(dirs)
    #         with open('File_MD5.txt', 'a') as f:
    #             f.write('===========文件夹根目录： ' + str(os.path.abspath(dirs)) +
    #                     '    本计算结果生成时间：' + str(datetime) + '=============')
    #         print('计算已完成: File_MD5.txt ' + '生成时间：' + str(datetime))
    #         exit()

    # Ver1.0
    help = ('\n'r"[*] 程序功能：通过-d参数遍历并生成指定文件夹中文件的散列值（md5），并将结果保存在"
            '\n'r"[*] 一个文本文档中，同时保存文件大小、修改时间。"
            '\n'r"[*] NOTE: Please run this program under the Python3.X"
            '\n'r"[*] For example: 'python CheckFile.py -d D:\TEST\ONE -o report.txt'"
            '\n'r"[*] Result: 32f4ddcfcfe2ac8f02a1d5b6dfdcb886  1231MB  2017.10.10  /Web/admin/index.php")
    parser = argparse.ArgumentParser(help)
    parser.add_argument('-v','--version', help='show the Version',action ='store_true')
    parser.add_argument('-d','--dirs', help='指定文件夹路径（eg."/usr/local/share"）',action ='store')
    parser.add_argument('-o', '--outfile', help='指定计算结果输出文件(eg."report.txt")', action='store')

    args = parser.parse_args()

    if args.version:
        ver = 'The version is 1.1'
        print(ver)

    if args.dirs:
        IterateFiles(args.dirs)
        with open('File_MD5.txt', 'a') as f:
            f.write('\n''===========文件夹根目录： ' + str(os.path.abspath(args.dirs)) +
                '  本次计算结果生成时间：' + str(datetime) + '=============''\n')
            print('计算已完成: '+ args.outfile + ' 生成时间：' + str(datetime))

    if args.outfile:
        OutFiles(outfile=args.outfile)
        os.remove('File_MD5.txt')
        
