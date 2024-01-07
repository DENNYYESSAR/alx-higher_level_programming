#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    templ = my_list[:]
    if idx < 0:
        return templ
    if idx > len(my_list) - 1:
        return templ
    templ[idx] = element
    return templ
