import os

file_object = open('out.txt', 'r')
file_out = open('queryre_local.txt', 'w')

search_title = 'url=http://'
search_end1 = '.'

start = 0

my_set = set()

read_sum = 0
not_sum = 0
cnt_sum = 0

for eachLine in file_object:
        start = 128

        index_title = eachLine.find(search_title, start)
        if index_title == -1:
                continue
        index_title += 11

        read_sum+=1

        if eachLine[index_title] == 'z':
        	continue

        not_sum += 1
        if eachLine[index_title:-2] in my_set:
        	continue

        cnt_sum += 1
        my_set.add(eachLine[index_title:-2])

        print(eachLine[index_title:-2])

        type_url = 0
        if eachLine[index_title] == 'v':
        	type_url = 7
        elif eachLine[index_title] == 'i':
         	type_url = 6
        elif eachLine[index_title] == 'b':
         	type_url = 12
        elif eachLine[index_title] == 'w':
         	type_url = 1
        elif eachLine[index_title] == '2':
         	type_url = 1

        print(str(type_url)+ ' ' +eachLine[index_title:-2])

        file_out.write(str(type_url)+ ' ' +eachLine[index_title:-2])

print('read_sum'+str(read_sum)+' not_sum'+str(not_sum)+' cnt_sum'+str(cnt_sum)+' ')
file_object.close()
file_out.close()

