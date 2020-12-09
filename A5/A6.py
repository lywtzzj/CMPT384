import csv


data = []
usedData = []
parent = []
# read file
with open('LifeOnEarth.csv', 'rt', encoding='gbk') as file:
    reader = csv.reader(file)
    for i in reader:
        data.append(i[0:4])

DataN= data

## all data without first line
usedData = DataN[1::]

## get parent id
for i in usedData:
    parent.append(i[0])
# delete data
def delete_List(k):
    """
    from total dataset get each item .then => take number of child
    check the number if is in parent if not delete recuiser
    return
    """
    for i in usedData:
        if not i[2] in parent:
            index1 = usedData.index(i)
            usedData.remove(i)
            parent.remove(parent[index1])
    if len(usedData) >= k:
        delete_List(k)
    else:
        return usedData

delete_List(100)
#%% write into file
with open("coreTree.csv", "w", newline="") as bgin:
    write = csv.writer(bgin)
    write.writerow(DataN[0])
    for i in usedData:
        write.writerow(i)



