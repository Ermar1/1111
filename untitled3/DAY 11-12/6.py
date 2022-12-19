sort_dict = {}
vlan_list = []
new_list = []
sort_vlans = []
set_vlans = set()
file_read = 'CAM_table.txt'
with open(file_read) as file:
    for line in file:
        list = line.split()
        for item in list:
           if len(item.split('.')) == 3:
               print('{} {:>17} {:>9}'.format(list[0], list[1], list[3]))
               vlan_list.append(list[0])
               new_list.append(list[0] +'   '+ list[1] +'   '+ list[3])
set_vlans = set(vlan_list)
sort_vlans = [vlan_item for vlan_item in set_vlans]
sort_vlans.sort()
print(sort_vlans)
print('sorted items')
for vlan in sort_vlans:
    for item in new_list:
        if vlan in item[0:4]:
            print(item)
