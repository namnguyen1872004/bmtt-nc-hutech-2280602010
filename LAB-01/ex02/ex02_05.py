so_gio_lam = float(input("Nhập số giờ làm moi tuan: "))
luong_moi_gio = float(input("Nhập lương mỗi giờ: "))
gio_tieu_chuan = 44
gio_vuot_chuan = max(0, so_gio_lam - gio_tieu_chuan)
thuc_linh = (gio_tieu_chuan * luong_moi_gio) + (gio_vuot_chuan * luong_moi_gio * 1.5)
print(f"so tien thuc linh la: {thuc_linh}")