<<<<<<< HEAD
##!/bin/sh
=======
#!/bin/sh
>>>>>>> b6e1f3667a904f59cbec8ac4d02b1f3daa1d6666

sudo modprobe snd-pcm-oss
sudo sh -c "echo snd-pcm-oss >> /etc/modules"
export AUDIODEV=/dev/dsp1

<<<<<<< HEAD
#julius -C ~/julius-4.4.2/julius-kit/dictation-kit-v4.3.1-linux/main.jconf -C ~/julius-4.4.2/julius-kit/dictation-kit-v4.3.1-linux/am-gmm.jconf -nostrip -module > /dev/null &

julius -C ~/julius-4.4.2/julius-kit/dictation-kit-v4.3.1-linux/word.jconf -module #> /dev/null &
#echo $!

=======
#julius -C ~/julius-4.4.2/julius-kit/dictation-kit-v4.3.1-linux/main.jconf -C ~/julius-4.4.2/julius-kit/dictation-kit-v4.3.1-linux/am-gmm.jconf -nostrip

julius -C ~/julius-4.4.2/julius-kits/dictation-kit-v4.3.1-linux/word.jconf -module > /dev/null &
echo $!
>>>>>>> b6e1f3667a904f59cbec8ac4d02b1f3daa1d6666
sleep 3
