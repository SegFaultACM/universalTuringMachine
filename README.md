# universalTuringMachine
  This is an universal turing machine that we wrote for our final project for Computational Mathematics.
It is coded in python, it is bounded by the MIT License, so you are free to use it in your projects with proper attribution.
Created by SegFaultACM (Esteban, Joel and Daniel)

## Input
Input is passed through eval(), so it has to be valid python syntax.

turing initial like 1010001

initial state

accepting states

rejecting states

transitions

```python
  10101
  "q0"
  ["qa"]
  ["qr"]
  {("q0","0"):("q0","0","R"),("q0","1"):("q0","1","R"),("q0"," "):("q1"," ","L"),("q1","0"):("q2"," ","L"),("q1","1"):("q3"," ","L"),("q1"," "):("qr"," ","L"),("q2","0"):("qa"," ","L"),("q2","1"):("qr"," ","L"),("q2"," "):("qr"," ","L"),("q3","0"):("qr"," ","L"),("q3","1"):("qr"," ","L"),("q3"," "):("qr"," ","L")}
```




An universal turing machine emulator with defined states.
