with open('ospf.txt') as file:
    for line in file:
        ospf_route = line
        list_ospf = ospf_route.strip().strip(',').split()
        list_ospf.remove('via')
        list2_ospf = [element.strip('[').strip(']') for element in list_ospf]
        print (list2_ospf)
        keys = ['Protocol', 'Prefix', 'AD/Metric', 'Next-Hop', 'Last update', 'Outbound Interface']
        for i in range(len(keys)):
           print('{:<20} {}'.format(keys[i],list_ospf[i].strip(',')))
