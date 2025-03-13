- Know the difference between feed-forward and recurrent neural networks(RNNs).
    
- Understand the role of **gating** and **memory cells** in long-short term memory (LSTM).
    
- Understand the process of **encoding** of RNNs in modeling sequences.

## Intro to Recurrent Neural Networks

Issue: Modeling sequences and temporal ?

1. Using feed forward network
    - Timeserie Create a feature vector of last n time periods
    - Language modeling Create a feature vector of the last n words. Concatenated from one-hot endocing of each work in the bag of word.

What are we missing?

- how many steps to look back?

"While in feed-forward networks we have to manually engineer how history is mapped to a feature vector (representation) for the specific task at hand, using RNN's this task is also part of the learning process and hence automatised."

## Why we need RNNs?
Predicitons tasks:
- predict the next word in a sentence
- sentiment classification
- machine translation

Each tasks might use different vector representation of the sentence.

FOr these task, 2 steps are necessary: Encoding and decoding

- **Encoding**: turning a sequence into a vector
- **Decoding**: turning (that) vector into a prediction - sequence
    - need summarization , cf Languange modeling later ?


## Encoding with RNN
![[Pasted image 20250308162911.png]]
$$
s_t = tanh(W^{s,s}s_{t-1}+W^{s,x}x_{t})
$$

## Gating and LSTM

Very deep Information is forgotten, over-written

Concerns:

- Gradients Vanish
- Gradient Explode
### A gating network
$$
g_t=sigmoid(W^{g,s}s_{t-1}+W^{g,x}x_t)
$$
between [0,1]
$$ s_t = (1 - g_t) * s_{t-1} + g_t * tanh(W s + W x)$$
$s_t$ is the previous state $tanh$ is the new suggested value

When $g_t=0$: learn nothing
- $(1-g_t)=1$:$s_t=s_{t-1}$
- tanh() is 0 When g_t = 1: remember nothing

### 5.2 the LSTM = Long Short Term Memory

An LSTM cell is structured around a **memory cell (Cₜ)** and three key **gates** that regulate the flow of information:

1. **Forget Gate** ($f_t$) – Decides what past information should be discarded.

2. **Input Gate** ($i_t$) – Decides what new information to store.

3. **Output Gate** ($o_t$) – Controls what part of the memory cell is exposed as output.

  Each LSTM unit maintains a **cell state** ($C_t$), which allows information to persist across long sequences without being lost due to vanishing gradients.

Each LSTM cell performs the following operations:

1. **Forget Gate**:
$$f_t = \sigma(W_f \cdot [h_{t-1}, x_t] + b_f)$$
This gate determines which parts of the previous memory  $C_{t-1}$  should be kept or discarded (values closer to 0 are forgotten, values closer to 1 are retained).

2. **Input Gate & Candidate Cell Update**:
$$i_t = \sigma(W_i \cdot [h_{t-1}, x_t] + b_i)$$$$\tilde{C}t = \tanh(W_C \cdot [h{t-1}, x_t] + b_C)$$The input gate  $i_t$  decides which new information to update, and $\tilde{C}_t$  is the candidate value that could be added to the cell state.

3. **Update Cell State**:
$$C_t = f_t \cdot C_{t-1} + i_t \cdot \tilde{C}_t$$

  This is the key **memory update step** that allows the LSTM to selectively keep long-term information.

4. **Output Gate & Hidden State Update**:
$$o_t = \sigma(W_o \cdot [h_{t-1}, x_t] + b_o)$$$$h_t = o_t \cdot \tanh(C_t)$$
The output gate determines what part of the memory is revealed as the hidden state  $h_t$ , which is used for the next step in the sequence.