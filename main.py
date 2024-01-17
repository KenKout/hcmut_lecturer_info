import json
import re
import requests

data = requests.get('https://www.grad.hcmut.edu.vn/gv/gv/tra_cuu_ttgv.php')
data_khoa = re.findall(r'getDSGV\("(.{0,9})"\)', data.text)
print(data_khoa)

data_crawl_teacher = []
for i in data_khoa:
    data = requests.post(f'https://www.grad.hcmut.edu.vn/gv/gv/tra_cuu_ttgv_process.php?w=bm_dsgv_1&m={i}')
    data_crawl_teacher.extend(re.findall(r'getTTGV\(\'(.{0,9})\'\)', data.text))
    #print(data_crawl_teacher)

info_teacher = []
for i in data_crawl_teacher:
    data = requests.post(f'https://www.grad.hcmut.edu.vn/gv/gv/tra_cuu_ttgv_process.php?w=mcb_ttgv&m={i}')
    html_code = data.text
    name = re.findall(r"Họ và tên:.+<b>(.*?)</b>", html_code)
    phone = re.findall(r"Điện thoại liên hệ: (.*?)</td>", html_code)
    email = re.findall(r"Email: (.*?)</td>", html_code)
    gv_info = {'name': name[0], 'phone': phone[0], 'email': email[0]}
    info_teacher.append(gv_info)
    #print(gv_info)
with open('data_lecturer.json', 'w', encoding='utf-8') as f:
    json.dump(info_teacher, f, ensure_ascii=False, indent=4)
