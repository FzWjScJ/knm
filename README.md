# knm

> 鼠标键盘流量包分析取证  
> author:[**FzWjScj**](https://github.com/FzWjScJ)、[**DizzyK**](https://github.com/Dizzy-K)

---

## 环境要求

1. python库
   1. matplotlib
   2. tqdm
2. tshark(作者还没研究明白pyshark，暂时只能先靠着tshark提取。别问，问就是DizzyK菜，没得洗呜呜呜)

### 安装方法

```bash
pip install -r requestment.txt
apt-get install tshark
```

## 使用方法

```bash
python knm.py <cmd> [arg] [opts]
        cmds:
            pca(p) <pcadile> (<outfile>)            转换pca的USB流量为data(文件)
            keyboard(k) <datafile> (<outfile>)      识别提取出的data(文件)并还原data(文件)为键盘输入内容
            mouse(m) <datafile> (<outfile>)         识别提取出的data(文件)并还原data(文件)为坐标并绘图
            -v          version                     读取版本号及作者信息
```

---

## 参数解释

datafile：USB数据，可以通过初始流量包获得  
outfile：输出文件(可以不输入，不输入时默认为outpca、outmouse、outkeyboard)  
keyboard(k)：解析键盘流量  
mouse(m)：解析鼠标流量  
pca(p)：将pcapng等USB流量包模式提取有用数据  
-v：版本描述及作者信息  

---

## 功能讲述

### DONE

- [x] 读取流量包信息
- [x] 分析鼠标、键盘流量
- [x] 代码重构
- [x] 键盘流量直接输出内容
- [x] 键盘流量扩容字典
- [x] 鼠标流量作图
  - 轨迹作图
  - 左右键作图
- [x] 更改pca的输出，使之能够更好的应用于mouse和keyboard
- [x] 报错信息完善
  - cmd wrong
  - 流量包文件不存在
  - 未指明输出文件(默认为outpca、outmouse、outkeyboard)
  - keyboard、mouse输入文件格式错误
- [x] 进度条

### TODO

- [ ] *自动识别流量类别*
- [ ] 外设流量分析
  - [ ] 触摸板
  - [ ] 打击垫
  - [ ] *手柄*
- [ ] 不标准的鼠标键盘流量协议分析
- [ ] pyshark代替tshark
- [ ] And so on......

---

## 使用范例

1. 提取USB流量信息

   ```python
   python knm.py p usb.pcap [output filename]
   ```

   在当前文件夹得到提取结果(若未填写[output filename], 则默认为outpca.txt)

2. 提取键盘流量信息

   ```python
   python knm.py k [input filename] [output filename]
   ```

   其中, [input filename]为必填项(若未填写[output filename], 则默认为outkeyboard.txt)。  
   在当前文件夹得到提取结果并将结果直接打印在终端上。

3. 提取鼠标流量信息

   ```python
   python knm.py m [input filename] [output filename]
   ```

   其中, [input filename]为必填项(若未填写[output filename], 则默认为outmouse.txt)  
   在当前文件夹得到提取结果并询问是否按照坐标点作图

4. 作图  
   直接输入序号(0\1\2\3)  
   0. 作出全部鼠标轨迹图
   1. 作出鼠标左击轨迹图
   2. 是作出鼠标右击轨迹图
   3. 是将上述三幅图合成一幅输出(但精度较低,请酌情使用)
