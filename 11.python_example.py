import functools

emp_dict = {
    101: {'name': 'Anupriya Roy',
          'depart_id': 1,
          'attendances': [{'date': 1, 'hours': [3.5, 4.5]}, {'date': 2, 'hours': [3.2, 4.5]},
                          {'date': 3, 'hours': [3.2, 4.6]},
                          {'date': 4, 'hours': [3.0, 4.5]}, {'date': 5, 'hours': [2.5, 4.5]},
                          {'date': 6, 'hours': [1.5, 4.5]},
                          {'date': 7, 'hours': [2, 3]}, {'date': 8, 'hours': [0, 4.5]}, {'date': 9, 'hours': [2, 3.5]},
                          {'date': 10, 'hours': [4, 3.5]}],
          'leaves': [{'date': 7, 'no_of_hours': 1.5}, {'date': 7, 'no_of_hours': 1.5}, {'date': 8, 'no_of_hours': 3}]
          },
    102:
        {'name': 'Kadambari Sharma',
         'depart_id': 1,
         'attendances': [{'date': 1, 'hours': [0, 4.5]}, {'date': 2, 'hours': [3.2, 0]},
                         {'date': 3, 'hours': [3.2, 4.6]},
                         {'date': 4, 'hours': [1, 4.5]}, {'date': 5, 'hours': [2.5, 2]}, {'date': 6, 'hours': [1.5, 1]},
                         {'date': 7, 'hours': [2, 4]}, {'date': 8, 'hours': [1, 4.5]}, {'date': 9, 'hours': [2, 2]},
                         {'date': 10, 'hours': [2, 3.5]}],
         'leaves': [{'date': 1, 'no_of_hours': 3.5}, {'date': 2, 'no_of_hours': 2}, {'date': 2, 'no_of_hours': 2}]
         },
    103:
        {'name': 'Abhishek Verma',
         'depart_id': 1,
         'attendances': [{'date': 3, 'hours': [3.2, 4.6]}, {'date': 4, 'hours': [1, 4.5]},
                         {'date': 5, 'hours': [2.5, 2]},
                         {'date': 6, 'hours': [1.5, 1]}, {'date': 7, 'hours': [2, 4]}, {'date': 8, 'hours': [1, 4.5]},
                         {'date': 9, 'hours': [2, 2]}, {'date': 10, 'hours': [2, 3.5]}],
         'leaves': [{'date': 1, 'no_of_hours': 3}, {'date': 2, 'no_of_hours': 2}, {'date': 2, 'no_of_hours': 3}]
         }
}
c=[]
for i, j in emp_dict.items():

    a = [{'employee_id': i, 'employee_name': j['name'],
          'total_attendance_hours':sum(map(lambda b: sum(b['hours']), j['attendances'])),
          'total_leave_days': sum(map(lambda b: b['no_of_hours'], j['leaves']))
          }]
    print(a)

    # b = map(lambda a:sum(a),j['attendances']['hours'])
    # print(list(b))
    ##print(a)

# a1=emp_dict[101]["leaves"]
# x1=a1[0]
# y1=x1.get("no_of_hours")
#
# a2=emp_dict[101]["leaves"]
# x2=a2[1]
# y2=x2.get("no_of_hours")
#
# a3=emp_dict[101]["leaves"]
# x3=a3[2]
# y3=x3.get("no_of_hours")
# print("total_leave_days':",y1+y2+y3)


# xa1=emp_dict[101]["attendances"][0].get("hours")
# hours_sum=functools.reduce(lambda a,b:a+b,xa1)
# print("day 1:=",hours_sum)
#
# xa2=emp_dict[101]["attendances"][1].get("hours")
# hours_sum1=functools.reduce(lambda a,b:a+b,xa2)
# print("day 2:=",hours_sum1)
#
# xa3=emp_dict[101]["attendances"][2].get("hours")
# hours_sum2=functools.reduce(lambda a,b:a+b,xa3)
# print("day 3:=",hours_sum2)
from functools import reduce

# for i in range(0,10):
#     sum(emp_dict[101]["attendances"][i].get("hours"))
