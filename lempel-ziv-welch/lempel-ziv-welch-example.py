

encode_flow = \
'''
              0    1    2    3   (indexes/code)
initial = [0x00,0x01,0x02,0x03]   s=4 <= 2^2  => 2-bit code

u = '012301230102' = 0001 1011 0001 1011 0001 0010    12 symbols (24 bits of data)

             |           |    Output         | Extended       |
Current Seq  | Next Byte | Code    |   Bits  | Dictionary     | Comments
 None        | 0x00      |         |         | -              |
 0x00        | 0x01      |    0    |      00 |  4( 100)  '01' | 4 requires 3 bits, future output use 3 bits
 0x01        | 0x02      |    1    |     001 |  5( 101)  '12' | 5 = first available code after 0 through 4
 0x02        | 0x03      |    2    |     010 |  6( 110)  '23' |
 0x03        | 0x00      |    3    |     011 |  7( 111)  '30' |
 0x0001      | 0x02      |    4    |     100 |  8(1000) '012' | 8 requires 4 bits, future output use 4 bits
 0x0203      | 0x00      |    6    |    0110 |  9(1001) '230' | 
 0x0001      | 0x00      |    4    |    0100 | 10(1010) '010' |
 0x00        | 0x02      |    0    |    0000 | 11(1011)  '02' |
 0x02        | None      |    2    |    0010 |                |

             4  5  6  7   8   9  10 11   (indexes/code)
extended = [01,12,23,30,012,230,010,02]

Unencoded length = 12 symbols * 2 bits/symbol       = 24 bits
Encoded   length = (1 codes * 2 bits/code)
                 + (4 codes * 3 bits/code)
                 + (4 codes * 4 bits/code)          = 30 bits

This is a very bad compression (the uncompressed data is smaller that the compressed).
It is all due to the initial dictionary used.

The code bits read top to bottom gives the compressed output
e = 00 001 010 011 100 0110 0100 0000 0010
  = 00 00 1010 0111 0001 1001 0000 0000 10

'''

decode_flow = \
'''
              0    1    2    3   (indexes/code)
initial = [0x00,0x01,0x02,0x03]   s=4 <= 2^2  => 2-bit code
e = 00 00 1010 0111 0001 1001 0000 0000 10
  = 00 001 010 011 100 0110 0100 0000 0010
  =  0   1   2   3   4    6    4    0    2

             |           |     Dictionary
 Input Code  | Output    | Full              |   Conjecture | Comment
 '0'    00   | 0     '0' |                   |  4 '0?'      | Initial is full, no more can fit in 2 bits
 '1'   001   | 1     '1' |  4 ( 100)    '01' |  5 '1?'      | so start reading input as 3 bits
 '2'   010   | 2     '2' |  5 ( 101)    '12' |  6 '2?'      |
 '3'   011   | 3     '3' |  6 ( 110)    '23' |  7 '3?'      |
 '4'   100   | 4    '01' |  7 ( 111)    '30' |  8 '01?'     | created code 7 (last to fit in 3 bits)
 '6'  0110   | 6    '23' |  8 (1000)   '012' |  9 '23?'     | so start reading input as 4 bits
 '4'  0100   | 4    '01' |  9 (1001)   '230' | 10 '01?'     |
 '0'  0000   | 0     '0' | 10 (1010)   '010' | 11 '0?'      |
 '2'  0010   | 2     '2' | 11 (1011)    '02' |              |

u = '012301230102' = 0001 1011 0001 1011 0001 0010    12 symbols (24 bits of data)

'''
