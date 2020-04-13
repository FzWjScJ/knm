# knm
鼠标键盘流量包取证
---
## 使用方法：

~~~
usage:python(3) knm.py <cmd> [arg] [opts]
        cmds:
            keyboard (<datafile>) <outfile>
            mouse (<datafile>) <outfile>
            pca <pcadile>(<outfile>)    转换pca的USB流量为data(文件)
            -v          version
~~~

---

## 参数解释：

datafile：USB数据，可以通过pca获得

outfile：输出文件

keyboard（k）：解析键盘流量 

mouse（m）：解析鼠标流量

pca：将pcapng等USB流量包模式提取有用数据

-v：版本描述
