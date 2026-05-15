# import subprocess
# cmd = 'python subscript.py'
#
# p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
# out, err = p.communicate()
# result = out.split(b'\n')
# for lin in result:
#     if not lin.startswith(b'#'):
#         print(lin)

# import yaml
# config = yaml.safe_load(open('test_yaml.yml', 'r'))
# print(config)


# import subprocess
#
# list_dir = subprocess.Popen(['python', 'subscript.py'], stdout=subprocess.PIPE)
# output = list_dir.communicate()
# list_dir.wait()
# print(output[0].decode('utf-8')+'--')

# Python code to demonstrate enumerations

# importing enum for enumerations
import enum


# creating enumerations using class
# class Animal(enum.Enum):
#     dog = 'dog'
#     cat = 2
#     lion = 3
#
#
# # printing enum member as string
# print("The string representation of enum member is : ", end="")
# print(Animal.dog)
#
# # printing enum member as repr
# print("The repr representation of enum member is : ", end="")
# print(repr(Animal.dog))
#
# # printing the type of enum member using type()
# print("The type of enum member is : ", end="")
# print(type(Animal.dog))
#
# # printing name of enum member using "name" keyword
# print("The name of enum member is : ", end="")
# print(Animal.dog.name)
# a = Animal.dog
# print(a.value)

# from queue import Queue
#
# a_queue = Queue(5)
# a_queue.put(1)
# print(a_queue.qsize())

import datetime, shelve

# Restore saved data
# import os
# print(os.getcwd())
#
# shelf = shelve.open(os.getcwd())
# # word_list = shelf['word_list']
# # last_run = shelf['last_run']
# # # Work with the restored values
# # print("Resuming. Last run {}".format(last_run))
# # print("Word list: {}".format(word_list))
# # word_list += input('More words please:').split()
# # # Update shelf and close (write to disk)
# # shelf['last_run'] = datetime.datetime.now()
# # shelf['word_list'] = 'abhishek'
# print(shelf['last_run'])
# print(shelf['word_list'])
# shelf.close()
# import os
#
# import subprocess
# from sys import stderr
# name = 'java_files/test_java_prog.java'
# process = subprocess.Popen(['javac', name ], stderr=subprocess.PIPE, stdout=subprocess.PIPE)
# output, error = process.communicate()
# print('Next line', output, error)
# if not len(error):
#     class_dir = name.rstrip('java')+'class'
#     cmd_0 = 'tree;'
#     cmd_1 = 'cd java_files &&'
#     cmd_2 = 'java test_java_prog'
#     cmd = cmd_1 + cmd_2
#     print(class_dir)
#
#     print('below this')
#     os.system(cmd_0)
#     print('above this')
#
#     process = subprocess.Popen(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
#     # process.wait(2)
#     print('Wait completete')
#     output, error = process.communicate()
#     print('Next line', output, error)
#
# else:
#     print('An error occurred while compiling')
#

# print(output, error)
# process = subprocess.Popen('java A')

#
# # output = subprocess.getoutput('java A')
# print('return code', exec.returncode)
# exec.kill()
# from datetime import datetime
# print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
#
# now = datetime.now()
# date_time = now.strftime("%m-%d-%Y %H:%M:%S")
# print("date and time:",date_time)
# import json
#
# import mysql.connector
#
# mydb = mysql.connector.connect(
#     host='localhost',
#     username='root',
#     database='mydatabase'
# )
#
# print(mydb.is_connected())
# cursor = mydb.cursor(dictionary=True)
# query = "SELECT * FROM `task_table` WHERE task_id=184"
#
# cursor.execute(query)
# result = cursor.fetchall()[0]['task_parameters']
# arr = json.loads(result)
# print(arr[1])


# from queue import Queue
#
# q = Queue(2)
# q.put((1, 2))
# ans = q.get()
# print(type(ans))


# import multiprocessing
# import time
# from queue import Queue
# q = Queue(1)
# # bar
# def bar(q2):
#     for i in range(5):
#         print("Tick")
#         time.sleep(1)
#     else:
#         q2.put(1)
#
# if __name__ == '__main__':
#     # Start bar as a process
#     p = multiprocessing.Process(target=bar, args=(q, ))
#     p.start()
#
#     # Wait for 10 seconds or until process finishes
#     return_val = p.join(10)
#     print(q)
#
#     # If thread is still active
#     if p.is_alive():
#         print("running... let's kill it...")
#
#         # Terminate - may not work if process is stuck for good
#         p.terminate()
#         # OR Kill - will work for sure, no chance for process to finish nicely however
#         # p.kill()
#
#         p.join()
# import threading
# import time
#
#
# def test_function_thread_1(lock_1):
#     local_var = 1
#     for i in range(10000000):
#         local_var += 1
#     print('Name', threading.current_thread().name)
#
# def test_function_thread_2(lock_2):
#     print('Entered function 2')
#     blocking_value = lock_2.acquire(blocking=False)
#     print('In block 2', blocking_value)
#     print('Printing in function 2')
#     time.sleep(5)
#     print('Releasing lcok in block 2')
#     lock_2.release()
#
#
# lock = threading.Lock()
# t1 = threading.Thread(target=test_function_thread_1, args=(lock,), name='t1')
# t2 = threading.Thread(target=test_function_thread_1, args=(lock, ), name='t2')
# t1.start()
# t2.start()
# time.sleep(1)
# print('Inside main')


try:
    raise Exception
except Exception as err:
    err.status_code = 100
    print(err.__dict__)

