ADD     = 0b00000
SUB     = 0b00001
AND     = 0b00010
OR      = 0b00011
XOR     = 0b00100
SLL     = 0b00101
SRL     = 0b00110
SRA     = 0b00111
ROL     = 0b01000
ROR     = 0b01001
SLT     = 0b01010
SGT     = 0b01011
SLE     = 0b01100
SGE     = 0b01101
UGT     = 0b01110
ULT     = 0b01111
ULE     = 0b10000
UGE     = 0b10001
LHI     = 0b10010   # or DM for R-triadic
ADD4    = 0b10011

LB      = 0b110100
LBU     = 0b110101
LH      = 0b110110
LHU     = 0b110111
LW      = 0b111000
SB      = 0b111001
SH      = 0b111010
SW      = 0b111011

BEQZ    = 0b011100
BNEZ    = 0b011101
JR      = 0b011110
JALR    = 0b011111

J       = 0b011001
JAL     = 0b011010


def compute(a, b, operation):
    result = 0

    if( operation == ADD ):
        result = a + b

    elif( operation == SUB ):
        result = a - b

    elif( operation == AND ):
        result = a & b

    elif( operation == OR ):
        result = a | b

    elif( operation == XOR ):
        result = a ^ b

    elif( operation == SLL ):                   
        result = (a << b) & 0xFFFFFFFF

    elif( operation == SRL ):
        result = a >> b

    elif( operation == SRA ):                   
        MSB = ( ( a >> 31 ) & 0xFFFFFFFF )

        if(MSB == 1):
            repeatation = ( '1' * b ) + ( '0' * (32 - b) )

        else:
            repeatation = '0' * 32
            
        result = int(repeatation, 2) | (a >> b)

    elif( operation == ROL ):                   
        aLeftShift = (a << b) & 0xFFFFFFFF
        result = aLeftShift | ( a >> ( 32 - b ) )

    elif( operation == ROR ):                   
        aLeftShift = (a << (32 - b)) & 0xFFFFFFFF
        result = ( a >> b ) | aLeftShift

    elif( operation == SLT ):
        result = a < b

    elif( operation == SGT ):
        result = a > b

    elif( operation == SLE ):
        result = a <= b

    elif( operation == SGE ):
        result = a >= b

    elif( operation == ULT ):
        result = a < b

    elif( operation == UGT ):
        result = a > b

    elif( operation == ULE ):
        result = a <= b

    elif( operation == UGE ):
        result = a >= b

    elif( operation == LHI ):                   
        a = a & 0xFFFF
        b = b & 0xFFFF
        result = (b << 16) | a

    elif( operation == ADD4 ):                   
        # b = (4 * b) & 0xFFFFFFFF
        b = (4 * b)
        result = a + b

    else:
        result = a + b

    return int(result)
