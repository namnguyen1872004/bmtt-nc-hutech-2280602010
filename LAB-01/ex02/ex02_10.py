def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]
input_str = input("Nhap chuoi: ")
print("Chuoi dao nguoc:", dao_nguoc_chuoi(input_str))