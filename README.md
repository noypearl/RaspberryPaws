
# RaspberryPaws
A great mix of love for dogs & raspberry.
<br>
Link to the full writeup: https://medium.com/@60noypearl/raspberrypaws-lost-animals-rfid-scanner-68d57cd4bd0 <br>
See the POC video - https://youtu.be/FA_y9DbqpAc
<br><br>
<img width="350" alt="scanme" src="https://github.com/noypearl/RaspberryPaws/assets/11259340/dab678fb-2f93-4b40-9584-193f2a2cffa8">
<img width="350" alt="scanned" src="https://github.com/noypearl/RaspberryPaws/assets/11259340/6def3fa0-ecf2-41b0-b059-c4db49747e45">

*The results are in hebrew and I censored only the city & owner's phone No.

## What
An Animal RFID scanner that shows you instantly the owner's phone number (and a few other details) for lost dogs.
<br>
## Howto
I advise you to [read the writeup](https://medium.com/@60noypearl/raspberrypaws-lost-animals-rfid-scanner-68d57cd4bd0) so you'll understand how to set up the environment. You will also need to:

* Clone this repo
```
git clone git@github.com:noypearl/RaspberryPaws.git
```
* Install the following libraries in RPi to use OLED 0.91"
```
pip install -r requirements.txt
```
* Connect an OLED 0.91" (or similar and modify scanner.py script) to RPi. Remember to enable i2c communication in `raspi-config`
* Run the python scanner script

```
python scanner.py
```
The RPi screen will show something like this:
<img width="682" alt="RPi screen ran scanner.py script" src="https://github.com/noypearl/RaspberryPaws/assets/11259340/ee7f630f-026d-4980-8214-bd96a4e030fd">


* Pair animal chip RFID scanner with RPi via Bluetooth

* Scan an animal RFID chip <br>

#### And that's it!
<br>

#### You can connect the RPi to a power bank so you can walk around with it. So you can start and scan!
--------

### Diagram:
<img width="666" alt="diagram of project components" src="https://github.com/noypearl/RaspberryPaws/assets/11259340/bbe14d2f-2db4-4681-8f2b-8823555aecd5">

### Graph:
<img width="673" alt="graph of project components" src="https://github.com/noypearl/RaspberryPaws/assets/11259340/678ce591-358d-400f-8f3b-cfaf3e49ad83">

<br>

Enjoy and let me know if you have any comments!
