#!/bin/python
import sys

def itob(a, bitnum=16):
    bits = []
    for i in range(0, bitnum):
        if (a & (1 << (bitnum - 1 - i))) != 0:
            bits.append('1')
        else:
            bits.append('0')
    return bits

def printv(bits):
    #dec format index
    sys.stdout.write('bitno: ')
    for i in range(15, -1, -1):
        sys.stdout.write('%4d' % i)
        if (i % 4) == 0:
            sys.stdout.write(' | ')
        else:
            sys.stdout.write(' ')
    sys.stdout.write('\n')

    #binary format index
    sys.stdout.write('bitno: ')
    for i in range(15, -1, -1):
        sys.stdout.write(''.join(itob(i, bitnum=4)))
        if (i % 4) == 0:
            sys.stdout.write(' | ')
        else:
            sys.stdout.write(' ')
    sys.stdout.write('\n')

    #value
    sys.stdout.write('value: ')
    bitno = 15
    for bit in bits:
        sys.stdout.write('%4s' % bit)
        if (bitno % 4) == 0:
            sys.stdout.write(' | ')
        else:
            sys.stdout.write(' ')
        bitno -= 1
    sys.stdout.write('\n')
    sys.stdout.write('\n')

    #karnaugh map
    print('kano-graphic:')
    sys.stdout.write('||= bit(3210) =|' + \
            '|= xx11 =||= xx10 =||= xx00 =||= xx01 =||\n')
    
    sys.stdout.write('||         11xx||%6s  ||%6s  ||%6s  ||%6s  ||\n' % (
        bits[0*4 + 0], bits[0*4 + 1], bits[0*4 + 3], bits[0*4 + 2]))
    
    sys.stdout.write('||         10xx||%6s  ||%6s  ||%6s  ||%6s  ||\n' % (
        bits[1*4 + 0], bits[1*4 + 1], bits[1*4 + 3], bits[1*4 + 2]))
    
    sys.stdout.write('||         00xx||%6s  ||%6s  ||%6s  ||%6s  ||\n' % (
        bits[3*4 + 0], bits[3*4 + 1], bits[3*4 + 3], bits[3*4 + 2]))
    
    sys.stdout.write('||         01xx||%6s  ||%6s  ||%6s  ||%6s  ||\n' % (
        bits[2*4 + 0], bits[2*4 + 1], bits[2*4 + 3], bits[2*4 + 2]))
    sys.stdout.write('\n')

def printlut4(a):
    bits = itob(a)
    print('original: 0x%04X' % a)
    print
    printv(bits)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print 'need hex digit!'
    else:
        printlut4(int(sys.argv[1], 16))


