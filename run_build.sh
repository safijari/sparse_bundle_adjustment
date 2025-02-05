#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
#sudo docker build --no-cache -t sba_builder .
yum install eigen3-devel
cd /tmp
wget https://gitlab.com/libeigen/eigen/-/archive/3.3.3/eigen-3.3.3.tar.gz
sudo tar -xzf eigen-3.3.3.tar.gz
cd -
sudo docker run -v $DIR:/repo -v /tmp/eigen-3.3.3:/eigenfolder --rm sba_builder /repo/build.sh
