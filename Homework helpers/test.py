import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))
def tanh(x):
    return((math.exp(x) - math.exp(-x)) / (math.exp(x) + math.exp(-x)))

W_fh = 0.
W_ih = 0.
W_oh = 0
W_fx = 0.
W_ix = 100.
W_ox = 100
b_f = -100.
b_i = 100.
b_o = 0
W_ch = -100.
W_cx = 50
b_c = 0

nsteps = 5 

h = [None] * (nsteps + 1)
h[-1] = 0

c = [None] * (nsteps + 1)
c[-1] = 0

x = [1,1,0,1,1] 

def forget_gate(t, h, x, W_fh=W_fh, W_fx=W_fx, b_f=b_f):
    return sigmoid(W_fh * h[t-1] + W_fx * x[t] + b_f)

def input_gate(t, h, x, W_ih=W_ih, W_ix=W_ix, b_i=b_i):
    return sigmoid(W_ih * h[t-1] + W_ix * x[t] + b_i)

def output_gate(t, h, x, W_oh=W_oh, W_ox=W_ox, b_o=b_o):
    return sigmoid(W_oh * h[t-1] + W_ox * x[t] + b_o)

def cell(t, h, x, W_ch=W_ch, W_cx=W_cx, b_c=b_c):
    return forget_gate(t, h, x) * c[t-1] + input_gate(t, h, x) * tanh(W_ch * h[t-1] + W_cx * x[t] + b_c)

def h_state(t, h, x):
    return round(output_gate(t, h, x) * tanh(cell(t, h, x)))

def learn():
    for t in range(nsteps):

        c[t] = cell(t, h, x)
        h[t] = h_state(t, h, x)
        
    print("h", h[:nsteps])

learn()
