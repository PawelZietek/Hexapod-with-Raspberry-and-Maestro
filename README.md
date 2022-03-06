Hi, I built a hexapod based on a raspberry pi, pololu maestro 24 channel servo controller, 18x RDS3225 cheap robotics servos, and couple other stuff.
I share all needed files including 3d printed parts and dxf drawing for laser cutting. I also include pictures of all connections I've made.

The electronics you need(with links):
1. Raspberry Pi 4B 2GB - https://botland.store/raspberry-pi-4b-modules-and-kits/14646-raspberry-pi-4-model-b-wifi-dual-band-bluetooth-2gb-ram-15ghz-765756931175.html
2. Pololu Maestro 24ch - https://www.pololu.com/product/1356
3. 18x RDS3225 ROBOTIC servos - its important for servos to be robotic type with shafts on both sides - https://pl.aliexpress.com/item/32907625266.html?gatewayAdapt=glo2pol
4. UBEC 5V 3A - https://www.amazon.com/Adafruit-UBEC-Step-Down-Buck-Converter/dp/B00PLV0VC0
5. 6x microswitches - https://www.amazon.com/FYSETC-Printer-Accessories-Mechanical-Endstops/dp/B07ZCSXNF3
6. 2 cell 7,4V LiPo battery pack with charger
7. xbox 360 controller with usb receiver

Mechanical Parts and tools needed:
1. Screwdrivers, pliers, callipers
2. 3d printer access
3. cutting laser access
4. lots of m3, m4 phillips head screws different lenghts with washers and bolts
5. soldering iron access with wires and other stuff for it<br />

<img width="500" alt="hexapod_project_fusion 1" src="https://user-images.githubusercontent.com/97260629/156940260-76a16a00-e74d-4ed8-ac00-9d9793eaef6e.PNG">
<img width="500" alt="hexapod_project_fusion 3" src="https://user-images.githubusercontent.com/97260629/156940293-6b059886-6e09-449b-be1f-8f532a016814.PNG">
<img width="500" alt="hexapod_project_fusion 4" src="https://user-images.githubusercontent.com/97260629/156940295-0673b1d6-e4ec-437b-bd40-c16e73cc3fde.PNG">
Final models of leg and foot<br />
<img width="500" alt="foot" src="https://user-images.githubusercontent.com/97260629/156940461-fc6d5f8b-1c93-4c21-a72f-b8357c540742.png">
<img width="500" alt="leg" src="https://user-images.githubusercontent.com/97260629/156940463-e6009c99-ea65-4a2c-873c-e1fe84e0d33a.png">

In the picture below i numbered servos from 0 to 17 and this is order i'm using later in my code.<br />
<img width="500" alt="hexapod_project_fusion 6" src="https://user-images.githubusercontent.com/97260629/156940306-6f7e1da1-d8b1-480f-880e-e850e0902fba.png">

Here's how i connected everything with raspberry.<br />
<img width="500" alt="connection" src="https://user-images.githubusercontent.com/97260629/156940382-a765efa2-7e1a-4601-bd80-3e1705825fc5.png">

And how swtiches and power are connected to Raspberry GPIO.<br />
<img width="500" alt="gpio connection" src="https://user-images.githubusercontent.com/97260629/156940423-5352075a-2a17-4e4c-8942-5ba040a54ea3.png">

My raspberry is using Ubuntu 20.04. Main code is in Python. You will need to instal repositories like xboxdrv, python3, pip, etc.<br />
![Hexapod1](https://user-images.githubusercontent.com/97260629/156941347-0096db8a-de55-4529-93f3-2412d0251e9a.jpg)
![Hexapod2](https://user-images.githubusercontent.com/97260629/156941351-ad232e2e-38a5-46c2-80be-fce31e4484e2.jpg)
![Hexapod3](https://user-images.githubusercontent.com/97260629/156941356-e3bb29f2-e362-458a-9091-ca8b0f1265c4.jpg)
![Hexapod4](https://user-images.githubusercontent.com/97260629/156941362-40ee463e-8e4a-4650-a1c0-0bb14bf48b44.jpg)







