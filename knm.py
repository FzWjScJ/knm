from email.policy import default
import sys,os
import click
from sqlalchemy import null, over
from tqdm import tqdm
import matplotlib.pyplot as plot

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
VERSION = 2.0

@click.group()
@click.version_option(version=VERSION)
def main():
    """主要功能：\n
    1.addr 快速查看usb流量所有地址\n
    2.pca pcap转为data文件\n
    3.keyboard data转为keyboard文件\n
    4.mouse data转为mouse文件\n"""
    pass


#一把梭导出数据,把数据转换为data文件
@click.command()
@click.option('-inputfile','-i',type=str ,help='输入文件')
@click.option('-output','-o',default="out.txt",type=str ,help='输出文件')


#分类
def pca(inputfile,output):
    """Usage: python knm.py pca -i input.pcap -o output.data"""
    print('选择接下来的操作')
    print('1.直接转换为data文件')
    print('2.过滤指定地址后选择data文件')
    choice = input(">")
    if choice == '1':
        print('请选择数据类型(usb.capdata/usbhid.data)输入1/2')
        c_type = input(">")
        if c_type == '1':
            os.popen('tshark -r ' + inputfile + ' -T fields -e usb.capdata | sed \'/^\s*$/d\'> ' + output)
            click.echo("done！")
        else:
            os.popen('tshark -r ' + inputfile + ' -T fields -e usbhid.data | sed \'/^\s*$/d\'> ' + output)
            click.echo("done！")

    elif choice == '2':
        print('请输入过滤地址,使用前建议使用addr查看所有地址\nUsage:2.10.1')
        filter = input(">")
        print('请选择数据类型(usb.capdata/usbhid.data)输入1/2')
        c_type = input(">")
        if c_type == '1':
            exp = 'tshark -r ' + inputfile + ' -T fields -e usb.capdata -Y "usb.addr == \\"'+ filter +'\\""| sed \'/^\s*$/d\'> ' + output
            os.popen(exp)
            click.echo("done！")
        else:
            exp = 'tshark -r ' + inputfile + ' -T fields -e usbhid.data -Y "usb.addr == \\"'+ filter +'\\""| sed \'/^\s*$/d\'> ' + output
            # os.popen('tshark -r ' + inputfile + ' -T fields -e usbhid.data -Y usb.addr == "'+ filter +'"| sed \'/^\s*$/d\'> ' + output)
            os.popen(exp)
            click.echo("done！")



#快速分析目标USB地址
@click.command()
@click.option('--inputfile','-i',nargs=1,type=str,help='目标文件')
@click.option('--pcatype','-t',type=click.Choice(['old', 'new']),help='USB流量版本选择(默认为old)')

def addr(inputfile,pcatype):
    """Usage: python knm.py addr -i input.pcap -t old/new"""
    if not pcatype:
        pcatype = 'old'
    if pcatype == 'old':    
        os.system('tshark -r ' + inputfile + ' -T fields -e usb.addr -Y usb.capdata | sort | uniq -c | sort -nr | head')
        click.echo("done！")
    elif pcatype == 'new':
        os.system('tshark -r ' + inputfile + ' -T fields -e usb.addr -Y usbhid.data | sort | uniq -c | sort -nr | head')
        click.echo('done!')

#直接输出键盘流量

@click.command()
@click.option('--inputfile','-i',nargs=1,type=str,help='目标data文件')

def keyboard(inputfile):
    """Usage: python knm.py keyboard -i input.data"""
    output = []
    f1 = open(inputfile,'r').readlines()
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
    
    print("Done!\n是否按照原始数据显示?(y/n)")
    flag = ''
    for data in output:
        flag += data
    if input('>') == 'y':
        print("Data of keyboard pca is :\n", flag, end='')
    else:
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
            try:
                a=output.index('<CAP>')
                del output[a]
            except:
                pass
        flag = ''
        for data in output:
            flag += data
        print("Data of keyboard pca is :\n", flag, end='')

#鼠标流量分析
@click.command()
@click.option('--inputfile','-i',nargs=1,type=str,help='目标data文件')
@click.option('--outputfile','-o',default="outmouse.txt",nargs=1,type=str,help='输出文件')


def mouse(inputfile,outputfile):
    """Usage: python knm.py mouse -i input.data"""
    keys = open(inputfile,'r').readlines()
    f = open(outputfile,'w')
    name = outputfile.split('.')[0]
    posx = 0
    posy = 0
    print('Taking Data...')
    for line in tqdm(keys):
        # if ':' not in line:
        #     out = ''
        #     for i in range(0, len(line)-1, 2):
        #         if i + 2 != len(line):
        #             out += line[i] + line[i + 1] + ":"
        #         else:
        #             out += line[i] + line[i + 1]
        # else:
        #     out = line
        # if len(out) != 12:
        #     continue
        # line = out[:12]

        #↑↑↑上述无效代码↑↑↑



        #注：根据题目情况与偏移地址不同，酌情修改此处的值
        #例如2020 DASCTF八月赛-misc-eeeeeeeasyusb需要把里面的值改为4:6,8:10
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
    plot.savefig('./'+filename+str(a)+'.png')
    print('Picture have save as '+filename+str(a)+'.png')
    print('Done!')    
    plot.show()


main.add_command(pca)
main.add_command(addr)
main.add_command(keyboard)
main.add_command(mouse)
if __name__ == '__main__':
    main()