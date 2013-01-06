# sample patterns

## use parts
  part name        |  memo
-------------------|--------------------------
led x8             |
nju3711            | 8bits serial-> parallel converter IC 
registor           | 1K x8

##  sample diagram
![sample dìagram](https://raw.github.com/kurosuke/RPi-GPIO/master/images/nju3711_board.png)

## alternating

    % sudo python alternating.py

- oxox oxox
- xoxo xoxo
- oxox oxox
- xoxo xoxo

## binary count up

    % sudo python binary_count_up.py

- oxxx xxxx
- xoxx xxxx
- ooxx xxxx
- xxox xxxx
- ...
- xooo oooo
- oooo oooo

## wave from center to around

    % sudo python wave.py

- xxxx xxxx
- xxxo oxxx
- xxoo ooxx
- xooo ooox
- oooo oooo


