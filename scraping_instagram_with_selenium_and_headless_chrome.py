"""
TR:
Projenin Amacı:instagrambot dosyası içinde ;kisiler.txt adındaki dosya da bulunan kullanıcı adlarına sahip kisilerin bilgilerini bilgiler.txt 
dosyasına yazan ve resimleri instagrambot dosyası içine indiren bir program gerçekleştirdim.Projemi ilk, başlı(arayüzlü) tarayıcıda deneyip 
düzeltilmesi gereken yerleri düzelttim.Ardından daha hızlı çalışan Headless Chrome(Başsız-Arayüzsüz) de çalıştırdım.
Bütün bilgiler instagrambot dosyası içine kaydedildi.

bilgiler.txt dosyasının yapısı;
bilgi_sayisi<->kullanici_adi<->kullanici_idsi<->resmin_yuklenme_tarihi<->resim_açıklama_yorumu<->resime_instagramın yorumu<->resim_urlsi
.... Yukarıda ki satır şeklinde satır satır bütün verileri çektim. 

kisiler.txt dosyasının yapısı;
abdullahharuntahtali
tahtalitekstil
...

KOD:
"""
#Program da değiştirilmesi gereken dizinleri değiştirmeyi unutmayın!

#Gerekli kütüphaneler import edildi.
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import urllib.request
import os
import json, requests
import time
import random



