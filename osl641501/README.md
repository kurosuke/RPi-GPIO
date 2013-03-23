# 8x8 red LED matrix


## NJU3711 x2  
    +----+----+----+----+----+----+----+
    |Vdd | P2 | P1 |CLR |STB |CLK |DATA|
    +----+----+----+----+----+----+----+
    | 14 | 13 | 12 | 11 | 10 | 9  | 8  |
    []                                 |
    | 1  | 2  | 3  | 4  | 5  | 6  | 7  |
    +----+----+----+----+----+----+----+
    | P3 | P4 | P5 |Vss | P6 | P7 | P8 |
    +----+----+----+----+----+----+----+

## sample pins setting

# nju3711 for LED matrix pin 1-8
  RPi  | NJU3711
-------|-----------
GPIO24 | DATA      
GPIO25 | CLK       
GPIO8  | STB       
GPIO7  | CLR       
GND    | Vss       
5V     | Vdd 

### nju3711 for LED matix pin 9-16
  RPi  | NJU3711
-------|-----------
GPIO22 | DATA      
GPIO10 | CLK       
GPIO9  | STB       
GPIO11 | CLR       
GND    | Vss       
5V     | Vdd 

## quick demo

    % sudo python osl641501.py 

print text to LED matrix on/off pattern 

## image
![LED lighting](/RPi-GPIO/images/osl641501_img.jpg)
