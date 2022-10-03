#!/bin/bash

# Using Ubuntu
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt-get install -y nodejs

cd ~/Desktop/monster

git clone https://github.com/dorna-robotics/dorna2-python.git
cd dorna2
sudo python3 setup.py install --force

cd ../server
pip install flask networkx
