import os

fr_test=open('e:\\1.txt','r',encoding= 'utf-8')
fr_online=open('e:\\2.txt','r',encoding= 'utf-8')

dict_test = dict()
dict_online = dict()

dict_test_name = dict()
dict_online_name = dict()

for buf in fr_test
    buf_lst=buf.split('\t')
    dict_test[buf_lst[0]]=buf_lst[1:]

for buf in fr_online
    buf_lst=buf.split('\t')
    dict_online[buf_lst[0]]=buf_lst[1:]

fr_test.seek(0)
fr_online.seek(0)

for buf in fr_test
    buf_lst=buf.split('\t')
    dict_test_name[buf_lst[1]]=buf_lst[2:]

for buf in fr_online
    buf_lst=buf.split('\t')
    dict_online_name[buf_lst[1]]=buf_lst[2:]

fr_test.close()
fr_online.close()

set_test_local = dict_test.keys()
set_online_local = dict_online.keys()

set_test_name = dict_test_name.keys()
set_online_name = dict_online_name.keys()

uset = set_test_local | set_online_local

fwu= open('e:\\3.txt','w')
for i in uset
	print dict_test[i]
	fwu.writelines(dict_test[i])
	fwu.write('\n')
fwu.close()

fwu=open('e:\\4.txt','w')
fwlost=open('e:\\5.txt','w')
for i in dict_test_name
	if i in dict_online_name:
		fwu.writelines(i+dict_test_name[i])
		fwu.write('\n')
		fwu.writelines(i+dict_online_name[i])
		fwu.write('\n')
	else:
		fwlost.writelines(i+dict_test_name[i])
		fwu.write('\n')

fwu.close()
fwlost.close()

input()




