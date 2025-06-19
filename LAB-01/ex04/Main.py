from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()
while (1 == 1):
    print("\nCHUONG TRINH QUAN LY SINH VIEN")
    print("*******************MENU*******************")
    print("*** 1. Them sinh vien                 ***")
    print("*** 2. Cap nhat sinh vien            ***")
    print("*** 3. Xoa sinh vien                  ***")
    print("*** 4. Tim kiem sinh vien            ***")
    print("*** 5. Sap xep sinh vien              ***")
    print("*** 6. Hien thi danh sach sinh vien  ***")  
    print("*** 0. Thoat                          ***")
    print("****************************************")  
    
    key = int(input("Nhap lua chon: "))
    if key == 1:
        print("\n1. Them sinh vien")
        qlsv.nhapSinhVien()
        print("\nThem sinh vien thanh cong!")
    elif key == 2:
        if qlsv.soLuongSV() > 0:
            print("\n2. Cap nhat sinh vien")
            print("Nhap ID sinh vien can cap nhat: ")
            id = int(input())
            qlsv.updateSinhVien(id)
        else:
            print("Khong co sinh vien nao de cap nhat!")
    elif key == 3:
        if qlsv.soLuongSV() > 0:
            print("\n3. Xoa sinh vien")
            print("Nhap ID sinh vien can xoa: ")
            id = int(input())
            if qlsv.deleteByID(id):
                print("\nSinh vien co ID: ", id, "da xoa thanh cong!")
            else:
                print("\n Sinh vien co ID: ", id, "khong ton tai!")
        else:
            print("Danh sach sinh vien rong!")
    elif key == 4:
        if qlsv.soLuongSV() > 0:
            print("\n4. Tim kiem sinh vien")
            print("Nhap ten sinh vien can tim: ")
            name = input()
            searchResult = qlsv.findByName(name)
            qlsv.show(searchResult)
        else:
            print("Danh sach sinh vien rong!")
    elif key == 5:
        if qlsv.soLuongSV() > 0:
            print("\n5. Sap xep sinh  theo diem trung binh")
            qlsv.sortByDiemTB()
            qlsv.show(qlsv.getListSinhVien())
        else:
            print("Danh sach sinh vien rong!")
    elif key == 6:
        if qlsv.soLuongSV() > 0:
            print("\n6. Hien thi danh sach sinh vien theo ten")
            qlsv.sortByName()
            qlsv.show(qlsv.getListSinhVien())
        else:
            print("Danh sach sinh vien rong!")
    elif key == 7:
        if qlsv.soLuongSV() > 0:
            print("\n7. Hien thi danh sach sinh vien")
            qlsv.show(qlsv.getListSinhVien())
        else:
            print("Danh sach sinh vien rong!")
    elif key == 0:
        print("\nBan da thoat chuong trinh!")
        break
    else:
        print("\nKhong co chuc nang nay!")
        print("Vui long nhap lai lua chon!") 
            