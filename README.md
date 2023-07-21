
# RaspberryPaws
A great mix of love for dogs & raspberry.
<br>
Link to the full writeup: https://medium.com/@60noypearl/raspberrypaws-lost-animals-rfid-scanner-68d57cd4bd0
<br><br>
<img width="365" alt="Photo of actual project" src="https://github.com/noypearl/RaspberryPaws/assets/11259340/01dc86f0-11fa-48b4-8134-1634df6908c1">

## What
An Animal RFID scanner that shows you instantly the owner's phone number (and a few other details) for lost dogs.
<br>
## Howto
I advise you to [read the writeup](https://medium.com/@60noypearl/raspberrypaws-lost-animals-rfid-scanner-68d57cd4bd0) so you'll understand how to set up the environment. You will also need to:
* Install the following library in RPi to use OLED 0.91"

```
pip install Adafruit-SSD1306
```
* Clone this repo
```
git clone git@github.com:noypearl/RaspberryPaws.git
```
* Connect an OLED 0.91" (or similar and modify scanner.py script) to RPi. Remember to enable i2c communication in `raspi-config`
* Run the python scanner script

```
python scanner.py
```
* Pair animal chip RFID scanner with RPi via Bluetooth

* Scan an animal RFID chip <br>

#### And that's it!
<br>

#### You can connect the RPi to a power bank so you can walk around with it. So you can start and scan!
--------

### Diagram:
<img width="658" alt="Diagram of project" src="https://github.com/noypearl/RaspberryPaws/assets/11259340/251f3a7b-4d11-4cec-8ea7-dc39b7ad1362">

### Graph:
<img width="803" alt="Graph of components" src="https://github.com/noypearl/RaspberryPaws/assets/11259340/c321e10e-da7f-4f87-8e46-9580199d2c9b">

<br>

