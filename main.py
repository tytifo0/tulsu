import requests
from bs4 import BeautifulSoup
import requests as req

def auth_request(username, password):
 response = requests.post("http://10.100.211.150/deloedu_test/CoreHost/auth/login", data={
 "username": username,
 "password": password
 })
 return response


username = "Елисеев"
password = "Qwerty1234"
response = auth_request(username, password)
if response.status_code == 200:
 print("авторизация прошла успешно")
 url = 'http://10.100.211.150/deloedu_test/WebRc/DOC_RC/DOC_RC.aspx#regParamsЯ%7B%22isn_prj%22:9338149,%22kind_doc%22:7,%22dg%22:%220.LIGI.LIHG.MOTJ.P9PO.%22,%22date%22:%2217.07.2024%2016:32:18%22,%22unlockCommand%22:%22UnlockObjects%3FobjectList%3D9338149%3A7%26card_id%3D0.PP6A.PP6G.PP76.%26cabinet_id%3D1199189%26current_dl%3D%22,%22regFromPrj%22:1%7DЧcard_idЯ0.PP6A.PP6G.PP76.Чcabinet_idЯ1199189Чcurrent_dlЯ'

 response = requests.get(url)
 soup = BeautifulSoup(response.content, 'html.parser')
 title = soup.title.text

 # Создаём файл, если он не существует
 file_path = 'output.txt'

 # Открываем файл для записи
 with open(file_path, 'w') as file:
  file.write(title)
  print(f'Заголовок страницы успешно сохранён в файл {file_path}')
