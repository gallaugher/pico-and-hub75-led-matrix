# pico-and-hub75-led-matrix
Board - Any Raspberry Pi Pico, including the original, will run this code.
Wiring is the same for all boards

Dispaly - most HUB75 64 x 32 displays should work. Beware ultra-cheap boards. Double-check if it's been used with CircuitPython / Raspberry Pi Pico projects. Two examples below (there are many other sizes at these & different stores)
Adafruit sells these (I love Adafruit - high quality - great support): https://www.adafruit.com/product/2278 
And here is an ultra-cheap on AliExpress that seems to work:
https://www.aliexpress.us/item/2251832185365664.html?spm=a2g0o.order_list.order_list_main.53.3eff1802I6SLPf&gatewayAdapt=glo2usa

Power Cable - the HUB75 power cable with U-shaped ground & power ends, plus 4 pin port to plug into the HUB75 display should be included with every display.
Power Supply - 5v power supply w/at least 2 amps, but ideally 4 amps or more for full brightness. One with a barrel jack can connect to the plug below. Example below also has an adaptor plug:
https://a.co/d/cgor85U

Power Adapter Plug - Female DC Power Adapter 2.1mm Jack to Screw Terminal Block. Example:
https://www.adafruit.com/product/368

CONSIDERATION: If you're going to buy a power supply and board, you might consider the super-easy setup of buying an Adafruit MatrixPortal S3 (go for the S3 and not the M4, the S3 is newer & more powerful). Using this setup allows you to use just one USB-style power supply (which you probably have laying around the house, for mobile phones, etc) to power both the board & the display. At the time I created this, that board was only $19.95 US at Adafruit: https://www.adafruit.com/product/5778
The code for this is only slightly different (and easier). AI can write the difference for you & if you want a vidoe tutorial, see: 
https://youtu.be/hb2HtoIEXM8?si=B6loUfyd5mQOX45j and
https://youtu.be/OV67IjXsQbA?si=ETBBG7LJgcw_CoTv

Wiring &amp; code to run a "Happy Graduation" on a Raspberry Pi Pico with a 64 x 32 HUB75 LED Matrix DIsplay
