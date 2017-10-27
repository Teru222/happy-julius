#!/bin/sh                                                                        

export AUDIODEV=/dev/dsp1

julius -C ~/julius-4.4.2/julius-kit/dictation-kit-v4.3.1-linux/main.jconf -C ~/j\
ulius-4.4.2/julius-kit/dictation-kit-v4.3.1-linux/am-gmm.jconf -nostrip
