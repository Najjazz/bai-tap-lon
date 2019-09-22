# Bài tập em tham khảo từ nguồn và có thực hiện code lại theo mẫu
# Link: https://theailearner.com/2019/04/10/histogram-matching-specification/?fbclid=IwAR2vB9NOneK823h4KIeSsHbwcH7tirnKDjAuluVFWIASkV9AbBoiDpr5vgs

import cv2
import numpy as np

# Hàm ánh xạ
def find_nearest_greater(my_array, target):
    diff = my_array - target
    mask = np.ma.less_equal(diff, -1)
    # Mask giá trị nghịch đảo
    if np.all(mask):
        result = np.abs(diff).argmin()
        return result 
    # trả lại vị trí gần nhất mà target lớn hơn giá trị của nó
    masked_diff = np.ma.masked_array(diff, mask)
    return masked_diff.argmin()

# Hàm matching
def histogram_matching(source, template):

    source_copy = source.shape
    source = source.ravel()
    template = template.ravel()

    # get the set of unique pixel values and their corresponding indices and counts
    s_values, fixed_num, s_counts = np.unique(source, return_inverse=True,return_counts=True)
    t_values, t_counts = np.unique(template, return_counts=True)

    # Tính s(k) cho source
    s_quantiles = np.cumsum(s_counts).astype(np.float64)
    s_quantiles /= s_quantiles[-1]
    
    # Tính s(k) cho template
    t_quantiles = np.cumsum(t_counts).astype(np.float64)
    t_quantiles /= t_quantiles[-1]

    # Làm tròn giá trị
    sour = np.around(s_quantiles*255)
    temp = np.around(t_quantiles*255)
    
    # Ánh xạ và làm tròn các giá trị
    temp_arr=[]
    for data in sour[:]:
        temp_arr.append(find_nearest_greater(temp,data))
    temp_arr= np.array(temp_arr,dtype='uint8')

    return temp_arr[fixed_num].reshape(source_copy)
 
# Tải ảnh vào dưới dạng gray scale
source = cv2.imread('moto.jpg',0)
template = cv2.imread('window.jpg',0)
 
# Thực hiện Histogram Matching
result = histogram_matching(source, template)
 
# Lưu hình ảnh đã matching lại
cv2.imwrite('after_matching.jpg',np.array(result,dtype='uint8'))