class Instagram_Bot:
    #Bu ana metod Headless Chrome'yi aktif eder ve bilgiler değişkeni adı altında dictionary(sözlük) tanımlar.
    #bilgi değikenindeusername ve userid değişkenlik göstermeyeceğinden string tipinde aldım.Fakat resim yüklenme tarihi,instagramın 
    #yapay zekasının resime yaptığı yorum(alt) v.s bilgiler değişkenlik gösterdiğinden liste halinde tuttum.
    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument("--headless")
        self.chrome_options.add_argument("--window-size=1920x1080")
        self.chrome_driver = os.getcwd() +"\\chromedriver.exe"
        self.driver = webdriver.Chrome(chrome_options=self.chrome_options, executable_path=self.chrome_driver)   

        self.bilgiler={
        "username":"",
        "userid":"",
        "date":[],
        "alt":[],
        "comment":[],
        "imageurl":[]       
                }

    #Bu fonksiyon kullanıcının resim sayısını buluyor.Çünkü "username_userid_date_url_text" adlı fonksiyonda verileri
    #çekerken for döngüsünün ne kadar dönmesi gerektiğini belirtmemiz gerekir.Bu iş parçasınıda bu fonksşyon gerçekleştirir.
    def imagesayisi(self,username):
        self.driver.get('https://www.instagram.com/'+username+'/')
        time.sleep(2)
        number =self.driver.find_element_by_css_selector('.g47SY ')
        number=number.text
        number=number.replace(".","")
        number=number.replace(",","")
        number=int(number)
        print(username+" =  ",number," adet fotoğrafı bulunmaktadır")        
        return number
    
    #Bu fonksiyon her kullanıcıda bir defa çalıştırılır.
    def user_id(self,username):      
        response = requests.get("https://www.instagram.com/"+username+"/?__a=1").text
        x=json.loads(response)
        userid=x["logging_page_id"]
        userid=userid[12:]
        print(userid[12:])
        return userid
             
    
    
    #Projede ki en önemli fonksiyonum.Biraz karmaşık gelebilir.Karmaşık gelmesinin sebebi try except bloklarının içiçe ve çok olmasın-
    #dan kaynaklanıyor.Sebebi ise bazen internet kesilebilir,instagram bir sayfada takılabilir veya yorum alırken # karakteri ile
    #başlayan yorumlar ile diğer yorumların bulunduğu dizin aynı olmadığından hata almamak,sonsuz döngüye girmemek için try except
    # blokları kullandım.Bot olduğumuz anlaşılmasın diye de sleep() metodunu random atadım.
    #Adım adım anlatmaya çalışacağım.
    
    def username_userid_date_url_text(self,username):
        userid=self.user_id(username) #user_id fonksiyonuna gidip kullanıcın idsini elde ediyoruz.
        number=int(self.imagesayisi(username))#for döngümüzün resim sayısı kadar dönmesi gerekir.imagesayisi fonk. bize sayıyı döndürüyor.
        self.bilgiler["username"]=username #sözlüğümüze(dictionary) kullanıcı adını ekliyoruz.
        self.bilgiler["userid"]=userid #sözlüğümüze(dictionary) kullanıcı kimliğini(id) ekliyoruz.
        
        #for a kadar olan bölüm kullanıcının profiline gitmemizi ardında ilk fotoğrafa tıklayıp açmamızı sağlıyor.
        #Try except bloğunda yazmamın sebebi elektrik kesildiğinde
        #kod hata vermesin ve elektriklerin gelmesine kadar olduğu yerde kalsın veya engel yediğimizde engel kalkana kadar
        #devam etsin diye sonsuz döngü içinde yazdım. 
        #Kullanıcının profili  gelince ilk fotoğrafa tıklar ve açılmasını bekler.Açılınca sonsuz döngüden çıkar.
        #sleep() metodunu random atayarak bot olduğumu gizlemeye çalıştım.
        okundumu=False
        while okundumu==False:
            self.driver.get('https://www.instagram.com/'+username+'/')
            try:
                time.sleep(random.randint(1,4))
                image =self.driver.find_element_by_css_selector('.eLAPa').click()# İlk fotoğrafa tıklayan kod
                time.sleep(random.randint(1,4))
                okundumu=True
            except:
                self.driver.get('https://www.instagram.com/'+username+'/')
                continue
        

        #Bu for döngüsü sayesinde fotoğraflara,kullanıcının fotoğraf açıklama yorumlarına,instagramın fotoğrafa yaptığı yorumlara
        #fotoğraf tarihlerine ve urllerine ulaşıp çekiyoruz.Yukarıda ilk fotoğrafa tıklandığı için döngünün 0. indexi ilk fotoğraf
        #olmuş oldu.
        
        for i in range(number):
            try:
               #while döngüsüne kadar olan bölüm sorunsuz çalışır.Çünkü her fotoğrafın urlsi ve tarihi aynı yerdedir.Buraya
               #ulaştığına göre bir fotoğraf açıktır.for döngüsünün sonunda diğer fotoğrafa geçiliyor.
               self.bilgiler["imageurl"].append(self.driver.current_url)
               x=self.driver.find_element_by_css_selector('.k_Q0X.NnvRN').find_element_by_tag_name('time')
               self.bilgiler["date"].append(x.get_attribute('title'))               
               
               #Bu while döngüsünde try bloğuna girmeden önce fotoğrafın üstüne tıklanıp img dizinin yenilenmesi sağlanıyor.
               #Bu kodu kullanmadığımda ne kadar başka fotoğraflara geçsemde, img dizininin hiç bir zaman değişmediğini farkettim.
               #Bu hatayı bu kod sayesinde aştım.
               okundumu=False
               while okundumu==False:
                   self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[1]/div/div/div[2]').click()
                   #try except bloğunda resimleri masaüstümdeki instagrambot dosyasına kaydettim ve instagramın resime yaptığı yorumu
                   #sözlüğümüze(dictionary) ekliyoruz.
                   try:
                       time.sleep(random.randint(1,3))
                       x=self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[1]/div/div/div[1]/img')
                       #Fotoğrafı kaydetmek istediğiniz dizini değiştirmei unutmayın.
                       urllib.request.urlretrieve(x.get_attribute('src'),"C:/Users/ABDULLAH/Desktop/instagrambot/"+ username+"."+self.user_id(username)+"-"+str(i)+".png")
                       self.bilgiler["alt"].append(str(x.get_attribute('alt')))
                       okundumu=True
                   except:
                       continue
               #print(x.get_attribute('alt'))     

               
               #yorum alırken # karakteri ile başlayan yorumlar ile diğer yorumların bulunduğu dizin aynı olmadığından
               #try except bloğu ile olası hatayı önledim.
               try:                                
                   x=self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/div[1]/ul/div/li/div/div/div[2]/span')
                   self.bilgiler["comment"].append(x.text)
                   #print(self.bilgiler["comment"])
               except:
                   try:   
                       x=self.driver.find_element_by_css_selector('.C4VMK').find_elements_by_tag_name('.span')
                       self.bilgiler["comment"].append(x.text)                                 
                   except:                       
                       self.bilgiler["comment"].append("")
               
               #Bu komut sağ tıklayarak bir sonraki fotoğrafa geçmemizi sağlar.İşte burada bir ileri gittiğimizde sayfa gelmezse
               #sola tıklayarak bir önceki sayfaya gidip tekrar sağa tıklar.Bu sayede elektrik kesintilerinde v.b sıkıntılarda
               #sonsuz döngüde bekler.
               self.driver.find_element_by_css_selector('.HBoOv.coreSpriteRightPaginationArrow').click()
               okundumu=False
               while okundumu==False:
                   time.sleep(random.randint(1,4))
                   try:
                       self.driver.find_element_by_css_selector('.k_Q0X.NnvRN').find_element_by_tag_name('time')
                       okundumu=True

                   except:
                       self.driver.find_element_by_css_selector(".qSTh6.coreSpriteLeftPaginationArrow").click()
                       time.sleep(random.randint(1,4))
                       self.driver.find_element_by_css_selector('.HBoOv.coreSpriteRightPaginationArrow').click()
                       continue
                                                   
               #self.bilgileriyazdir(i)
            #Eğer anormal bir hata hata alırsak yazdırmadan çıkmayalım diye dosyaya yazdırma metodunu burada çağırdım.
            #Aynı zamanda sözlüğü temizler.Çünkü ardından diğer kullanıcı bilgilerini bu sözlük tipindeki değişkene kaydediceğiz.
            except:
                self.bilgileriyazdir(i)
                self.bilgiler={
                        "username":"",
                        "userid":"",
                        "date":[],
                        "alt":[],
                        "comment":[],
                        "imageurl":[]       
                        }
                break
            
    
    #Dictionary(sözlük)e kaydettiğimiz bilgileri bilgiler.txt dosyasına yazdırırız.
    #Kaydetmek istediğiniz dizini değiştirmei unutmayın.
    def bilgileriyazdir(self,index): 
        with open(r"C:\Users\ABDULLAH\Desktop\instagrambot\bilgiler.txt","a",encoding="utf-8") as dosya :
            dosya.write(str(index)+"<<->>"+self.bilgiler["username"]+"<<->>"+self.bilgiler["userid"]+"<<->>"+self.bilgiler["date"][index]
            +"<<->>"+self.bilgiler["alt"][index]+"<<->>"+self.bilgiler["comment"][index]+"<<->>"+self.bilgiler["imageurl"][index]+"\n\n")    


                
a=Instagram_Bot()#Classı mızı çağırırız.
#bilgiler.txt dosyasını çağırırız.İçinde verilerinin çekilmesini istediğimiz kullanıcı adları mevcut.
with open(r"C:\Users\ABDULLAH\Desktop\instagrambot.\kisiler.txt","r",encoding="utf-8") as kisi :#Dizini değiştirmei unutmayın.
    x=kisi.readlines()#bilgiler.txt dosyasını satır satır listeye atarız.
    for i in range(len(x)):
        x[i]=x[i].replace("\n","")#Kullanıcı adlarının sonundaki \n karakterlerini sileriz.
        a.username_userid_date_url_text(x[i])#Bu komut ile veri çekme işlemi başlar.
   
