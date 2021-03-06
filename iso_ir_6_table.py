# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 01:10:59 2020

@author: Romain

E-1 DICOM Default Character Repertoire Encoding

Encoding iso_ir_6 norm ? 

"""


def default_char(bin_num):
    
    b = {}
    
    b["00001010"] = "LF"
    b["00001101"] = "CR"
    
    b["00100000"] = "SP"
    b["00100001"] = "!"
    b["00100010"] = "g"
    b["00100011"] = "#"
    b["00100100"] = "$"
    b["00100101"] = "%"
    b["00100110"] = "&"
    b["00100111"] = "'"
    b["00101000"] = "("
    b["00101001"] = ")"
    b["00101010"] = "*"
    b["00101011"] = "+"
    b["00101100"] = ","
    b["00101101"] = "-"
    b["00101110"] = "."
    b["00101111"] = "/"
    
    b["00110000"] = "0"
    b["00110001"] = "1"
    b["00110010"] = "2"
    b["00110011"] = "3"
    b["00110100"] = "4"
    b["00110101"] = "5"
    b["00110110"] = "6"
    b["00110111"] = "7"
    b["00111000"] = "8"
    b["00111001"] = "9"
    b["00111010"] = ":"
    b["00111011"] = ";"
    b["00111100"] = "<"
    b["00111101"] = "="
    b["00111110"] = ">"
    b["00111111"] = "?"
    
    b["01000001"] = "A"
    b["01000010"] = "B"
    b["01000011"] = "C"
    b["01000100"] = "D"
    b["01000101"] = "E"
    b["01000110"] = "F"
    b["01000111"] = "G"
    b["01001000"] = "H"
    b["01001001"] = "I"
    b["01000010"] = "J"
    b["01001011"] = "K"
    b["01001100"] = "L"
    b["01001101"] = "M"
    b["01001110"] = "N"
    b["01001111"] = "O"
    
    b["01010000"] = "P"
    b["01010001"] = "Q"
    b["01010010"] = "R"
    b["01010011"] = "S"
    b["01010100"] = "T"
    b["01010101"] = "U"
    b["01010110"] = "V"
    b["01010111"] = "W"
    b["01011000"] = "X"
    b["01011001"] = "Y"
    b["01011010"] = "Z"
    b["01011011"] = "["
    b["01011100"] = " "
    b["01011101"] = "]"
    b["01011110"] = "^"
    b["01011111"] = "_"
    
    b["01100000"] = "`"
    b["01100001"] = "a"
    b["01100010"] = "b"
    b["01100011"] = "c"
    b["01100100"] = "d"
    b["01100101"] = "e"
    b["01100110"] = "f"
    b["01100111"] = "g"
    b["01101000"] = "h"
    b["01101001"] = "i"
    b["01101010"] = "j"
    b["01101011"] = "k"
    b["01101100"] = "l"
    b["01101101"] = "m"
    b["01101110"] = "n"
    b["01101111"] = "o"
    
    b["01110000"] = "p"
    b["01110001"] = "q"
    b["01110010"] = "r"
    b["01110011"] = "s"
    b["01110100"] = "t"
    b["01110101"] = "u"
    b["01110110"] = "v"
    b["01110111"] = "w"
    b["01111000"] = "x"
    b["01111001"] = "y"
    b["01111010"] = "z"
    b["01111011"] = "{"
    b["01111100"] = "|"
    b["01111101"] = "}"
    b["01111110"] = "~"
    b["01111111"] = " "
    
    
    
    for i in b:
        if i == bin_num:
            return b[i]
    
