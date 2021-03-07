*Inspired from* **ChrEn: Cherokee-English Machine Translation for Endangered Language Revitalization**
Cherokee is a highly endangered Native American language spoken by the Cherokee people. The Cherokee culture is deeply embedded in its language. However, there are approximately only 2,000 fluent first language Cherokee speakers remaining in the world.

**Dataset** : ChrEn, a Cherokee-English parallel dataset, to facilitate machine translation research between
Cherokee and English.

Example sequence from the dataset is as follow.
**Chr** : ᎥᏝ ᎡᎶᎯ ᎠᏁᎯ ᏱᎩ, ᎾᏍᎩᏯ ᎠᏴ ᎡᎶᎯ ᎨᎢ ᏂᎨᏒᎾ ᏥᎩ.
**English** : They are not of the world, even as I am not of the world.

Compared to some popular machine translation language pairs, ChrEn is extremely low-resource, only containing 14k sentence pairs in total. 

We have  used Encoder-decoder archictecture for this transduction problem of Neural Machine Translation. Precisely, we have used Stacked LSTMs with Attention Mechanism.
we have used google's Sentencepiece to deal with tokenization and vocabulary making.
 Given a sentence,  we lookup the subword embedding from an embedding matrix,   we feed this embedding to a bidirectional encoder this yields hidden and cell state for both forward and backward LSTM. The forward and Backward Hidden and cell states are concatenated to get the final states.
 Now as the decoder is initialized we feed it a target sentence, at each step, we look for the embedding and concatenate it with *combined-out* vector and feed it to the decoder.
 We then use the encoder hidden states to compute Multiplication attention at each step to let the model decide where to put its attention on the input sequence.
We now concatenate the attention output with the decoder hidden state and pass this through a linear layer, tanh, and dropout to attain the combined-output vector.
we Produce a probability distribution over the target subwords at each time step. We then compute softmax with entropy loss between Probability distribution and OHE of Target subword. 
