# to_scrape_data_from_instagram_with_headless_chrome_and_selenium_library


TR:Dosyalar hakkında bilgi ;

1)logging_in_and_out_of_instagram :Bu dosyam da kullanıcı ismi ve şifresi ile instagrama giriş yapmayı gösterdim.Ardından profil sayfamıza
gidip ayarlar butonuna tıklayıp çıkış butonu sayesinde çıkış yapan basit bir uygulama gerçekleştirdim.Deneyimi olmayanların veya fikir sa-
hibi olmak isteyenlerin ilk önce bu kodu incelemelerini tavsiye ederim.Selenium ile yazdığım ilk program.

2)learning_the_number_of_users'_photos:Bu dosyam da instagram da kullanıcının kaç fotoğrafı olduğunu ekrana veren küçük bir uygulama yaptım.

3)pulling_instagram_user _ID:Bu dosyam da kullanıcı ismini aldığımız bir kişinin kullanıcı kimliğini(userID) JSON dosyasından bulan bir program gerçekleştirdim.

4)browser_activation:Bu dosyamda Selenium da denediğim 3 yöntemi(chrome,headless chrome,phantomjs) anlattım.Ve nasıl Seleniumda kullanılacağını gösterdim.Bunlar;

a)Chrome (Başlı-Arayüzlü) :https://chromedriver.chromium.org/downloads İlk aşama olarak chrome tarayıcınızı güncelleyin.Ardından chrome sürümünüze uygun chromedriver.exe dosyasını Anacondanın kurulu olduğu(bulunduğu) dizine (genelde kullanıcı dizininde-Örnek-->Benim dizinim=C:\Users\ABDULLAH) indirin.
-İndirme işleminden sonra;
Windows için:Bilgisayarınızdaki arama yerine "Sistem Ortam Değişkenlerini Düzenleyin" yazın ve tıklayın."Ortam Değişkenleri" butonuna basıp
x(ABDULLAH gibi) için kullanıcı değişkenleri yazan yerde "yeni" tuşuna basıp PYTHONPATH adında değişken adı tanımlayın ve değişken olarak
chromedriver.exe dosyanızın dizinini belirtin.(Benim dizinim-->C:\Users\ABDULLAH\chromedriver.exe)

b)PhantomJS :https://phantomjs.org/download Bu urlden .exe dosyasını indirebilirsiniz.Rar dosyası halinde iner.Bin dosyası içinde .exe mevcuttur.Anacondanın kurulu olduğu dizine(genelde kullanıcı dizininde-Örnek=Benim dizinim-->C:\Users\ABDULLAH) .exe dosyasını indiriniz.
-İndirme işleminden sonra;
Windows için:Bilgisayarınızdaki arama yerine "Sistem Ortam Değişkenlerini Düzenleyin" yazın ve tıklayın."Ortam Değişkenleri" butonuna basıp
x(ABDULLAH gibi) için kullanıcı değişkenleri yazan yerde "yeni" tuşuna basıp PYTONPATH adında değişken adı tanımlayın ve değişken olarak
chromedriver.exe dosyanızın dizinini belirtin.(Benim dizinim-->C:\Users\ABDULLAH\phantomjs.exe)

c)Headless Chrome(Başsız-Arayüzsüz) :Chrome deki aşamalar ile aynıdır. 

5)scraping_instagram_with_selenium_and_headless_chrome:Bu dosyam asıl projemi barındırıyor.Kullanıcının fotoğrafları dahil bütün bilgilerini elde ettiğim program.Açıkçası birçok araştırmalar yaptım.Fakat bulduğum kodlar ya çok uzun veya çok karmaşıktı.Elimden geldiği kadar sadeleştirdim ve yorum satırlarında açıklamaya çalıştım.


*Tavsilerinizi bekliyorum.
