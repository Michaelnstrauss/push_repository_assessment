

the_list = [1,0,7,2,0,3,9,0,4]


def zero_sort(the_list):
    new_list = [0 for i in range(the_list.count(0))]
    other_list = [i for i in the_list if i != 0]
    other_list.extend(new_list)
    return other_list

print(zero_sort(the_list))

#The number of steps this algorithm takes is 4.


# def zero_sort(the_list):
#     new_list = []
#     for num in the_list:
#         if num > 0:
#             new_list.append(num)
#         elif num == 0:
#             for num in the_list:
#                 new_list.append(num)
#     print(new_list)
        
        
    #     elif num == 0:
    #         for num in the_list:
    #             if num == 0:
    #                 new.list.append(num)
    # print(new_list)
    # #new_list.append(zero_list)
    # print(new_list)