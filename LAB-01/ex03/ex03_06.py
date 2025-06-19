def xoa_phan_tu(dictionary, key):
    """
    Hàm này nhận vào một từ điển và một khóa, và xóa phần tử có khóa đó khỏi từ điển.
    """
    if key in dictionary:
        del dictionary[key]
    else:
        print("Khóa không tồn tại trong từ điển.")
    return dictionary

my_dict = { 'a': 1, 'b': 2, 'c': 3 }
key_to_delete = 'b'
result = xoa_phan_tu(my_dict, key_to_delete)
if result:
    print("Từ điển sau khi xóa phần tử:", my_dict)
else:
    print("Không có phần tử nào được xóa.")