# knm

> 鼠标键盘流量包分析取证  
>
> 全新重构2.0
>
> author:[**FzWjScj**](https://github.com/FzWjScJ)、[**DizzyK**](https://github.com/Dizzy-K)、[**Snowywar**](https://github.com/jiayuqi7813/)

---

## 前言

使用了click库对整体交互进行了重构，优化了过往键盘数据显示，修复了鼠标流量无法正常绘制的bug。

### 优化：

1. 键盘流量转换为数据完全显示和最终显示
2. 修复了鼠标流量无法正常绘制
3. 整体功能细化，交互人性化

### 新功能：

1. 新增一键查看流量包中所有usb地址
2. 新增pca转data导出时自定义地址过滤
3. keyboard转换数据时输出原始数据或者最终数据

## 环境要求

1. python库
   1. matplotlib
   2. tqdm
   2. click
2. tshark

### 安装方法

```bash
pip install -r requestment.txt
apt-get install tshark
```

## 使用方法

```bash
Usage: knm.py [OPTIONS] COMMAND [ARGS]...

  主要功能：

  1.addr 快速查看usb流量所有地址

  2.pca pcap转为data文件

  3.keyboard data转为keyboard文件

  4.mouse data转为mouse文件

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  addr      Usage: python knm.py addr -i input.pcap -t old/new
  keyboard  Usage: python knm.py keyboard -i input.data
  mouse     Usage: python knm.py mouse -i input.data
  pca       Usage: python knm.py pca -i input.pcap -o output.data

```

---

## 参数解释

addr:一键输出目标流量包所有地址内容

keyboard：解析键盘流量  
mouse：解析鼠标流量  
pca：将pcapng等USB流量包模式提取有用数据  
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
- [x] 进度条
- [x] 不标准的鼠标键盘流量协议分析

### TODO

- [ ] *自动识别流量类别*
- [ ] 外设流量分析
  - [ ] 触摸板
  - [ ] 打击垫
  - [ ] *手柄*
- [ ] pyshark代替tshark
- [ ] And so on......

---

## 使用范例

1. 查看目标流量的全部USB地址信息（new代表usbhid.data,old代表usb.capdata）

   ```
   python3 knm.py addr -i usb.pcapng -t new                                           
   ```

2. 提取USB流量信息

   ```python
   python knm.py pca -i usb.pcapng -o out.txt
   ```

   在当前文件夹得到提取结果(若未填写[output filename], 则默认为out.txt)

   后续会有引导，按照后续内容所选进行输出不同内容

   ![image-20220531195010887](.\img\1.png)

3. 提取键盘流量信息

   ```python
   python knm.py keyboard [input filename] [output filename]
   ```

   其中, [input filename]为必填项(若未填写[output filename], 则默认为outkeyboard.txt)。  
   在当前文件夹得到提取结果并将结果直接打印在终端上。

   后续仍有引导，两种效果如下，自行根据题目所需进行选择

   ![image-20220531195415864](.\img\2.png)

3. 提取鼠标流量信息

   ```python
   python knm.py mouse [input filename] [output filename]
   ```

   其中, [input filename]为必填项(若未填写[output filename], 则默认为outmouse.txt)  
   在当前文件夹得到提取结果并询问是否按照坐标点作图

4. 作图  
   直接输入序号(0\1\2\3)  
   0: 作出全部鼠标轨迹图
   1: 作出鼠标左击轨迹图
   2: 是作出鼠标右击轨迹图
   3: 是将上述三幅图合成一幅输出(但精度较低,请酌情使用)
