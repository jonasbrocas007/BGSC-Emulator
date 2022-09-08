# BGSC-Emulator
## Emulator for my minecraft computer, Basic Giant and Slow Computer  
The computer uses the MB_8 architechture, developed by myself  

### Specifications  
The computer has 2 registers, an Accumulator and a Program Counter  
The computer has a 8 bit data bus, no address bus and a 8 bit ALU, it is capable of text and add/subtraction  
This computer is not assembly compatible and cannot be programmed with a programming language  

###How to use the emulator:  

The emulator works a little diferent from the "real computer"  
It has some functions like PCI, JMP, PC, PCR, OUT, TOUT, TEXT, CALC and .  
PCI - increments the program counter by one  
JMP - jump the program counter to a specified number  
PC - Shows the program counter output  
PCR - resets the program counter to adress 0  
OUT - Adds the acumulator and the next adress  
TOUT - Outputs the textlist  
TEXT - transforms memory data into text to the textlist  
CALC - inputs 2 numbers and adds or subtract them  
. - prints the input after it  


