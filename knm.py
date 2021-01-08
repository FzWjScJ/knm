import sys,os
import matplotlib.pyplot as plot
from tqdm import tqdm

normalKeys = {
        "04":"a", "05":"b", "06":"c", "07":"d", "08":"e",
        "09":"f", "0a":"g", "0b":"h", "0c":"i", "0d":"j",
        "0e":"k", "0f":"l", "10":"m", "11":"n", "12":"o",
        "13":"p", "14":"q", "15":"r", "16":"s", "17":"t",
        "18":"u", "19":"v", "1a":"w", "1b":"x", "1c":"y",
        "1d":"z","1e":"1", "1f":"2", "20":"3", "21":"4",
        "22":"5", "23":"6","24":"7","25":"8","26":"9",
        "27":"0", "28":"<RET>", "29":"<ESC>", "2a":"<DEL>", "2b":"<ALT>",
        "2c":"<SPACE>","2d":"-","2e":"=","2f":"[","30":"]","31":"\\",
        "32":"<NON>", "33":";","34":"'", "35":"<GA>", "36":",", "37":".",
        "38":"/", "39":"<CAP>", "3a":"<F1>", "3b":"<F2>", "3c":"<F3>", "3d":"<F4>",
        "3e":"<F5>", "3f":"<F6>", "40":"<F7>", "41":"<F8>", "42":"<F9>", "43":"<F10>",
        "44":"<F11>", "45":"<F12>", "4a":"<HOME>", "4c":"<DELETE>", "4d":"<END>", "4f":"<RightArrow>", 
        "50":"<LeftArrow>", "51":"<DownArrow>", "52": "<UpArrow>", "53":"<NumLock>", "54":"/", 
        "55":"*", "56":"-", "57":"+", "58":"<RET>", "59":"1", "5a":"2", "5b":"3", "5c":"4", "5d":"5", 
        "5e":"6", "5f":"7", "60":"8", "61":"9", "62":"0"}
shiftKeys = {
        "04":"A", "05":"B", "06":"C", "07":"D", "08":"E",
        "09":"F", "0a":"G", "0b":"H", "0c":"I", "0d":"J",
        "0e":"K", "0f":"L", "10":"M", "11":"N", "12":"O", 
        "13":"P", "14":"Q", "15":"R", "16":"S", "17":"T",
        "18":"U", "19":"V", "1a":"W", "1b":"X", "1c":"Y",
        "1d":"Z","1e":"!", "1f":"@", "20":"#", "21":"$",
        "22":"%", "23":"^","24":"&","25":"*","26":"(","27":")",
        "28":"<RET>","29":"<ESC>","2a":"<DEL>", "2b":"<ALT>","2c":"<SPACE>",
        "2d":"_","2e":"+","2f":"{","30":"}","31":"|","32":"<NON>","33":"\"",
        "34":":","35":"<GA>","36":"<","37":">","38":"?","39":"<CAP>","3a":"<F1>",
        "3b":"<F2>", "3c":"<F3>","3d":"<F4>","3e":"<F5>","3f":"<F6>","40":"<F7>",
        "41":"<F8>","42":"<F9>","43":"<F10>","44":"<F11>","45":"<F12>", 
        "4a":"<HOME>", "4c":"<DELETE>", "4d":"<END>", "4f":"<RightArrow>", 
        "50":"<LeftArrow>", "51":"<DownArrow>", "52": "<UpArrow>", "53":"<NumLock>", "54":"/", 
        "55":"*", "56":"-", "57":"+", "58":"<RET>", "59":"1", "5a":"2", "5b":"3", "5c":"4", "5d":"5", 
        "5e":"6", "5f":"7", "60":"8", "61":"9", "62":"0"}
VERSION = 1.1

