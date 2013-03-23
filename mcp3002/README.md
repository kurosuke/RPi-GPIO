# A/D converter MCP3002 driver


## MCP3002 pin
    +----+----+----+----+
    |VDD |CLK |DOUT|DIN |
    +----+----+----+----+
    | 8  | 7  | 6  | 5  |
    []                  |
    | 1  | 2  | 3  | 4  |
    +----+----+----+----+
    | CS |CH0 |CH1 |VSS |
    +----+----+----+----+

## sample pins setting
  RPi         |  MCP3002
--------------|--------------
GPIO18        | CS
GPIO10(MOSI)  | DIN
GPIO09(MISO)  | DOUT
GPIO11(SCKL)  | CLK
GND           | VSS
3.3V          | VDD
 
## quick demo

    % sudo python mcp3002.py 

read result from sensor channel 0

## example

	% cd example
    % sudo python lux.py
    % sudo python temperature.py
