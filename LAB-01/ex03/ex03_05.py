def dem_so_lan_xuat_hien(lst):
    """
    Hàm này nhận vào một chuỗi s và trả về một từ điển với các ký tự trong chuỗi là khóa
    và số lần xuất hiện của chúng là giá trị.
    """
    count_dict = {}
    for char in lst:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    return count_dict

input_string = input("Nhap danh sach cac tu, cach nhau bang dau cach: ")

word_list = input_string.split()

so_lan_xuat_hien = dem_so_lan_xuat_hien(word_list)
print("So lan xuat hien cua cac phan tu: ", so_lan_xuat_hien)