#!/bin/bash
#
#export PYTHONPATH="..:$PYTHONPATH"
basepath=$(cd `dirname $0`; pwd)
echo "添加 $basepath 到PYTHONPATH"
#export PYTHONPATH=./ # 将项目根目录作为PYTHONPATH
export PYTHONPATH="..:$PYTHONPATH"





