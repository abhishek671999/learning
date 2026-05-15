# import base64
#
# import rsa
#
# # generate public and private keys with
# # rsa.newkeys method,this method accepts
# # key length as its parameter
# # key length should be atleast 16
# client_publicKey, client_privateKey = rsa.newkeys(512)
# server_publicKey, server_privateKey = rsa.newkeys(512)
#
#
# # this is the string that we will be encrypting
# server_message = "hello geeks"
#
# # rsa.encrypt method is used to encrypt
# # string with public key string should be
# # encode to byte string before encryption
# # with encode method
# encMessage = rsa.encrypt(server_message.encode(),
#                          client_publicKey)
#
# print("original string: ", server_message)
# print("encrypted string: ", encMessage)
#
# # the encrypted message can be decrypted
# # with ras.decrypt method and private key
# # decrypt method returns encoded byte string,
# # use decode method to convert it to string
# # public key cannot be used for decryption
# decMessage = rsa.decrypt(encMessage, client_privateKey).decode()
#
# print("decrypted string: ", decMessage)
#
#
# ## --- client response ----
# client_message = 'Hello Server'
# encrypted_message = rsa.encrypt(client_message.encode(), server_publicKey)
# print('Client message', client_message)
# print('Encrypted Message', encrypted_message)
#
# decrypted_message = rsa.decrypt(encrypted_message, server_privateKey).decode()
# print('Decrypted message', decrypted_message)
#
# print(server_privateKey, server_publicKey, type(server_privateKey), str(server_privateKey))
# class A:
#     def __init__(self):
#         self.a = 1
# obj_a = A()
#
# print(obj_a.__dict__)
# print(server_privateKey.__dict__)
#
#
#
# class SomeClass:
#     def __init__(self):
#         self.var_1 = 1
#         self.var_2 = 'a'+ str(self.var_1.copy())
#
#     def update_var(self):
#         self.var_1 = 2
#         print(self.var_2)
#
# s = SomeClass()
# s.update_var()
import time

#
# some_list = []
#
# some_dict_1 = {'a': 1}
# some_dict_2 = {'b': 2}
# some_dict_3 = {'a': 1, 'b': 2}
# some_list.append(some_dict_1)
# some_list.append(some_dict_2)
# print(some_list)
#
#
# print(some_dict_3)
# print(time.time())
# declaring string variables
# str1 = 'Understanding'
# str2 = 'integers'
# str3 = 'at'
# str4 = 'GeeksforGeeks = '

# declaring list variables
# lst = list((1, 2, 3))
#
# # concatenating strings as well as list
# final_str = "%s" % (lst)
#
# # printing the final string
# print("Concatenating multiple values using Python '%s' operator:\n")
# print(final_str)
# list_of_numbers = ('a', 'b', 'c')
# string_form = '"' + '","'.join(list_of_numbers) + '"'
# print(string_form)
#
# string = "SELECT * FROM node_table_2 WHERE node_id in %s " % list_of_numbers
# print(string)
# import sys
# import time
#
#
# def lambda_function():
#     print("Executing Lambda function", len(sys.argv))
#     n = len(sys.argv)
#     print(sys.argv)
#
#     for i in range(1, n):
#         print(sys.argv[i], end=' ')
#
#     print(total)
#
#
# total = int(sys.argv[1]) + int(sys.argv[2])
# print(total)
#
#
#
# import json
# b = ['.py', '.java']
# print(b, type(b))
# a = json.dumps(b)
# print(a, type(a))

# import socket
# s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# s1.bind(('localhost', 10000))
# s2.bind(('localhost', 10000))

# import queue
# q = queue.Queue(1)
# q.put(1)
# print(q.get(), q.get())
#
# print(q.qsize())
# print(q.not_full)
# print(q.full())
import shelve, os
shelf = shelve.open(os.getcwd())
shelf['task'] = [1, 2]
print(a for a in shelf['task'])
temp_list = shelf['task']
temp_list.append(3)
shelf['task'] = temp_list
print(shelf)
