"""
TR:Bu bölümde 3 yöntem denedim.3 yönteminde .exe dosyalarını indirmeniz gerekiyor(chrome ve headless chrome nin .exe dosyaları aynı).
İndirdiğiniz dosyaların güncelliğine,chrome veya headless chrome kullanıyorsanız chrome browserinizin güncel olmasına dikkat edin.
Yoksa hata alabilirsiniz.

1)Chrome(Başlı-Arayüzlü):Chrome arayüzü sayesinde; verinin bulunduğu class ismi,xpath'i,tagı gibi önemli bilgilere ulaştım.Ardından bu 
bilgileri kullanarak projemin tamamını bu yöntemle tamamladım.Deneme aşamasını yani 2-3 kullanıcının verilerini çekerek oluşan hata
ları düzeltme gibi adımları burada gerçekleştirdim.

2)PhantomJS(Arayüzsüz):Projemi Chrome de denediğimde çok yavaş olduğunu farkettim.Ardından arayüzsüz tarayıcı olarak PhantomJS kullandım.
Büyük veri çekerken çok yararlı bir yöntem olduğunu söyleyebilirim.

3)Headless Chrome(Arayüzsüz-Başsız):Bazı araştırmalarım sonucu PhantomJS den daha hızlı olduğunu öğrenip projemi burada da denedim.Benim
bilgisayarımda 150 veriyi daha az bellek kullanarak 2 sn daha hızlı yaptı.

Kod Bölümü:
"""
"""
1)Chrome:
"""
from selenium import webdriver
driver=webdriver.Chrome(r"C:\Users\ABDULLAH\chromedriver.exe")#chromedriver.exe dosyamızın bulunduğu dizininizi yazın.
#(r"C:\Users\ABDULLAH\chromedriver.exe") burada ki r harfi eğik çizgilerin(\) yönünü değiştirir(/)
#("C:/Users/ABDULLAH/chromedriver.exe")=(r"C:\Users\ABDULLAH\chromedriver.exe")


"""
2)PhantomJS:
"""
from selenium import webdriver
driver = webdriver.PhantomJS(r"C:\Users\ABDULLAH\phantomjs.exe")
"""
3)Headless Chrome:
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

schrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080") #Bunun önemini bir yerden screenshot yaptığımda gördüm.Aynı zamanda veri çekerken window_size belirtlimesi gerekir. 
chrome_driver = os.getcwd() +"\\chromedriver.exe"
