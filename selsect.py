import os

file_object = open('out.txt', 'r')

file_out = open('queryre_local.txt', 'w')
file_out2 = open('queryre_err.txt', 'w')

search_title = 'title='
search_end1 = ','
search_title_old = 'old_title='
search_end2 = '\n'
start = 0

str_buf = ''

num_a = 0
num_b = 0

for eachLine in file_object:
        start = 0
        eachLine.strip(' ')
        str_buf += eachLine

        index_title_old = eachLine.find(search_title_old, start)
        if index_title_old == -1:
                continue

        print(str_buf)
        index_title = str_buf.find(search_title, start)
        if index_title == -1:
                print(str(1))
                continue
        index_title += 6
        start = index_title + 1

        index_end1 = str_buf.find(search_end1, start)
        if index_end1 == -1:
                print(str(2))
                continue

        start = index_end1 + 1

        index_title_old = str_buf.find(search_title_old, start)
        if index_title_old == -1:
                print(str(3))
                continue
        index_title_old += 10		

        index_end2 = str_buf.find(search_end2, start)
        if index_end2 == -1:
                print(str(4))
                continue

        if str_buf[index_end1-1] == ' ':
                index_end1 -= 1

        if str_buf[index_end2-1] == ' ':
                index_end2 -= 1
      
        if index_end2-index_title_old < index_end1 - index_title:
                start = index_end2-index_title_old
        else:
                start = index_end1 - index_title


        iret = cmp(str_buf[index_title:index_title+start],str_buf[index_title_old:index_title_old+start])

        if iret == 0:
                num_a+=1
                file_out.write(str(num_a)+ ' ' +str_buf)
        else:
                num_b+=1
                file_out2.write(str(num_b)+ ' ' +str_buf)

        str_buf = ''

file_object.close()
file_out.close()
file_out2.close()