#!/bin/sh

sudo modprobe snd-pcm-oss
sudo sh -c "echo snd-pcm-oss >> /etc/modules"
export AUDIODEV=/dev/dsp1

#julius -C ~/julius-4.4.2/julius-kit/dictation-kit-v4.3.1-linux/main.jconf -C ~/julius-4.4.2/julius-kit/dictation-kit-v4.3.1-linux/am-gmm.jconf -nostrip

julius -C ~/julius-4.4.2/julius-kits/dictation-kit-v4.3.1-linux/word.jconf -module > /dev/null &
echo $!
sleep 3
