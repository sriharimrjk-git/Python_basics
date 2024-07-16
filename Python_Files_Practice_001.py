# Print all the lines in a file line by line

# with open('1.txt', 'r') as reader:
#     line = reader.readline()
#     while line !='':
#         print(line)
#         line = reader.readline()


#Read  a file store it in a list.

# with open('1.txt', 'r') as reader:
#     content_org= reader.readlines()
#     print(content_org)

#Read a file store it in a list , reverse the list and write it on to a file
with open('1.txt', 'r') as reader:
    content_org= reader.readlines()
    content_rev= (reversed(content_org))
#print(content_rev)
print(content_org)

with open('2.txt','w') as writer:
    for item in content_rev:
        writer.write(item+"\n")

