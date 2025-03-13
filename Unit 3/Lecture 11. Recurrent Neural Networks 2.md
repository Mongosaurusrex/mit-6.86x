- Formulate, estimate and sample sequences from Markov models.
    
- Understand the relation between RNNs and Markov model for generating sequences.
    
- Understand the process of **decoding** of RNN in generating sequences.

## Markov Models

Markov Language Models are probabilistic models used for generating and predicting sequences of words based on the Markov assumption, which states that the probability of a word depends only on a fixed number of preceding words. In an _n_-gram Markov model, the probability of a word is conditioned on the previous ($n_{-1}$) words, allowing for efficient modeling of language patterns while maintaining computational feasibility. These models are commonly used in applications like speech recognition, text generation, and autocomplete systems. However, they struggle with long-range dependencies due to their limited context window and often require smoothing techniques to handle unseen word sequences. Despite their simplicity, they serve as a foundational approach to language modeling and have been largely supplanted by neural models like transformers in modern NLP.

## RNN for sequences
![[Pasted image 20250310083609.png]]



