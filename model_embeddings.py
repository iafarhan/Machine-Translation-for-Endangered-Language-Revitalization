#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import torch.nn as nn
from vocab import *

class ModelEmbeddings(nn.Module): 
    """
    Class that converts input words to their embeddings.
    """
    def __init__(self, embed_size, vocab):
        """
        Init the Embedding layers.

        @param embed_size (int): Embedding size (dimensionality)
        @param vocab (Vocab): Vocabulary object containing src and tgt languages
                              See vocab.py for documentation.
        """
        super(ModelEmbeddings, self).__init__()
        self.embed_size = embed_size

        # default values
        self.source = None
        self.target = None

        src_pad_token_idx = vocab.src['<pad>']
        tgt_pad_token_idx = vocab.tgt['<pad>']

        num_emb_src = len(vocab.src) # chr
        num_emb_tgt = len(vocab.tgt) #eng

        self.source = nn.Embedding(num_embeddings=num_emb_src, embedding_dim=self.embed_size, padding_idx= src_pad_token_idx)
        self.target = nn.Embedding(num_embeddings=num_emb_tgt, embedding_dim=self.embed_size, padding_idx=tgt_pad_token_idx)
        ### END YOUR CODE


# if __name__=="__main__":
#     vocab = Vocab.load('./vocab.json')
#     emb = ModelEmbeddings(10,vocab)
#     print(emb.source)