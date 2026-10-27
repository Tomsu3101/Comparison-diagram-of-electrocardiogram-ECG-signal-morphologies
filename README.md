<img width="1149" height="545" alt="Comparison table of electrocardiogram (ECG) signal morphologies" src="https://github.com/user-attachments/assets/852f3422-7f72-4cef-921e-89a7ffb2677a" />
[mitbih_test.csv.zip](https://github.com/user-attachments/files/34027343/mitbih_test.csv.zip)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Tùy chỉnh kích thước và phong cách biểu đồ mặc định cho đẹp mắt
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (12, 6)

# Đọc file CSV, không dùng dòng đầu làm tiêu đề vì dữ liệu thuần số
df = pd.read_csv('mitbih_test.csv.zip.csv', header=None)

# Kiểm tra kích thước dữ liệu (số dòng, số cột)
print("Data size:", df.shape)

# Xem 5 dòng đầu tiên
display(df.head())

# Lấy ra tất cả các hàng có nhãn là 0 (Bình thường) và 1 (Bất thường - Supraventricular)
normal_beats = df[df[187] == 0.0]
abnormal_beats = df[df[187] == 1.0]

# Trích xuất dòng dữ liệu đầu tiên của mỗi nhóm, bỏ đi cột nhãn cuối cùng ([:-1])
sample_normal = normal_beats.iloc[0, :-1]
sample_abnormal = abnormal_beats.iloc[0, :-1]

# Khởi tạo khung vẽ
plt.figure(figsize=(14, 6))

# Vẽ đường tín hiệu bình thường (màu xanh)
plt.plot(sample_normal, color='#2c3e50', linewidth=2, label="Nhịp bình thường (Normal)")

# Vẽ đường tín hiệu bất thường (màu đỏ)
plt.plot(sample_abnormal, color='#e74c3c', linewidth=2, label="Rối loạn nhịp (Arrhythmia)")

# Bổ sung thông tin cho trục và tiêu đề
plt.title("So sánh Hình thái học của Tín hiệu ECG", fontsize=16, fontweight='bold')
plt.xlabel("Thời gian (Bước mẫu - Time Steps)", fontsize=12)
plt.ylabel("Biên độ chuẩn hóa (Normalized Amplitude)", fontsize=12)

# Hiển thị chú thích
plt.legend(loc='upper right', fontsize=12)

# Xuất đồ thị
plt.show()
