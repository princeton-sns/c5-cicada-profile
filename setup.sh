#!/usr/bin/env sh

# for g++-5
sudo apt-get update
sudo apt-get install -y software-properties-common
sudo add-apt-repository -y ppa:ubuntu-toolchain-r/test

# common
sudo apt-get update
sudo apt-get install -y build-essential cmake git g++-5 libjemalloc-dev libnuma-dev libaio-dev
# for Silo
sudo apt-get install -y libdb6.0++-dev
# for FOEDUS/MOCC
sudo apt-get install -y libgoogle-perftools-dev papi-tools

# for experiments
sudo apt-get install -y psmisc python3

# for analysis
sudo apt-get install -y python3-pip
sudo apt-get install -y texlive-generic-recommended texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended texlive-fonts-extra dvipng
pip3 install --user 'pandas>=0.20,<0.21' 'pandasql>=0.7,<0.8' 'matplotlib>=1.5,<2.0'

# for non-interactive experiment execution
echo "`whoami` ALL=(ALL:ALL) NOPASSWD:ALL" | sudo tee -a /etc/sudoers

# for third-party engines
echo "`whoami` - memlock unlimited" | sudo tee -a /etc/security/limits.conf
echo "`whoami` - nofile 655360" | sudo tee -a /etc/security/limits.conf
echo "`whoami` - nproc 655360" | sudo tee -a /etc/security/limits.conf
echo "`whoami` - rtprio 99" | sudo tee -a /etc/security/limits.conf

sudo groupadd hugeshm
sudo usermod -a -G hugeshm `whoami`

# Clone repo
sudo git clone --recursive https://github.com/efficient/cicada-exp-sigmod2017.git /usr/local/src

