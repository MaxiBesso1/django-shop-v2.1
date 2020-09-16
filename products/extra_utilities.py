def get_range(list):
    y = -1
    list_final = []
    url_list = []
    for x in list:
        y+=1
        list_final.append(y)
    for x in list_final:
        url_list.append({"id":x,"url":list[x]["url"]})
                     
    return url_list