"""TR:Kullanıcının kaç fotoğrafı olduğunu döndüren bir fonksiyon



KOD:
"""
#import edilmesi gereken kütüphaneler
from selenium import webdriver
import time

#Tarayıcıyı açan kod
driver =webdriver.Chrome(r"C:\Users\ABDULLAH\chromedriver.exe")

#Fotoğraf sayısını çekmek istediğiniz kullanıcının, kullanıcı adını username değişkenine yazın
#Örnek:Kullanıcı adı:abdullahharuntahtali ise--> driver.get('https://www.instagram.com/abdullahharuntahtali/') 
username="abdullahharuntahtali"
driver.get('https://www.instagram.com/'+username+'/')
time.sleep(2)

#Fotoğraf sayısını öğrendiğimiz kod.String olarak alıyoruz.
number =self.driver.find_element_by_css_selector('.g47SY ')
number=number.text

#Şuan fotoğraf sayısını aldık.İnstagram 4 rakamlı sayılar ve üzerinde virgüllü veya noktalı(1500) veriyor.Stringlerdeki replace 
#fonksiyonu sayesinde sayıyı noktasız yahut virgülsüz hale getiriyoruz.Ardından Stringi integer e çeviriyoruz.
number=number.replace(".","")
number=number.replace(",","")
number=int(number)

#Ekrana--> "abdullahharuntahtali =  x(mesela 10) adet fotoğrafı bulunmaktadır"  diye çıktı verir. 
print(username+" =  ",number," adet fotoğrafı bulunmaktadır")        
