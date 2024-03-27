import threading
from PyQt5 import QtWidgets 
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QImage  # QtGui modülünü içe aktarın
from Ui_anket import Ui_Form
import sys
import joblib
import pandas as pd
import numpy as np
from PyQt5.QtCore import QTimer


class Window(QtWidgets.QMainWindow):
    
    Q1_score = 0
    Q2_score = 0
    Q3_score = 0
    Q4_score = 0
    Q5_score = 0
    Q6_score = 0
    Q7_score = 0
    Q8_score = 0
    Q9_score = 0
    Q10_score = 0
    Q11_score = 0
    Q12_score = 0
    Q13_score = 0
    Q14_score = 0
    Q15_score = 0
    Q16_score = 0
    Q17_score = 0
    Q18_score = 0
    Q19_score = 0
    Q20_score = 0   
    i=0

    def __init__(self):
        super(Window, self).__init__()  
        self.ui = Ui_Form()
        self.ui.setupUi(self) 
        self.ui.Sonraki.clicked.connect(self.sonraki_sayfa)
        self.ui.Onceki.clicked.connect(self.onceki_sayfa)
        self.ui.Label_.setCurrentIndex(self.i)
        self.ui.anket_sonlandir.clicked.connect(self.anketi_bitir)
        self.ui.sonuclari_gor.clicked.connect(self.sonuclari_gor)        
        self.visblte()  
        # Her checkbox için bir önceki durumu saklamak için bir sözlük kullanalım
        self.prev_checkbox_states = {}
        # QTimer oluşturun ve belirli bir aralıkta updateScore fonksiyonunu çağırın
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.q1_score)
        self.timer.timeout.connect(self.q2_score)
        self.timer.timeout.connect(self.q3_score)
        self.timer.timeout.connect(self.q4_score)
        self.timer.timeout.connect(self.q5_score)
        self.timer.timeout.connect(self.q6_score)
        self.timer.timeout.connect(self.q7_score)
        self.timer.timeout.connect(self.q8_score)
        self.timer.timeout.connect(self.q9_score)
        self.timer.timeout.connect(self.q10_score)
        self.timer.timeout.connect(self.q11_score)
        self.timer.timeout.connect(self.q12_score)
        self.timer.timeout.connect(self.q13_score)
        self.timer.timeout.connect(self.q14_score)
        self.timer.timeout.connect(self.q15_score)
        self.timer.timeout.connect(self.q16_score)
        self.timer.timeout.connect(self.q17_score)
        self.timer.timeout.connect(self.q18_score)
        self.timer.timeout.connect(self.q19_score)
        self.timer.timeout.connect(self.q20_score)
        self.timer.start(1000)

        # Her saniyede bir güncelleme yapacak (1000 milisaniye = 1 saniye)

    def visblte(self):
        self.ui.Onceki.setVisible(False)
        self.ui.sonuclari_gor.setVisible(False)



    def q1_score(self):
        self.Q1_score = 0
        for i in range(1, 11):
            checkbox = getattr(self.ui, f"A{i}_checkBox_Q1")
            if checkbox.isChecked():
                self.Q1_score = self.Q1_score + 0.10
            # Checkbox'un önceki durumunu kontrol edelim
            prev_state = self.prev_checkbox_states.get(checkbox)
            # Eğer önceki durum işaretliyse ve şu an işaretli değilse, puanı azaltalım
            if prev_state and not checkbox.isChecked():
                self.Q1_score -= 0.10
            # Checkbox'un şu anki durumunu önceki durum olarak güncelleyelim
            self.prev_checkbox_states[checkbox] = checkbox.isChecked()

    def q2_score(self):
        for i in range(1, 8):
            radioButton = getattr(self.ui, f"A{i}_radioButton_Q2")
            
            if radioButton.isChecked() and i==1:
                self.Q2_score =0
            elif radioButton.isChecked() and i==2:                
                self.Q2_score = 0.20
            elif radioButton.isChecked() and i==3:                
                self.Q2_score = 0.40
            elif radioButton.isChecked() and i==4:                
                self.Q2_score = 0.60
            elif radioButton.isChecked() and i==5:                
                self.Q2_score = 0.80
            elif radioButton.isChecked() and i==6:                
                self.Q2_score = 0.90
            elif radioButton.isChecked() and i==7:                
                self.Q2_score = 1                
            else:
                None

    def q3_score(self):
        for i in range(1, 6):
            radioButton = getattr(self.ui, f"A{i}_radioButton_Q3")
            
            if radioButton.isChecked() and i==1:
                self.Q3_score =0
            elif radioButton.isChecked() and i==2:                
                self.Q3_score = 0.25
            elif radioButton.isChecked() and i==3:                
                self.Q3_score = 0.5
            elif radioButton.isChecked() and i==4:                
                self.Q3_score = 0.75
            elif radioButton.isChecked() and i==5:                            
                self.Q3_score = 1                
            else:
                None


    def q4_score(self):
        for i in range(1, 7):
            radioButton = getattr(self.ui, f"A{i}_radioButton_Q4")
            
            if radioButton.isChecked() and i==1:
                self.Q4_score =1
            elif radioButton.isChecked() and i==2:                
                self.Q4_score = 0.80
            elif radioButton.isChecked() and i==3:                
                self.Q4_score = 0.6
            elif radioButton.isChecked() and i==4:                
                self.Q4_score = 0.4
            elif radioButton.isChecked() and i==5:                            
                self.Q4_score = 0.2    
            elif radioButton.isChecked() and i==6:                            
                self.Q4_score = 0              
            else:
                None

    def q5_score(self):
        for i in range(1, 6):
            radioButton = getattr(self.ui, f"A{i}_radioButton_Q5")
            
            if radioButton.isChecked() and i==1:
                self.Q5_score =0
            elif radioButton.isChecked() and i==2:                
                self.Q5_score = 0.25
            elif radioButton.isChecked() and i==3:                
                self.Q5_score = 0.5
            elif radioButton.isChecked() and i==4:                
                self.Q5_score = 0.75
            elif radioButton.isChecked() and i==5:                            
                self.Q5_score = 1                
            else:
                None

    def q6_score(self):
        for i in range(1, 6):
            radioButton = getattr(self.ui, f"A{i}_radioButton_Q6")
            
            if radioButton.isChecked() and i==1:
                self.Q6_score =0
            elif radioButton.isChecked() and i==2:                
                self.Q6_score = 0.25
            elif radioButton.isChecked() and i==3:                
                self.Q6_score = 0.5
            elif radioButton.isChecked() and i==4:                
                self.Q6_score = 0.75
            elif radioButton.isChecked() and i==5:                            
                self.Q6_score = 1                
            else:
                None

    def q7_score(self):
        for i in range(1, 6):
            radioButton = getattr(self.ui, f"A{i}_radioButton_Q7")
            
            if radioButton.isChecked() and i==1:
                self.Q7_score =0
            elif radioButton.isChecked() and i==2:                
                self.Q7_score = 0.25
            elif radioButton.isChecked() and i==3:                
                self.Q7_score = 0.5
            elif radioButton.isChecked() and i==4:                
                self.Q7_score = 0.75
            elif radioButton.isChecked() and i==5:                            
                self.Q7_score = 1                
            else:
                None
    def q8_score(self):
        for i in range(1, 6):
            radioButton = getattr(self.ui, f"A{i}_radioButton_Q8")
            
            if radioButton.isChecked() and i==1:
                self.Q8_score =0
            elif radioButton.isChecked() and i==2:                
                self.Q8_score = 0.25
            elif radioButton.isChecked() and i==3:                
                self.Q8_score = 0.5
            elif radioButton.isChecked() and i==4:                
                self.Q8_score = 0.75
            elif radioButton.isChecked() and i==5:                            
                self.Q8_score = 1                
            else:
                None


    def q9_score(self):
        for i in range(1, 6):
            radioButton = getattr(self.ui, f"A{i}_radioButton_Q9")
            
            if radioButton.isChecked() and i==1:
                self.Q9_score =0
            elif radioButton.isChecked() and i==2:                
                self.Q9_score = 0.25
            elif radioButton.isChecked() and i==3:                
                self.Q9_score = 0.5
            elif radioButton.isChecked() and i==4:                
                self.Q9_score = 0.75
            elif radioButton.isChecked() and i==5:                            
                self.Q9_score = 1                
            else:
                None
    def q10_score(self):
        for i in range(1, 6):
            radioButton = getattr(self.ui, f"A{i}_radioButton_Q10")
            
            if radioButton.isChecked() and i==1:
                self.Q10_score =0
            elif radioButton.isChecked() and i==2:                
                self.Q10_score = 0.25
            elif radioButton.isChecked() and i==3:                
                self.Q10_score = 0.5
            elif radioButton.isChecked() and i==4:                
                self.Q10_score = 0.75
            elif radioButton.isChecked() and i==5:                            
                self.Q10_score = 1                
            else:
                None

    def q11_score(self):
        for i in range(1, 5):
            radioButton = getattr(self.ui, f"A{i}_radioButton_Q11")
            
            if radioButton.isChecked() and i==1:
                self.Q11_score =1
            elif radioButton.isChecked() and i==2:                
                self.Q11_score = 0.75
            elif radioButton.isChecked() and i==3:                
                self.Q11_score = 0.5
            elif radioButton.isChecked() and i==4:                
                self.Q11_score = 0.25              
            else:
                None

    def q12_score(self):
        for i in range(1, 5):
            radioButton = getattr(self.ui, f"A{i}_radioButton_Q12")
            
            if radioButton.isChecked() and i==1:
                self.Q12_score =0.25
            elif radioButton.isChecked() and i==2:                
                self.Q12_score = 0.50
            elif radioButton.isChecked() and i==3:                
                self.Q12_score = 0.75
            elif radioButton.isChecked() and i==4:                
                self.Q12_score = 1              
            else:
                None
    def q13_score(self):
        for i in range(1, 5):
            radioButton = getattr(self.ui, f"A{i}_radioButton_Q13")
            
            if radioButton.isChecked() and i==1:
                self.Q13_score =1
            elif radioButton.isChecked() and i==2:                
                self.Q13_score = 0.75
            elif radioButton.isChecked() and i==3:                
                self.Q13_score = 0.5
            elif radioButton.isChecked() and i==4:                
                self.Q13_score = 0.25              
            else:
                None
    def q14_score(self):
        for i in range(1, 5):
            radioButton = getattr(self.ui, f"A{i}_radioButton_Q14")
            
            if radioButton.isChecked() and i==1:
                self.Q14_score =1
            elif radioButton.isChecked() and i==2:                
                self.Q14_score = 0.75
            elif radioButton.isChecked() and i==3:                
                self.Q14_score = 0.5
            elif radioButton.isChecked() and i==4:                
                self.Q14_score = 0.25              
            else:
                None

    def q15_score(self):
        for i in range(1, 5):
            radioButton = getattr(self.ui, f"A{i}_radioButton_Q15")
            
            if radioButton.isChecked() and i==1:
                self.Q15_score =0.25
            elif radioButton.isChecked() and i==2:                
                self.Q15_score = 0.50
            elif radioButton.isChecked() and i==3:                
                self.Q15_score = 0.75
            elif radioButton.isChecked() and i==4:                
                self.Q15_score = 1              
            else:
                None



    def q16_score(self):
        for i in range(1, 5):
            radioButton = getattr(self.ui, f"A{i}_radioButton_Q16")
            
            if radioButton.isChecked() and i==1:
                self.Q16_score =0.25
            elif radioButton.isChecked() and i==2:                
                self.Q16_score = 0.50
            elif radioButton.isChecked() and i==3:                
                self.Q16_score = 0.75
            elif radioButton.isChecked() and i==4:                
                self.Q16_score = 1              
            else:
                None



    def q17_score(self):
        for i in range(1, 5):
            radioButton = getattr(self.ui, f"A{i}_radioButton_Q17")
            
            if radioButton.isChecked() and i==1:
                self.Q17_score =1
            elif radioButton.isChecked() and i==2:                
                self.Q17_score = 0.75
            elif radioButton.isChecked() and i==3:                
                self.Q17_score = 0.5
            elif radioButton.isChecked() and i==4:                
                self.Q17_score = 0.25              
            else:
                None


    def q18_score(self):
        for i in range(1, 5):
            radioButton = getattr(self.ui, f"A{i}_radioButton_Q18")
            
            if radioButton.isChecked() and i==1:
                self.Q18_score =0.25
            elif radioButton.isChecked() and i==2:                
                self.Q18_score = 0.50
            elif radioButton.isChecked() and i==3:                
                self.Q18_score = 0.75
            elif radioButton.isChecked() and i==4:                
                self.Q18_score = 1              
            else:
                None
    
    def q19_score(self):
        for i in range(1, 5):
            radioButton = getattr(self.ui, f"A{i}_radioButton_Q19")
            
            if radioButton.isChecked() and i==1:
                self.Q19_score =0.25
            elif radioButton.isChecked() and i==2:                
                self.Q19_score = 0.50
            elif radioButton.isChecked() and i==3:                
                self.Q19_score = 0.75
            elif radioButton.isChecked() and i==4:                
                self.Q19_score = 1              
            else:
                None


    def q20_score(self):
        for i in range(1, 5):
            radioButton = getattr(self.ui, f"A{i}_radioButton_Q20")
            
            if radioButton.isChecked() and i==1:
                self.Q20_score =1
            elif radioButton.isChecked() and i==2:                
                self.Q20_score = 0.75
            elif radioButton.isChecked() and i==3:                
                self.Q20_score = 0.5
            elif radioButton.isChecked() and i==4:                
                self.Q20_score = 0.25              
            else:
                None

    def sonraki_sayfa(self):
        if self.i<23:
            self.i=self.i+1
            self.ui.Label_.setCurrentIndex(self.i)
            self.ui.Onceki.setVisible(True)
            self.ui.Sonraki.setVisible(True)
            if self.i==23:
                self.ui.Sonraki.setVisible(False)


    def onceki_sayfa(self):
        if self.i>0:
            self.i=self.i-1
            self.ui.Label_.setCurrentIndex(self.i)
            self.ui.Onceki.setVisible(True)
            self.ui.Sonraki.setVisible(True)
            if self.i==0:
                self.ui.Onceki.setVisible(False)

    def anketi_bitir(self):
        df=pd.read_csv('./veri.csv')
        # Kullanıcıdan yeni veri girişi al
        yeni_veri = {}
        for i, sütun in enumerate(df.columns[0:], start=1):
            yeni_veri[sütun] = [getattr(self, f"Q{i}_score")]


        # Yeni veriyi DataFrame'e ekleme
        yeni_satır = pd.DataFrame(yeni_veri)
        df = pd.concat([df, yeni_satır], ignore_index=True)
        # Güncellenmiş DataFrame'i CSV dosyasına kaydetme
        df.to_csv('veri.csv', index=False)


        self.ui.Sonraki.setVisible(False)
        self.ui.Onceki.setVisible(False)
        self.ui.anket_sonlandir.setVisible(False)
        self.ui.A1_radioButton_Q20.setVisible(False)
        self.ui.A2_radioButton_Q20.setVisible(False) 
        self.ui.A3_radioButton_Q20.setVisible(False)       
        self.ui.A4_radioButton_Q20.setVisible(False) 
        self.ui.label_Q20.setVisible(False)       
        self.ui.sonuclari_gor.setVisible(True)  



    def sonuclari_gor(self):
        self.ui.Label_.setCurrentIndex(24)
        dataframe=pd.read_csv('./veri.csv')
        model = joblib.load('./Sosyal_estimation_model.pkl')
        X=dataframe[-1::1]
        
        tahmin = model.predict(X)

        if tahmin == 3:
            self.ui.sonuc.setText("Duyarlı")
            self.ui.sonuc.setStyleSheet("color: green;")
        elif tahmin == 2:
            self.ui.sonuc.setText("Az Bağımlı")
            self.ui.sonuc.setStyleSheet("color: green;")
        elif tahmin == 1:
            self.ui.sonuc.setText("Ağır Bağımlı")
            self.ui.sonuc.setStyleSheet("color: red;")
        elif tahmin == 0:
            self.ui.sonuc.setText("Hasta")
            self.ui.sonuc.setStyleSheet("color: red;")
        else:
            self.ui.sonuc.setText("Geçersiz tahmin değeri")


def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

app()
