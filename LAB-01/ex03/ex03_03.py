def tao_tuple_tu_list(lst):
    """
    Hàm này nhận vào một danh sách và trả về một tuple chứa các phần tử của danh sách đó.
    """
    return tuple(lst)
input_list = input("Nhap danh sach so nguyen, cach nhau boi phay: ")
numbers = list(map(int, input_list.split(",")))

my_tuple = tao_tuple_tu_list(numbers)
print("List: ", numbers)
print("Tuple tu danh sach la:", my_tuple)