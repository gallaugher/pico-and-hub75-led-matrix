# pico-and-hub75-led-matrix
[![Watch the video](https://img.youtube.com/vi/XzjYWSvCipk/hqdefault.jpg)](https://youtu.be/XzjYWSvCipk)

Board - Any Raspberry Pi Pico, including the original, will run this code.
Wiring is the same for all Raspberry Pi Pico-family boards. If you're buying a new board, I'd get the most powerful veresion (at the time I'm writing this, that's the Pico 2 WH). 
https://www.adafruit.com/product/6315
Be sure to get a version with headers since you'll be adding this to a breadboard.

A mini breadboard. I love the ones by MonkMakes because they are labeled with the Raspberry Pi Pico pins, making breadboard wiring a lot easier.
https://www.adafruit.com/product/5422

Dispaly - most HUB75 64 x 32 displays or smaller should work. Know that if you use a display that's not 64 x 32 you'll need to modify your code for the new dimensions. Beware ultra-cheap boards. Double-check if it's been used with CircuitPython / Raspberry Pi Pico projects. Two examples below (there are many other sizes at these & different stores)
Adafruit sells these (I love Adafruit - high quality - great support): https://www.adafruit.com/product/2278 
And here is an ultra-cheap on AliExpress that seems to work, but know your price will probably increase with shipping and tarriffs:
https://www.aliexpress.us/item/2251832185365664.html?spm=a2g0o.order_list.order_list_main.53.3eff1802I6SLPf&gatewayAdapt=glo2usa

Power Cable - the HUB75 power cable with U-shaped ground & power ends, plus 4 pin port to plug into the HUB75 display should be included with every display.

Power Supply - 5v power supply w/at least 2 amps, but ideally 4 amps or more for full brightness. One with a barrel jack can connect to the plug below. Example below also has an adaptor plug:
https://a.co/d/cgor85U

Power Adapter Plug - Female DC Power Adapter 2.1mm Jack to Screw Terminal Block. Example:
https://www.adafruit.com/product/368

A microUSB cable & a power supply for the pico if you plan to run it when not connected to your computer. If you've been working with a pico you probably have these.

And if you prefer to diffuse the LEDs for a more "square" look to the pixels that also aren't as garishly bright, you can cover the display with diffusion acrylic like this: https://www.adafruit.com/product/4594

Drag files & folders onto a Pico configured with the latest CircuitPython from CircuitPython.org (if you donn't know how to set up a pico with CircuitPython see the lesson at https://bit.ly/pico-school). The "lib" folder above shows you which libraries are used, but I'd STRONGLY advise downloading the newest version from CircuitPython.org. If you're new to CircuitPython and will do more projects, use CIRCUP. There is a lesson in pico-school on circup, as well. All tutorials for the University Course I teach to new-to-coding/new-to-electronics students is at: https://bit.ly/circuitpython-school. Pico only at https://bit.ly/pico-school

CONSIDERATION: As mentioned, you might consider the super-easy setup of buying an Adafruit MatrixPortal S3 (go for the S3 and not the M4, the S3 is newer, more capable with more storage, and cheaper). Using a Matrix Portal S3 allows you to use just one USB-style power supply (which you probably have laying around the house, for mobile phones, etc) and one USB-C cable to power both the board & the display. At the time I created this, that board was only $19.95 US at Adafruit: https://www.adafruit.com/product/5778
The code for this is only slightly different (and easier). AI can write the difference for you & if you want a vidoe tutorial, see: 
https://youtu.be/hb2HtoIEXM8?si=B6loUfyd5mQOX45j and
https://youtu.be/OV67IjXsQbA?si=ETBBG7LJgcw_CoTv

Wiring &amp; code to run a "Happy Graduation" on a Raspberry Pi Pico with a 64 x 32 HUB75 LED Matrix Display
![Pico HUB75 Wiring Diagram](https://github.com/user-attachments/assets/d00afd63-ca34-4f65-a2f5-37aca9885d04)
![pico and 64x32 LED HUB75 wiring photo](https://github.com/user-attachments/assets/ad1b957d-1072-4f63-9da2-bb0b31e8d256)

