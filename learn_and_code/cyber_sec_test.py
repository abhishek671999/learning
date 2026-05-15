# import threading
# import subprocess
# # from requests import HttpResponse
#
#
# def show_data():
#
#     list_url = ["http://192.168.4.86:3000/","https://bobbyhadz.com/","https://pythonexamples.org/","http://testphp.vulnweb.com/"]
#
#     thread_list=[]
#
#     for x in list_url :
#         thread = threading.Thread(target=nikto_data, args=(x,))
#         thread_list.append(thread)
#
#     for thread in thread_list:
#         thread.start()
#
#     for th in thread_list:
#         th.join()
#         # thread_list[-1].join()
#
#     # return HttpResponse("hello")
#
#
# def nikto_data(x):
#     try:
#             # global count
#             count = 1
#             # cmd = "nikto -host {0}-o scan_output.txt".format(x)
#             # print(cmd)
#
#             # print("step-4", x)
#             # pl = subprocess.Popen(["powershell","wsl -d Ubuntu-20.04","--exec " + cmd],stdout=subprocess.PIPE,universal_newlines=True)
#             # main_lis = []
#             # for new in pl.stdout:
#             #     main_lis.append(new)
#             file_name = f'output_file{count}.json'
#             with open(file_name,'w+') as file:
#                 # for x in main_lis:
#                 #     file.write("%s\n" % x)
#                 count += 1
#                 print('value of x: ' + x + ' || value of count: ' + str(count) + ' ')
#             print("step-6")
#
#     except Exception as e :
#         print(e)
#
#
# show_data()


a = [1,2,3,4,5]
print({}.fromkeys(a, 1))
