
# coding: utf-8

# In[ ]:

from time import time

from wavenet.utils import make_batch, mu_law_bins
from wavenet.models import Model, Generator

from IPython.display import Audio

import numpy as np

inputs, targets = make_batch('assets/voice.wav')
num_time_samples = inputs.shape[1]
num_channels = 1
gpu_fraction = 1.0

model = Model(num_time_samples=num_time_samples,
              num_channels=num_channels,
              gpu_fraction=gpu_fraction)

Audio(inputs.reshape(inputs.shape[1]), rate=16000)


# In[ ]:

tic = time()
model.train(inputs, targets)
toc = time()

print('Training took {} seconds.'.format(toc-tic))


# In[ ]:

generator = Generator(model)

# Get first sample of input
input_ = inputs[:, 0:1, 0]

tic = time()
predictions = generator.run(input_, 32000)
toc = time()
print('Generating took {} seconds.'.format(toc-tic))


# In[ ]:

Audio(predictions, rate=44100)

