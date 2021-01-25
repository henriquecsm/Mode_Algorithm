import random

#To get a random list of temperature
def get_list_temp(size):
    list_temp = []
    try:
        for i in range(size):
            list_temp.append(round(random.uniform(1,size),2))   #to generate float number
            list_temp.append(random.randint(1, size))           #to generate integer number
        return list_temp
    except Exception as e:
        print(e)
        return 0

#Sort numbers list
def order_list(list_t):
    try:
        if len(list_t) == 1 or not list_t: #check the list length, minimum is 1 element, if it is 1 or [] then result is [0]
            return [0]
        list_t.sort()
        return list_t
    except Exception as e:
        print('Error: order_list - %s' % e)
        return 0

#It will return a list with mode
def get_mode(list_temp):
    try:
        if len(list_temp) == 1: #check the list length, minimum is 1 element, if it is 1 then result is 0
            return '[0]'
        a = 0
        c = 1
        d = {}
        l = []
        for i in range(len(list_temp)):
            if a == list_temp[i]:
                c += 1
            elif c > 1:
                d[list_temp[i-1]] = c   #put the repeated number into a dic
                c = 1;
            a = list_temp[i]
        m = d[max(d, key=d.get)]        #Check what is the biggest number of repetitions
        for key in d.keys():
            if (d[key] == m):
                l.append(key)           #List with most frequent number
        return l
    except Exception as e:
        print('Error: get_mode - %s' % e)
        return 0



d_set = [-5.05, 8, 7.5, 5, 9.54, 4, 6.76, 5.84, 1, 1.28, 4, 1.09, 6, 3.02, 8, 2.02, 3, 7.52, 6, 5.05]
#list_temp = get_list_temp(10000)
#print(list_temp)
print(d_set)
print(order_list(d_set))
print(get_mode(order_list(d_set)))
#print(get_mode(order_list(list_temp)))