# AI Stock Trading Agent

### About
This repository contains project work to build a Q-learning neural network stock trading agent.

### Install
* Python 2.7
* pandas
* numpy
* pandas_datareader
* matplotlib
* datetime
* random
* timeit
* keras (https://keras.io/)
* Theano (http://deeplearning.net/software/theano/install.html#install)

### Code Setup
If all necessary libraries and dependencies are installed, run qlearning_trader.ipynb. Note that the data retrieved runs up to the current date. To use the data I originally used (stored in data folder), skip down to the implementation section of the notebook. Run code from there forward.

### Folders
* data - stores price, technical, and spy data in pkl format
* logs - stores evaluation text output from trading agent
* plots - stores evaluation plot output from trading agent

### Works Referenced
* http://www.nature.com/nature/journal/v529/n7587/full/nature16961.html
* https://www.cs.toronto.edu/~vmnih/docs/dqn.pdf
* https://webdocs.cs.ualberta.ca/~sutton/papers/sutton-92-ISKIT.pdf
* https://webdocs.cs.ualberta.ca/~sutton/papers/sutton-90.pdf
* https://hackernoon.com/the-self-learning-quant-d3329fcc9915#.r6pzeoc2i
