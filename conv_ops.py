# conv_ops.py
#
# Usage: python3 conv_ops.py c_in h_in w_in n_filt h_filt w_filt s p


# Arguments:
#c_in: input channel count
#h_in: input height count
#w_in: input width count
#n_filt: number of filters in the convolution layer
#h_filt: filter height count
#w_filt: filter width count
#s: stride of convolution filters
#p: amount of padding on each of the four input map sides

# Output:
#print(int(c_out)) # output channel count
#print(int(h_out)) # output height count
#print(int(w_out)) # output width count
#print(int(adds))  # number of additions performed
#print(int(muls))  # number of multiplications performed
#print(int(divs))  # number of divisions performed

# Written by Samuel Jacobson
# Other contributors: None

# This work is licensed under CC BY-SA 4.0

# import Python modules
import math  # math module
import sys  # argv

# Constants
w = 7.292115 * 10 ** -5



# initialize script arguments
c_in = float('nan')
h_in = float('nan')
w_in = float('nan')
n_filt = float('nan')
h_filt = float('nan')
w_filt = float('nan')
s = float('nan')
p = float('nan')

# Parse Script Arguments
if len(sys.argv) == 9:
    c_in = float(sys.argv[1])
    h_in = float(sys.argv[2])
    w_in = float(sys.argv[3])
    n_filt = float(sys.argv[4])
    h_filt = float(sys.argv[5])
    w_filt = float(sys.argv[6])
    s = float(sys.argv[7])
    p = float(sys.argv[8])
else:
    print( \
        'python3 conv_ops.py c_in h_in w_in n_filt h_filt w_filt s p' \
        )
    exit()

# Script

c_out = n_filt
h_out = (h_in + 2 * p - h_filt) / s + 1
w_out = (w_in + 2 * p - w_filt) / s + 1
mults = n_filt * h_out * w_out * c_in * h_filt * w_filt
adds = n_filt * h_out * w_out * c_in * h_filt * w_filt
divs = 0

print(int(c_out))  # output channel count
print(int(h_out))  # output height count
print(int(w_out))  # output width count
print(int(adds))  # number of additions performed
print(int(mults))  # number of multiplications performed
print(int(divs))  # number of divisions performed