#获取指令
def start() -> int:
    if '-h' in sys.argv or '--help' in sys.argv or len(sys.argv) < 2:
        print('''
        usage:python(3) knm.py <cmd> [arg] [opts]
        cmds:
            pca <pcadile> (<outfile>)           转换pca的USB流量为data(文件)
            keyboard <datafile> (<outfile>)     识别提取出的data(文件)并还原data(文件)为键盘输入内容
            mouse <datafile> (<outfile>)        识别提取出的data(文件)并还原data(文件)为坐标并绘图
            -v          version                 读取版本号及作者信息
        ''')
        return 0
    cmd = sys.argv[1]
    if '-v' == sys.argv[1]:
        print('version:'+str(VERSION))
        print('Thanks to the auther DizzyK && FzWjScj')
        print('''
            If U find any problem, please take Ur issue into Github \
                https://github.com/Dizzy-K/knm OR https://github.com/FzWjScJ/knm''')
        return 0
    elif 'pca' == sys.argv[1] or 'p' == sys.argv[1]:
        return analyse_pca(cmd=cmd)
    elif 'mouse' == sys.argv[1] or 'm' == sys.argv[1]:
        return analyse_mouse(cmd=cmd)
    elif 'keyboard' in sys.argv or 'k' in sys.argv:
        return analyse_keyboard(cmd=cmd)
    else:
        return 1 #cmd wrong

# 提取usb流量信息
def analyse_pca(cmd) -> int:
    if 'pca' == sys.argv[1]:
        p = sys.argv.index('pca')
    elif 'p' == sys.argv[1]:
        p = sys.argv.index('p')
    if len(sys.argv) <= p+1:
        return 1 # cmd wrong
    if 'pcap' not in sys.argv[p+1]:
        return 4 # input wrong
    pca = str(sys.argv[p+1])
    if len(sys.argv) == p+2:
        sys.argv.append('outpca.txt')
        os.popen('tshark -r ' + pca + ' -T fields -e usb.capdata | sed \'/^\s*$/d\'> ' + sys.argv[p+2])
        return 3 # output wrong
    if len(sys.argv) == p+3:
        os.popen('tshark -r ' + pca + ' -T fields -e usb.capdata | sed \'/^\s*$/d\'> ' + sys.argv[p+2])
        print('done!')
        exit(1)
    else:
        print('Unknown Wrong, please take it into issue!')
        return 1 # other wrong

# 键盘流量分析
def analyse_keyboard(cmd) -> int:
    if 'keyboard' in sys.argv:
        p = sys.argv.index('keyboard')
    elif 'k' in sys.argv:
        p = sys.argv.index('k')
    if len(sys.argv) < p + 2:
        print('Missing file for keyboard')
        return 2
    elif len(sys.argv) == p + 2:
        sys.argv.append('outkeyboard.txt')
        print('Missing outputfile, it will named outkeyboard by default')
    output = []
    f1 = open(sys.argv[p+1],'r').readlines()
    f2 = open(sys.argv[p+2],'w')
    f1_ = tqdm(f1)
    print("Taking keyboard data...")
    for line in f1_:
        if ':' not in line:
            out = ''
            for i in range(0, len(line)-1, 2):
                if i + 2 != len(line):
                    out += line[i] + line[i + 1] + ":"
                else:
                    out += line[i] + line[i + 1]
        else:
            out = line
        try:
            if out[0] != '0' or (out[1] != '0' and out[1] != '2') or out[3] != '0' or out[4] != '0' or out[
                9] != '0' or out[10] != '0' or out[12] != '0' or out[13] != '0' or out[15] != '0' or out[
                16] != '0' or out[18] != '0' or out[19] != '0' or out[21] != '0' or out[22] != '0' or out[6:8] == "00":
                continue
            if out[6:8] in normalKeys.keys():
                output += [[normalKeys[out[6:8]]], [shiftKeys[out[6:8]]]][out[1] == '2']
            else:
                output += ['[unknown]']
        except:
            pass
    print("Done!\nClearing data...")
    for i in tqdm(range(len(output))):
        try:
            a=output.index('<DEL>')
            del output[a]
            del output[a-1]
        except:
            pass
        try:
            a=output.index('<RET>')
            del output[a]
            output.append('\n')
        except:
            pass
        try:
            a=output.index('<SPACE>')
            del output[a]
            output.append(' ')
        except:
            pass
        try:
            a=output.index('<ALT>')
            del output[a]
            output.append('\t')
        except:
            pass
    flag = ''
    for data in output:
        f2.write(data)
        flag += data
    print("Data of keyboard pca is :\n", flag, end='')
    f2.close()
    exit(1)

