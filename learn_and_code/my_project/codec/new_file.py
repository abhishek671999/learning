# import base64
# import json
#
# with open("codec_file.py", "rb") as image_file:
#     encoded_string = base64.b64encode(image_file.read())
#
# print(type(encoded_string))
# encoded_string = encoded_string.decode('utf-8')
#
# print('0', encoded_string)
#
# temp_dict = {'test': encoded_string}
# print('1', temp_dict)
# print(type(temp_dict['test']))
#
# json_form = json.dumps(temp_dict)
# print('2', json_form)
#
# original_form = json.loads(json_form)
# print('3', original_form)
#
# original_string = bytes(original_form['test'], 'utf-8')
# print('4', original_string)
# print(type(original_string))
#
# with open('new_file.py', 'wb') as write_file:
#     write_file.write(base64.b64decode(original_string))
import importlib

abc = importlib.import_module('..ftp.test_function.py'.strip('.py'))
print(abc.print_hello())