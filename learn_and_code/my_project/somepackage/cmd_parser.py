# import argparse
#
# parser = argparse.ArgumentParser(description='Test arg parser')
# parser.add_argument('-exec', dest='exec', action='store_true')
# parser.add_argument('-f', dest='file_name', metavar='filename', type=str, help='To execute a file, enter file name')
#
# parser.add_argument('-query', dest='query', action='store_true')
# parser.add_argument('-id', dest='task_id', metavar='task_id', type=int, help='To query status of the task')
#
# parser.add_argument('-result', dest='result', action='store_true')
# parser.add_argument('-id', dest='task_id', metavar='task_id', type=int, help='To get the result of the query')
#
# args = parser.parse_args()
# print(args)

# def abc():
#     pass
# import argparse
#
# parser = argparse.ArgumentParser(description='Process some integers.')
# parser.add_argument('integers', metavar='N', type=int, nargs='*',
#                     help='an integer for the accumulator')
# parser.add_argument('--sum', dest='accumulate', action='store_const',
#                     const=sum, default=max,
#                     help='sum the integers (default: find the max)')
#
# args = parser.parse_args()
# print(args)
# print(args.accumulate(args.integers))

import argparse

parser = argparse.ArgumentParser()
subparser = parser.add_subparsers(dest='action')

exec_parser = subparser.add_parser('exec')
exec_parser.add_argument('file_name', type=str)

query_parser = subparser.add_parser('query')
query_parser.add_argument('task_id', type=int)

result_parser = subparser.add_parser('result')
result_parser.add_argument('task_id', type=int, nargs='+')
result_parser.add_argument('id', type=int)

print(parser.parse_args(), type(parser.parse_args()))