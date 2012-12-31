8bits serial-> parallel converter IC NJU3711 driver


# NJU3711 pin
    +----+----+----+----+----+----+----+
    |Vdd | P2 | P1 |CLR |STB |CLK |DATA|
    +----+----+----+----+----+----+----+
    | 14 | 13 | 12 | 11 | 10 | 9  | 8  |
    []                                 |
    | 1  | 2  | 3  | 4  | 5  | 6  | 7  |
    +----+----+----+----+----+----+----+
    | P3 | P4 | P5 |Vss | P6 | P7 | P8 |
    +----+----+----+----+----+----+----+

# sample pins setting
  RPi         |  NJU3711
--------------|--------------
GPIO4         | DATA
GPIO10(MOSI)  | CLK
GPIO09(MISO)  | STB
GPIO11(SCKL)  | CLR
GND           | Vss
5V            | Vdd
 
# quick demo

    % sudo python nju3177.py 

led on from 1 to 8

# exsample

	% cd exsample
    % sudo python alternating.py
    % sudo python binary_count_up.py
    % sudo python wave.py
