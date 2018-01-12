# CheckFile.py
批量计算指定文件夹下所有文件的MD5值、文件大小、修改时间、绝对路径等信息并保存为File_MD5.txt

用法：
CheckFile.py －h (查看帮助)

CheckFile.py -d (DIRS) -o report.txt

示例：File_MD5.txt


c1253649afd954978efa509c82716ecc  2018-01-06 12:14:27  0.0001MB /Users/xx/PycharmProjects/TEST/bs4_test.py


a9e4bab38ead529802f670552e71773d  2018-01-10 23:17:58  0.0045MB /Users/xx/PycharmProjects/TEST/CheckFile.py


===========文件夹根目录： /Users/XX/PycharmProjects/TEST 


===========本次计算结果生成时间：2018-01-10 23:19:04.548448
# FileCMP.py
比较两个文本文件差异化内容，生成对比报告report.html
eg.: FileCMP.py file1 file2
