# TradingHub

环境名称
```
conda create -n TradingHub python=3.6
```
进入环境
```
source activate TradingHub
```
退出环境
```
source deactivate
```

在环境里面到配置文件列单所在目录，安装环境依赖
```
pip install --upgrade pip

pip freeze >requirements.txt
pip install -r requirements.txt
```
检查环境配置
```
pip list
```
删除虚拟环境
```
conda remove -n TradingHub --all
```
删除环境中的某个包
```
conda remove --name TradingHub package_name
```
