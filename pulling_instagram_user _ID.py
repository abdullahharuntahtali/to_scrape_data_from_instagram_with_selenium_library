"""
TR:
Bu program kullanıcı adını girdiğiniz kişinin kullanıcı kimliğini yani kullanıcı id sini çeker.
En önemli nokta kullanıcının url sinin sonuna ?a__a=1 yazmak(("https://www.instagram.com/abdullahharuntahtali/?__a=1")) 
Bu url sayesinde json dosyasına ulaşıp oradan kişinin idsini bulup çekeriz.



KOD:
"""
#Gerekli Kütüphaneler
from selenium import webdriver
import json, requests
import urllib.request

#chromedriver aktifleştirip,kullanıcının adresine gideriz
driver =webdriver.Chrome(r"C:\Users\ABDULLAH\chromedriver.exe")


#username yerine idsini bulmak istediğiniz kullanıcının, kullanıcı adını giriniz.Bu sayede adresine gidebiliriz.
#Aslında gitmedende yapılır.Hatta daha hızlı çalışır.Görmemiz amacı ile ekledim.
username="abdullahharuntahtali"
driver.get('https://www.instagram.com/tahtalitekstil/?hl=tr') #hl=en yaparsanız sayfa dili ingilizce olur. 
time.sleep(0.5)

#Burada dikkat ettiyseniz url nin sonuna "/?__a=1" ekledik.Bu sayede kullanıcının bilgilerinin bulunduğu json dosyası gelir.
#requests ve json  kütüphanesi sayesinde json yapısının tamamını text olarak alabiliriz.
response = requests.get("https://www.instagram.com/"+username+"/?__a=1").text
x=json.loads(response)


#--> Bu kod ile kullanıcın json yapısını görebilirsiniz.Bu kodu çalıştırmassa-
#nızda olur.Çalıştırırsanız aşağıdaki adımları görebilirsiniz.
driver.get("https://www.instagram.com/"+username+"/?__a=1") 


#{"logging_page_id":"profilePage_1597569073","dadsad":"fadj" ......} gibi json dosyası gelir.Dictionary de olduğu gibi
#userid=x["logging_page_id"] ile "profilePage_1597569073" bilgisini elde ederiz.
#Ardından userid=userid[12:] komutu ile 8517067367 şeklinde idmize ulaşmış oluruz.
userid=x["logging_page_id"] 
userid=userid[12:]
print(userid)
