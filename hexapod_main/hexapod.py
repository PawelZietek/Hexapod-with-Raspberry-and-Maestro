import xbox
import maestro
import time
import math
import RPi.GPIO as GPIO


servo = maestro.Controller() #inicjalizacja sterownika maestro
joy = xbox.Joystick() #inicjacja kontrolera

#ustawienia numerowania GPIO
GPIO.setmode(GPIO.BCM)

#inicjalizacja przełączników krańcowych
GPIO.setup(16, GPIO.IN) #noga0
GPIO.setup(17, GPIO.IN) #noga1
GPIO.setup(27, GPIO.IN) #noga2
GPIO.setup(26, GPIO.IN) #noga3
GPIO.setup(20, GPIO.IN) #noga4
GPIO.setup(21, GPIO.IN) #noga5


#definicja zmiennych potrzebnych w dalszej części kodu
numer_nogi = 0
i = 0

#wyśrodkowanie wszystkich serwomechanizmów
servo.setTarget(6, 5500)
servo.setTarget(7, 5500)
servo.setTarget(8, 5500)
servo.setTarget(9, 5500)
servo.setTarget(10, 5200)
servo.setTarget(11, 5500)
time.sleep(1)
servo.setTarget(0, 6200)
servo.setTarget(1, 6000)
servo.setTarget(2, 5800)
servo.setTarget(3, 6900)
servo.setTarget(4, 5300)
servo.setTarget(5, 6200)
time.sleep(1)
servo.setTarget(12, 5000)
servo.setTarget(13, 5000)
servo.setTarget(14, 5000)
servo.setTarget(15, 5000)
servo.setTarget(16, 5000)
servo.setTarget(17, 5000)

#pętla ustawiająca przyśpieszenie i prędkość poruszania się serw
while i < 18:
	servo.setAccel(i, 0)
	servo.setSpeed(i, 100)
	i+=1
		
