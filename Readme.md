# Vadeli Mevduat Katılım Verileri ile Sınıflandırma ve Analiz

Bu işe alım projesinde hedef eldeki verileri bir yapay zeka algoritmasıyla sınıflandıran ve tahmini yapan model geliştirmek. Ayrıca eldeki verileri kullanarak anlamlı sonuç çıkarımı sağlamaktır.


# Sınıflandırıcı Algoritması

Proje sürecinde yapay zeka ile veri tahmin modellemeleri yapan birçok algoritma bu veriseti üzerinde denenmiştir. Kıstas olarak bize sunulan başarı oranı ( 5 çapraz doğrulama ile) %81 'i sağlayan algoritma **MLPC (Multi-layer Perceptron classifier)** olduğu belirlenmiştir. Eğitim verileri modele girdi olarak verildiğinde sonuç, aşağıda ki görselde de belirtirldiği gibi %92 başarım oranı olarak tespit edilmiştir. 

![Model başarı oranı](https://ibb.co/KhskQjZ) 


## Sunulan Verilerden Anlamlı Bilgiler Çıkarma

Yazının devamında görseller ile de desteklenen müşterilerin mevduat ürününü alması adına yapılan çalışmaların görselleştirmelerinin incelenmesi sonucu ; 

1- Etkili sonuç alma yaşı **26-39** arası yaş grubu olarak belirlenmiştir.
2- Yıllık bakiye ortalamaları **düşük** çalışma grubu ürünü almaya daha yatkındır.
3- Meslekle ilgili genel yorum yapmak gerekirse, "Ev hanımı" "Öğrenci" ve "Girişimci"'lere ürünü satma potansiyeli çok düşüktür. Daha çok yöneticiler,şirket sahipleri ve mavi yakalılara yönelinmelidir.
4- Müşterilerin daha önceden kredi sahibi olmaları bu ürünü almalarını olumsuz etkilemiştir. Daha önceden kredisi **olmayan** müşteriler tercih edilmelidir.
5-Evli olan müşterilerin bu mevduatı alma potansiyelleri bekar ve boşanmış olan müşterilere göre daha yüksektir.
6-Eğitim seviyesi lise-orta okul olan müşterilerin ürünü alma potansiyeli diğerlerine göre **daha yüksektir.**
7- Müşterilerin ev kredilerinin olup/olmaması ürünün alınma potansiyelini **değiştirmemektedir.**
8-Müşteri potansiyeli belirlenen grup 2'den fazla aranmamalıdır. **2'den** fazla aranan müşterilerde olumlu sonuç oranı **çok düşük** olarak tespit edilmiştir.
9-İletişim süreleri çok uzun tutulmamalıdır. Anlatılacak bilginin en fazla 1000sn. 'de müşteriye verilmesi gerektiği tespit edilmiştir. Sürenin uzaması müşteriyi **olumsuz** etkilemektedir.


### Mevduatı Satın Alan Müşterilerin Yaş Grubu Grafiği

![YasGrafigi](https://ibb.co/pyN71ky)


### Mevduatı Satın Alan Müşterilerin Medeni Durumları ile İlgili Grafik

![marital](https://ibb.co/QQdyLzk)

### Mevduatı Satın Alan Müşterilerin Eğitim Durumları Hakkında Grafik

![education](https://ibb.co/mc7pgDt)

### Mevduatı Satın Alan Müşterilerin Meslek Grupları ile İlgili Grafik

![job](https://ibb.co/vhW3zV3)

### Mevduatı Satın Alan Müşterilerin Bakiye Grafiği

![bakiye](https://ibb.co/cxTZsdQ)

### Mevduatı Satın Alan Müşterilerin Aranma Sayılarını İçeren Grafik

![aranma](https://ibb.co/VTtwvd3)

### Mevduatı Satın Alan Müşterilerin Aranma Sürelerini İçeren Grafik

![duration](https://ibb.co/Q8HG9rR)

### Mevduatı Satın Alan Müşterilerin Daha Önceden Mevduata Sahip Olması Durumunu İçeren Grafik

![default](https://ibb.co/hLkQqbD)


### Mevduatı Satın Alan Müşterilerin Ev Kredisi Olup/Olmama Durumlarını İçeren Grafik

![housing](https://ibb.co/ygCDbkN)


### Mevduatı Satın Alan Müşterilerin Bireysel Kredileri Olup/Olmamaları Hakkında Bilgi İçeren Grafik

![loan](https://ibb.co/Mp2yx5P)


