"""TR:
Bu programı Selenium kütüphanesini öğrenmek için yapmıştım.Bu program için instagramgiris.py dosyası hazırladım.içinde 2 satır kod bulun-
maktadır;
1. satır-->kullaniciadi="kullanici_adiniz"
2. satır-->sifre="sifreniz"
Eğer kendi dosyanızı veya modülünüzü import etmeyi bilmiyorsanız;
 "https://github.com/abdullahharuntahtali/importing_custom_python_my_files_and_modules"   adlı urlden öğrenebilirsiniz.


Kod Kısmı:
"""
#1. asama: Selenium kütüphanesini import edin.
#time kütüphanesini sleep işlemi için import edin.sleep işlemini aralarda kullanmazsanız programınız çalışmaz.
#instagramgiris dosyanızı import edin.
from selenium import webdriver
import time
import instagramgiris
driver=webdriver.Chrome(r"C:\Users\ABDULLAH\chromedriver.exe")

#instagram.com sitesine gidip ardından 2 sn bekledik.Beklemezsek içerideki yapı değişmeden diğer kodu çalıştırmış oluruz.
#classi,xpath v.s daha gelmediği için hata verir.
driver.get("https://www.instagram.com/")
time.sleep(2)

#Üye ol,giriş yap kısmından giriş yapıp seçip; kullanıcı adı ve şifre istenilen sayfaya ulaşmamızı sağlayan kod parçası
giris_yap=driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[2]/p/a")
giris_yap.click()
time.sleep(3)

#Giriş yap ekranındaki kullanıcı adı ve şifre bölümünü instagramgiris.py dosyamız sayesinde otomatik olarak doldurup
#İnstagram ana sayfamıza gitmemizi sağlayan kod parçası
kullanici_adi=driver.find_element_by_name("username")
sifre=driver.find_element_by_name("password")
kullanici_adi.send_keys(instagramgiris.kullaniciadi)
sifre.send_keys(instagramgiris.sifre)
giris_butonu=driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[4]/button/div")
giris_butonu.click()
time.sleep(2)

#Ardından bildirimleri aç diye uyarı geldiğinde bu kod o uyarıyı kapatmamızı sağlar.
uyarı_kapatma_butonu=driver.find_element_by_css_selector(".aOOlW.HoLwm ").click()
time.sleep(1)

#Bu kod parçası profil sayfamıza gitmemizi sağlar.
profil=driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[3]/a/span")
profil.click()
time.sleep(2)

#Bu kod profil sayfamızdaki ayarlar segmesini açar.
ayarlar=driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[1]/div/button")
ayarlar.click()
time.sleep(2)

#Bu kod ayarlar segmesindeki çıkış butonuna basarak instagramdan çıkışı sağlar
cikis_butonu=driver.find_element_by_xpath("/html/body/div[3]/div/div/div/button[6]")
cikis_butonu.click()
time.sleep(5)

#Bu kodda açılan tarayıcıyı kapatır.
driver.close()
