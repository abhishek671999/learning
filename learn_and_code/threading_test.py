order = int(input("Please enter the order of matrix  you want to convert i.e 1.3*3 2.4*4 3.5*5  "))
if order == 1:
    seperator = 3
elif order == 2:
    seperator = 4
elif order == 3:
    seperator = 5


length = seperator * seperator
input_list = []
output_list = []
for input_elements in range(length):
    integer = input("Enter a number: ")
    input_list.append(integer)

temp = seperator
for x in range(seperator):
    input_num = input_list[temp-seperator:temp]
    output_list.append(input_num)
    temp = temp + seperator
print("Matrix before interchanging diagonals")
print(output_list)


def inter_change_diagonals(array):
    for input_fill in range(seperator):
        if input_fill != seperator / 2:
            temp = array[input_fill][input_fill]
            array[input_fill][input_fill] = array[input_fill][seperator - input_fill - 1]
            array[input_fill][seperator - input_fill - 1] = temp
    print("Matrix after interchanging diagonals")
    for row in range(seperator):
        for column in range(seperator):
            print(array[row][column], end=" ")
        print()
    return array


print(inter_change_diagonals(output_list))