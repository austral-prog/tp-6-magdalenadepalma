def remove_elements(list_to_remove_elements):
    if len(list_to_remove_elements) >= 6:
        del list_to_remove_elements[5]
        del list_to_remove_elements[4]
        del list_to_remove_elements[0]
        return list_to_remove_elements
    elif len(list_to_remove_elements) >= 5:
        del list_to_remove_elements[4]
        del list_to_remove_elements[0]
        return list_to_remove_elements
    elif len(list_to_remove_elements) >= 1:
        del list_to_remove_elements[0]
        return list_to_remove_elements
    else:
        return list_to_remove_elements

def add_elements(list_to_add_elements):
    list_to_add_elements.insert(0, 'Pink') 
    list_to_add_elements.append('Yellow')
    return list_to_add_elements

def is_empty(list_to_check):
    if len(list_to_check) == 0:
        return True
    else:
        return False

def check_lists(list_to_compare1, list_to_compare2):
    if len(list_to_compare1) >= 3 and len(list_to_compare2) >= 3 :
        if list_to_compare1[2] == list_to_compare2[2]:
            return True
        else:
            return False
    else:
        return False

def list_of_lists(list_of_lists_to_modify):
    list0 = list_of_lists_to_modify[0]
    list1 = list_of_lists_to_modify[1]
    list2 = list_of_lists_to_modify[2]
    if len(list0) >= 2:
        list0_new = list0[0:2]
        if len(list1) >= 2:
            list1_new = list1[1:4]
            if len(list2) >= 2:
                list2_new = list2[-2:]
                full_list_new = [list0_new , list1_new, list2_new]
                return full_list_new
            else:
                full_list_new = [list0_new , list1_new, list2]
                return full_list_new
        else:
            list1_new = []
            if len(list2) >= 2:
                list2_new = list2[-2:]
                full_list_new = [list0_new, list1, list2_new]
                return full_list_new
            else:
                full_list_new = [list0_new, list1, list2]
                return full_list_new 
    else:
        if len(list1) >=2 :
            list1_new = list1[1:4]
            if len(list2) >= 2:
                list2_new = list2[-2:]
                full_list_new = [list0, list1_new, list2_new]
                return full_list_new
            else:
                full_list_new = [list0, list1_new, list2]
        else:
            list1_new = []
            if len(list2) >= 2:
                list2_new = list2[-2:]
                full_list_new = [list0, list1_new, list2_new]
                return full_list_new
            else:
                full_list_new = [list0, list1_new, list2]
                return full_list_new