# 鼠标流量分析
def analyse_mouse(cmd) -> int:
    if 'mouse' in sys.argv:
        p = sys.argv.index('mouse')
    elif 'm' in sys.argv:
        p = sys.argv.index('m')
    if len(sys.argv) < p + 2:
        print('Missing file for mouse')
        return 2
    if len(sys.argv) == p + 2:
        sys.argv.append('outmouse.txt')
        print('Missing outputfile, it will named outmouse by default')
    name = sys.argv[p + 2].split('.')[0]
    keys = open(sys.argv[p+1],'r').readlines()
    f = open(sys.argv[p+2],'w')
    posx = 0
    posy = 0
    print('Taking Data...')
    for line in tqdm(keys):
        if ':' not in line:
            out = ''
            for i in range(0, len(line)-1, 2):
                if i + 2 != len(line):
                    out += line[i] + line[i + 1] + ":"
                else:
                    out += line[i] + line[i + 1]
        else:
            out = line
        if len(out) != 12:
            continue
        line = out[:12]
        x = int(line[3:5], 16)
        y = int(line[6:8], 16)
        if x > 127:
            x -= 256
        if y > 127:
            y -= 256
        posx += x
        posy += y
        btn_flag = int(line[0:2], 16)
        f.write(str(btn_flag))
        f.write(' ')
        f.write(str(posx))
        f.write(' ')
        f.write(str(posy))
        f.write('\n')
    f.close()
    print('Done!')
    change = input('Do U want to draw out?(Y/N)')
    if change == 'Y' or change == 'y' or change == '':
        draw_mouse(filename=name)
    else:
        exit(1)

# 鼠标坐标作图
def draw_mouse(filename="outmouse"):
    print('Drawing...')
    a = input('Please input numof U want:\n0:All\n1:Only Left\n2:Only Right\n3:All of above\n')
    if a == '0' or a == '1' or a == '2':
        a = int(a)
        fig = plot.figure()
        ax = fig.add_subplot(111)
        ax.set(title='QTMD', ylabel='nmb', xlabel='nmd')
        print('Drawing...')
        with open("outmouse.txt", 'r') as f:
            for i in tqdm(f.readlines()):
                btn_flag = int(i.split()[0])
                x = int(i.split()[1])
                y = int(i.split()[2])
                if btn_flag == a:
                    ax.plot(x, y, 'b.')

    elif a == '3':
        fig, axs = plot.subplots(2, 2)
        #print(type(axs))
        ax1 = axs[0, 0]
        ax2 = axs[0, 1]
        ax3 = axs[1, 0]
        ax4 = axs[1, 1]
        with open("outmouse.txt", 'r') as f:
            for i in tqdm(f.readlines()):
                btn_flag = int(i.split()[0])
                x = int(i.split()[1])
                y = int(i.split()[2])
                if btn_flag == 0:
                    ax1.plot(x, y, 'b.', label='All')
                    ax1.set_title('All')
                elif btn_flag == 1:
                    ax2.plot(x, y, 'r.', label='Left')
                    ax2.set_title('Left')
                elif btn_flag == 2:
                    ax3.plot(x, y, 'g.', label='Right')
                    ax3.set_title('Right')
    print('Saving...')              
    plot.savefig('./'+filename+'.png')
    print('Picture have save as '+filename+a+'.png')
    print('Done!')    
    plot.show()

if __name__ == '__main__':
    error = start()
    if error == 1:
        print("Wrong cmd")
    elif error == 2:
        print('Missing input file')
    elif error == 3:
        print('Missing outputfile, it will named outpca by default')
    elif error == 4:
        print('Wrong input file')