while not joy.Back(): 
#aby wyłączyć robota należy na kontrolerze wcisnąć przycisk "back"
		
	if joy.rightTrigger():	
	#Zwiększenie prześwitu robota poprzez wcisnięcie
	#prawego spustu kontrolera (im mocniej wciśnięty tym szybciej się podnosi)
	#im większą wartość zwróci joy.rightTrigger tym większą wartość dodana 
	#zostanie do wartości aktualnego położenia
		servo.setTarget(6, servo.getPosition(6)+int((joy.rightTrigger()*50)))
		servo.setTarget(7, servo.getPosition(7)+int((joy.rightTrigger()*50)))
		servo.setTarget(8, servo.getPosition(8)+int((joy.rightTrigger()*50)))
		servo.setTarget(9, servo.getPosition(9)+int((joy.rightTrigger()*50)))
		servo.setTarget(10, servo.getPosition(10)+int((joy.rightTrigger()*50)))
		servo.setTarget(11, servo.getPosition(11)+int((joy.rightTrigger()*50)))
		time.sleep(0.05)
	if joy.leftTrigger(): 
	#Zmiejszenie prześwitu robota poprzez wcisnięcie lewego spustu kontrolera 
	#(im mocniej wciśnięty tym szybciej się opuszcza)
	#dzialanie analogiczne do joy.rightTrigger lecz teraz odejmujemy 
	#określoną wartość od aktualnego położenia
		servo.setTarget(6, servo.getPosition(6)-int((joy.leftTrigger()*50)))
		servo.setTarget(7, servo.getPosition(7)-int((joy.leftTrigger()*50)))
		servo.setTarget(8, servo.getPosition(8)-int((joy.leftTrigger()*50)))
		servo.setTarget(9, servo.getPosition(9)-int((joy.leftTrigger()*50)))
		servo.setTarget(10, servo.getPosition(10)-int((joy.leftTrigger()*50)))
		servo.setTarget(11, servo.getPosition(11)-int((joy.leftTrigger()*50)))
		time.sleep(0.05)
	if joy.dpadRight(): #wychylenie robota w prawo
		servo.setTarget(0, servo.getPosition(0)+50)
		servo.setTarget(1, servo.getPosition(1)+50)
		servo.setTarget(2, servo.getPosition(2)+50)
		servo.setTarget(3, servo.getPosition(3)+50)
		servo.setTarget(4, servo.getPosition(4)+50)
		servo.setTarget(5, servo.getPosition(5)+50)
		time.sleep(0.05)
	if joy.dpadLeft(): #wychylenie robota w lewo
		servo.setTarget(0, servo.getPosition(0)-50)
		servo.setTarget(1, servo.getPosition(1)-50)
		servo.setTarget(2, servo.getPosition(2)-50)
		servo.setTarget(3, servo.getPosition(3)-50)
		servo.setTarget(4, servo.getPosition(4)-50)
		servo.setTarget(5, servo.getPosition(5)-50)
		time.sleep(0.05)
	if joy.dpadUp(): #podnoszenie piszczeli 
		servo.setTarget(12, servo.getPosition(12)+50)
		servo.setTarget(13, servo.getPosition(13)+50)
		servo.setTarget(14, servo.getPosition(14)+50)
		servo.setTarget(15, servo.getPosition(15)+50)
		servo.setTarget(16, servo.getPosition(16)+50)
		servo.setTarget(17, servo.getPosition(17)+50)
		time.sleep(0.05)
	if joy.dpadDown(): #opuszczanie piszczeli
		servo.setTarget(12, servo.getPosition(12)-50)
		servo.setTarget(13, servo.getPosition(13)-50)
		servo.setTarget(14, servo.getPosition(14)-50)
		servo.setTarget(15, servo.getPosition(15)-50)
		servo.setTarget(16, servo.getPosition(16)-50)
		servo.setTarget(17, servo.getPosition(17)-50)
		time.sleep(0.05)
	if joy.Start(): #przysisk start resetuje serwa robota do wartości początkowych (wyśrodkowuje serwa)
		servo.setTarget(6, 5500)
		servo.setTarget(7, 5500)
		servo.setTarget(8, 5500)
		servo.setTarget(9, 5500)
		servo.setTarget(10, 5300)
		servo.setTarget(11, 5500)
		time.sleep(1)
		servo.setTarget(0, 6200)
		servo.setTarget(1, 6000)
		servo.setTarget(2, 5800)
		servo.setTarget(3, 6900)
		servo.setTarget(4, 5300)
		servo.setTarget(5, 6200)
		time.sleep(1)
		servo.setTarget(12, 5000)
		servo.setTarget(13, 5000)
		servo.setTarget(14, 5000)
		servo.setTarget(15, 5000)
		servo.setTarget(16, 5000)
		servo.setTarget(17, 5000)
	if joy.rightX(deadzone=10000): #obrót hexapoda wokół własnej osi sterowane za pomocą wychylenia osi X prawego analoga kontrolera
		#podnosimy nogi 0, 2, 4 w górę o wartość 750
		servo.setTarget(6, servo.getPosition(6)-750)
		servo.setTarget(8, servo.getPosition(8)-750)
		servo.setTarget(10, servo.getPosition(10)-750)
		time.sleep(0.1)
		#Nogi 0, 2, 4 przesuwamy o wartość którą zmienia się wraz z wychyleniem gałki prawego analoga w osi X,
		#jeśli analog zwróci wartość mniejszą niż 0 to int((joy.right()*1000)) zwróci nam wartość ujemną,
		#a co za tym idzie do pozycji serw dodamy wartość, w drugim przypadku gdy int((joy.right()*1000)) będzie dodatnie,
		#to wtedy od pozycji serw odejmujemy okresloną wartość, a to determinuję w którą stronę obróci się robot.
		servo.setTarget(0,servo.getPosition(0)-int((joy.rightX()*1000)))
		servo.setTarget(2,servo.getPosition(2)-int((joy.rightX()*1000)))
		servo.setTarget(4,servo.getPosition(4)-int((joy.rightX()*1000)))
		time.sleep(0.1)
		#W tym kroku opuszczamy nogi 0, 2, 4 o wartość którą w kroku 1 je podnieśliśmy
		servo.setTarget(6, servo.getPosition(6)+750)
		servo.setTarget(8, servo.getPosition(8)+750)
		servo.setTarget(10, servo.getPosition(10)+750)
		time.sleep(0.3)
		#Powtórzenie tych samych operaacji na nogach 1, 3, 5
		servo.setTarget(7, servo.getPosition(7)-750)
		servo.setTarget(9, servo.getPosition(9)-750)
		servo.setTarget(11, servo.getPosition(11)-750)
		time.sleep(0.1)
		servo.setTarget(1,servo.getPosition(1)-int((joy.rightX()*1000)))
		servo.setTarget(3,servo.getPosition(3)-int((joy.rightX()*1000)))
		servo.setTarget(5,servo.getPosition(5)-int((joy.rightX()*1000)))
		time.sleep(0.1)
		servo.setTarget(7, servo.getPosition(7)+750)
		servo.setTarget(9, servo.getPosition(9)+750)
		servo.setTarget(11, servo.getPosition(11)+750)
		time.sleep(0.1)
		#Na końcu wyśrodkowujemy serwa 0, 1, 2 ,3 , 4, 5
		servo.setTarget(0, 6200)
		servo.setTarget(1, 6000)
		servo.setTarget(2, 5800)	
		servo.setTarget(3, 6900)
		servo.setTarget(4, 5300)
		servo.setTarget(5, 6200)
		time.sleep(0.2)
		
	if joy.leftY(deadzone=10000): #chodzenie do przodu oraz do tyłu sterowane za pomocą wychylenia w osi Y lewego analoga kontrolera
		servo.setTarget(7, servo.getPosition(6)-1000)
		servo.setTarget(9, servo.getPosition(8)-1000)
		servo.setTarget(11, servo.getPosition(10)-1000)	
		
		time.sleep(0.2)
		
		servo.setTarget(1,servo.getPosition(1)-int((joy.leftY()*700)))
		servo.setTarget(3,servo.getPosition(3)-int((joy.leftY()*700)))
		servo.setTarget(5,servo.getPosition(5)+int((joy.leftY()*700)))
		
		time.sleep(0.1)
		
		servo.setTarget(0,servo.getPosition(0)-int((joy.leftY()*700)))
		servo.setTarget(2,servo.getPosition(2)+int((joy.leftY()*700)))
		servo.setTarget(4,servo.getPosition(4)-int((joy.leftY()*700)))
		
		time.sleep(0.2)		
	
		servo.setTarget(7, servo.getPosition(7)+1000)
		servo.setTarget(9, servo.getPosition(9)+1000)
		servo.setTarget(11, servo.getPosition(11)+1000)
		
		time.sleep(0.2)
		
		servo.setTarget(6, servo.getPosition(6)-1000)
		servo.setTarget(8, servo.getPosition(8)-1000)
		servo.setTarget(10, servo.getPosition(10)-1000)
		
		time.sleep(0.2)
		
		servo.setTarget(0,servo.getPosition(0)+int((joy.leftY()*700)))
		servo.setTarget(2,servo.getPosition(2)-int((joy.leftY()*700)))
		servo.setTarget(4,servo.getPosition(4)+int((joy.leftY()*700)))
		
		time.sleep(0.1)
		
		servo.setTarget(1,servo.getPosition(1)+int((joy.leftY()*700)))
		servo.setTarget(3,servo.getPosition(3)+int((joy.leftY()*700)))
		servo.setTarget(5,servo.getPosition(5)-int((joy.leftY()*700)))
		
		time.sleep(0.2)
		
		servo.setTarget(6, servo.getPosition(6)+1000)
		servo.setTarget(8, servo.getPosition(8)+1000)
		servo.setTarget(10, servo.getPosition(10)+1000)
		
		time.sleep(0.2)
		
	while joy.X(): #obsługa jedenj nogi przytrzumyjac przycisk x
		if joy.rightBumper() and numer_nogi < 5: #wybór nogi nastepnej
			numer_nogi += 1
			time.sleep(0.5)
		elif joy.rightBumper() and numer == 5: #zapetlenie w gorę
			numer_nogi = 0
			time.sleep(0.5)
		if joy.leftBumper() and numer_nogi > 0:  #wybór nogi poprzedniej 
			numer_nogi -= 1
			time.sleep(0.5) 
		elif joy.leftBumper() and numer_nogi == 0: #zapętlenie w dół
			numer_nogi = 5
			time.sleep(0.5)

		#sterowanie nogą w górę i w dół
		if joy.leftY(deadzone=10000): 
			servo.setTarget(6+numer_nogi, servo.getPosition(6+numer_nogi)-int((joy.leftY()*50)))
			time.sleep(0.05)
		#poruszanie nogą w lewo i w prawo 
		if joy.leftX(deadzone=10000):
			servo.setTarget(0+numer_nogi, servo.getPosition(0+numer_nogi)-int((joy.leftX()*50)))
			time.sleep(0.05)
		if joy.rightTrigger(): #podniesienie łydki za pomocą prawego triggera
			servo.setTarget(12+numer_nogi, servo.getPosition(12+numer_nogi)+int((joy.rightTrigger()*50)))
			time.sleep(0.05)
		if joy.leftTrigger(): #opuszczenie łydki za pomocą lewego triggera
			servo.setTarget(12+numer_nogi, servo.getPosition(12+numer_nogi)-int((joy.leftTrigger()*50)))
			time.sleep(0.05)

	while joy.X(): #obsługa jedenj nogi przytrzumyjac przycisk x
		if joy.rightBumper() and numer_nogi < 5: #wybór nogi nastepnej
			numer_nogi += 1
			time.sleep(0.5)
		if joy.leftBumper() and numer_nogi > 0:  #wybór nogi poprzedniej 
			numer_nogi -= 1
			time.sleep(0.5)
		if joy.leftY(deadzone=10000): 
			servo.setTarget(6+numer_nogi, servo.getPosition(6+numer_nogi)-int((joy.leftY()*50)))
			time.sleep(0.05)
		if joy.leftX(deadzone=10000):
			servo.setTarget(0+numer_nogi, servo.getPosition(0+numer_nogi)-int((joy.leftX()*50)))
			time.sleep(0.05)
		if joy.rightTrigger(): #podniesienie łydki za pomocą prawego triggera
			servo.setTarget(12+numer_nogi, servo.getPosition(12+numer_nogi)+int((joy.rightTrigger()*50)))
			time.sleep(0.05)
		if joy.leftTrigger(): #opuszczenie łydki za pomocą lewego triggera
			servo.setTarget(12+numer_nogi, servo.getPosition(12+numer_nogi)-int((joy.leftTrigger()*50)))
			time.sleep(0.05)
			
	if joy.leftX(deadzone=10000): #obrót hexapoda wokół własnej osi sterowane za pomocą wychylenia osi X prawego analoga kontrolera
		servo.setTarget(6, servo.getPosition(6)-1500)
		time.sleep(0.3)
		servo.setTarget(0,servo.getPosition(0)-int((joy.leftX()*1000)))
		while (GPIO.input(16)) == 0:
			servo.setTarget(6, servo.getPosition(6)+50)
			time.sleep(0.1)
				
		servo.setTarget(8, servo.getPosition(8)-1500)
		time.sleep(0.3)
		servo.setTarget(2,servo.getPosition(2)-int((joy.leftX()*1000)))	
		while (GPIO.input(27)) == 0:
			servo.setTarget(8, servo.getPosition(8)+50)
			time.sleep(0.1)	
		
		servo.setTarget(10, servo.getPosition(10)-1500)
		time.sleep(0.3)
		servo.setTarget(4,servo.getPosition(4)-int((joy.leftX()*1000)))
		while (GPIO.input(20)) == 0:
			servo.setTarget(10, servo.getPosition(10)+50)
			time.sleep(0.1)
		
		servo.setTarget(7, servo.getPosition(7)-1500)
		time.sleep(0.3)
		servo.setTarget(1,servo.getPosition(1)-int((joy.leftX()*1000)))
		while (GPIO.input(17)) == 0:
			servo.setTarget(7, servo.getPosition(7)+50)
			time.sleep(0.1)
			
		servo.setTarget(9, servo.getPosition(9)-1500)
		time.sleep(0.3)
		servo.setTarget(3,servo.getPosition(3)-int((joy.leftX()*1000)))
		while (GPIO.input(26)) == 0:
			servo.setTarget(9, servo.getPosition(9)+50)
			time.sleep(0.1)
			
		servo.setTarget(11, servo.getPosition(11)-1500)
		time.sleep(0.3)
		servo.setTarget(5,servo.getPosition(5)-int((joy.leftX()*1000)))
		while (GPIO.input(21)) == 0:
			servo.setTarget(11, servo.getPosition(11)+50)
			time.sleep(0.1)
	
		servo.setTarget(0, 6200)
		servo.setTarget(1, 6000)
		servo.setTarget(2, 5800)	
		servo.setTarget(3, 6900)
		servo.setTarget(4, 5300)
		servo.setTarget(5, 6200)

	if joy.rightY(deadzone=10000): #chodzenie do przodu oraz do tyłu sterowane za pomocą wychylenia w osi Y lewego analoga kontrolera
		servo.setTarget(7, servo.getPosition(6)-1000)
		servo.setTarget(9, servo.getPosition(8)-1000)
		servo.setTarget(11, servo.getPosition(10)-1000)	
		
		time.sleep(0.2)
		
		servo.setTarget(1,servo.getPosition(1)-int((joy.rightY()*700)))
		servo.setTarget(3,servo.getPosition(3)-int((joy.rightY()*700)))
		servo.setTarget(5,servo.getPosition(5)+int((joy.rightY()*700)))
		
		time.sleep(0.1)
		
		servo.setTarget(0,servo.getPosition(0)-int((joy.rightY()*700)))
		servo.setTarget(2,servo.getPosition(2)+int((joy.rightY()*700)))
		servo.setTarget(4,servo.getPosition(4)-int((joy.rightY()*700)))
		
		time.sleep(0.2)		
	
		while (GPIO.input(17)) == 0:
			servo.setTarget(7, servo.getPosition(7)+50)
			time.sleep(0.1)
		while (GPIO.input(26)) == 0:
			servo.setTarget(9, servo.getPosition(9)+50)
			time.sleep(0.1)	
		while (GPIO.input(21)) == 0:
			servo.setTarget(11, servo.getPosition(11)+50)
			time.sleep(0.1)
			
		time.sleep(0.2)
		
		servo.setTarget(6, servo.getPosition(6)-1000)
		servo.setTarget(8, servo.getPosition(8)-1000)
		servo.setTarget(10, servo.getPosition(10)-1000)
		
		time.sleep(0.2)
		
		servo.setTarget(0,servo.getPosition(0)+int((joy.rightY()*700)))
		servo.setTarget(2,servo.getPosition(2)-int((joy.rightY()*700)))
		servo.setTarget(4,servo.getPosition(4)+int((joy.rightY()*700)))
		
		time.sleep(0.1)
		
		servo.setTarget(1,servo.getPosition(1)+int((joy.rightY()*700)))
		servo.setTarget(3,servo.getPosition(3)+int((joy.rightY()*700)))
		servo.setTarget(5,servo.getPosition(5)-int((joy.rightY()*700)))
		
		time.sleep(0.2)
		
		while (GPIO.input(16)) == 0:
			servo.setTarget(6, servo.getPosition(6)+50)
			time.sleep(0.1)
		while (GPIO.input(27)) == 0:
			servo.setTarget(8, servo.getPosition(8)+50)
			time.sleep(0.1)	
		while (GPIO.input(20)) == 0:
			servo.setTarget(10, servo.getPosition(10)+50)
			time.sleep(0.1)
		
		time.sleep(0.2)
joy.close()
servo.close()
