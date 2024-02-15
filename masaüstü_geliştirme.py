from PyQt5.QtWidgets import *
aa = QApplication([])
class Login(QMainWindow):
    def tiklama(self):
       kullaniciadi=self.ka.text()
       sifre=self.pa.text()
       mesaj=QMessageBox()
       dogru_kullaniciadi="eren"
       dogru_sifre="123"
       #print("doğru şifre",dogru_sifre)
       if kullaniciadi==dogru_kullaniciadi and sifre==dogru_sifre:
            mesaj.setText("Merhaba")
            mesaj.exec()
            self.close()
            self.anaekran=Anapencere()
            self.anaekran.show()
       else:
            mesaj.setText("Hata")
            mesaj.exec()
            self.close()
    def tiklama4(self):
        self.close()
    def __init__(self):
        super().__init__()
        icerik=QVBoxLayout()
        icerik.addWidget(QLabel("Kullanıcı adı:"))
        self.ka=QLineEdit()
        icerik.addWidget(self.ka)
        icerik.addWidget(QLabel("Şifre:"))
        self.pa=QLineEdit()
        self.pa.setEchoMode(QLineEdit.EchoMode.Password)
        icerik.addWidget(self.pa)
        bt=QPushButton("Giriş yap:")
        icerik.addWidget(bt)
        bt4=QPushButton("Çıkış")
        icerik.addWidget(bt4)
        bt.clicked.connect(self.tiklama)
        bt4.clicked.connect(self.tiklama4)
        pencere=QWidget()
        pencere.setLayout(icerik)
        self.setCentralWidget(pencere)
#◙//////////////////////////////////////////////////////////////////////////////////
class Ceviri(QMainWindow):
    def tiklama(self):
       metre=self.m.text()
       santimetre=self.cm.text()
       mesaj=QMessageBox()
       if metre == "" and santimetre!="":
            self.m.setText(str(int(santimetre)/100))
       elif (metre!="") and (santimetre ==""):
            self.cm.setText(str(int(metre)*100))
       else:
            mesaj.setText("Hata")
            mesaj.exec()
            #self.close()
    def tiklama_(self):
        self.close()
        self.am=Anapencere()
        self.am.show()
    def __init__(self):
        super().__init__()
        icerik=QVBoxLayout()
        icerik.addWidget(QLabel("Metre"))
        self.m=QLineEdit()
        icerik.addWidget(self.m)
        icerik.addWidget(QLabel("Santimetre"))
        self.cm=QLineEdit()
        icerik.addWidget(self.cm)
        bt=QPushButton("Çevir")
        icerik.addWidget(bt)
        bt.clicked.connect(self.tiklama)
        anbt=QPushButton("Ana Menüye Dön")
        icerik.addWidget(anbt)
        anbt.clicked.connect(self.tiklama_)
        pencere=QWidget()
        pencere.setLayout(icerik)
        self.setCentralWidget(pencere)
#◙//////////////////////////////////////////////////////////////////////////////////
class Index(QMainWindow):
    def tiklama(self):
       boy=self.b.text()
       kilo=self.kg.text()
       mesaj=QMessageBox()
       #self.close()
       if float(kilo)/((float(boy))**2)<18.5:
           mesaj.setText("Zayıf")
           mesaj.exec()
       elif 18.5<(float(kilo)/((float(boy))**2))<25:
           mesaj.setText("Normal")
           mesaj.exec()
       elif 25<(float(kilo)/((float(boy))**2))<30:
           mesaj.setText("Kilolu")
           mesaj.exec()
    def tiklama_(self):
        self.close()
        self.am=Anapencere()
        self.am.show()
    def __init__(self):
        super().__init__()
        icerik=QVBoxLayout()
        icerik.addWidget(QLabel("Boy:(M)"))
        self.b=QLineEdit()
        icerik.addWidget(self.b)
        icerik.addWidget(QLabel("Kilo(KG)"))
        self.kg=QLineEdit()
        icerik.addWidget(self.kg)
        bt=QPushButton("Hesapla")
        icerik.addWidget(bt)
        bt.clicked.connect(self.tiklama)
        anbt=QPushButton("Ana Menüye Dön")
        icerik.addWidget(anbt)
        anbt.clicked.connect(self.tiklama_)
        pencere=QWidget()
        pencere.setLayout(icerik)
        self.setCentralWidget(pencere)
#◙//////////////////////////////////////////////////////////////////////////////////
class Anapencere(QMainWindow):
    def tiklama1(self):
       self.close()
       self.u1=Ceviri()
       self.u1.show()
    def tiklama2(self):
       self.close()
       self.u2=Index()
       self.u2.show()
    def tiklama3(self):
        self.close()
        self.u3=Login()
        self.u3.show()
    def __init__(self):
        super().__init__()
        icerik=QVBoxLayout()
        icerik.addWidget(QLabel("ANAMENÜ"))
        bt1=QPushButton("Metre-Santimetre Çevirici")
        icerik.addWidget(bt1)
        bt2=QPushButton("Boy-Kütle İndeksi Hesaplama")
        icerik.addWidget(bt2)
        self.cm=QLineEdit()
        bt3=QPushButton("Giriş Ekranına Dön")
        icerik.addWidget(bt3)
        bt1.clicked.connect(self.tiklama1)
        bt2.clicked.connect(self.tiklama2)
        bt3.clicked.connect(self.tiklama3)
        pencere=QWidget()
        pencere.setLayout(icerik)
        self.setCentralWidget(pencere)
ekran = Login()
ekran.show()
aa.exec()
