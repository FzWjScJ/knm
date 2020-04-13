import sys,os
normalKeys = {
    "04":"a", "05":"b", "06":"c", "07":"d", "08":"e",
    "09":"f", "0a":"g", "0b":"h", "0c":"i", "0d":"j",
     "0e":"k", "0f":"l", "10":"m", "11":"n", "12":"o",
      "13":"p", "14":"q", "15":"r", "16":"s", "17":"t",
       "18":"u", "19":"v", "1a":"w", "1b":"x", "1c":"y",
        "1d":"z","1e":"1", "1f":"2", "20":"3", "21":"4",
         "22":"5", "23":"6","24":"7","25":"8","26":"9",
         "27":"0","28":"<RET>","29":"<ESC>","2a":"<DEL>", "2b":"\t",
         "2c":"<SPACE>","2d":"-","2e":"=","2f":"[","30":"]","31":"\\",
         "32":"<NON>","33":";","34":"'","35":"<GA>","36":",","37":".",
         "38":"/","39":"<CAP>","3a":"<F1>","3b":"<F2>", "3c":"<F3>","3d":"<F4>",
         "3e":"<F5>","3f":"<F6>","40":"<F7>","41":"<F8>","42":"<F9>","43":"<F10>",
         "44":"<F11>","45":"<F12>"}
shiftKeys = {
    "04":"A", "05":"B", "06":"C", "07":"D", "08":"E",
     "09":"F", "0a":"G", "0b":"H", "0c":"I", "0d":"J",
      "0e":"K", "0f":"L", "10":"M", "11":"N", "12":"O",
       "13":"P", "14":"Q", "15":"R", "16":"S", "17":"T",
        "18":"U", "19":"V", "1a":"W", "1b":"X", "1c":"Y",
         "1d":"Z","1e":"!", "1f":"@", "20":"#", "21":"$",
          "22":"%", "23":"^","24":"&","25":"*","26":"(","27":")",
          "28":"<RET>","29":"<ESC>","2a":"<DEL>", "2b":"\t","2c":"<SPACE>",
          "2d":"_","2e":"+","2f":"{","30":"}","31":"|","32":"<NON>","33":"\"",
          "34":":","35":"<GA>","36":"<","37":">","38":"?","39":"<CAP>","3a":"<F1>",
          "3b":"<F2>", "3c":"<F3>","3d":"<F4>","3e":"<F5>","3f":"<F6>","40":"<F7>",
          "41":"<F8>","42":"<F9>","43":"<F10>","44":"<F11>","45":"<F12>"}
VERSION = 0.1

def start():
    if '-h' in sys.argv or '--help' in sys.argv or len(sys.argv) < 2:
        print('''
        usage:python(3) knm.py <cmd> [arg] [opts]
        cmds:
            keyboard (<datafile>) <outfile>
            mouse (<datafile>) <outfile>
            pca <pcadile>(<outfile>)    转换pca的USB流量为data(文件)
            -v          version
        ''')
        exit(1)
    cmd = sys.argv[1]
    if cmd != 'keyboard' and cmd != 'k' and cmd != 'mouse' and cmd != 'm' and cmd != 'pca' and cmd != 'p' and cmd != '-v':
        print("Wrong cmd")
        exit(1)
    if '-v' in sys.argv:
        print('version:'+VERSION)
        exit(1)
    if 'pca' in sys.argv or 'p' in sys.argv:
        if 'pca' in sys.argv:
            p = sys.argv.index('pca')
        elif 'p' in sys.argv:
            p = sys.argv.index('p')
        if len(sys.argv) <= p+1:
            print('Missing pca file for pca')
            exit(1)
        pca = str(sys.argv[p+1])
        if len(sys.argv) == p+3:
            os.popen('tshark -r ' + pca + ' -T fields -e usb.capdata > ' + sys.argv[p+2])
            exit(1)
        # elif len(sys.argv) == p+2:
        #     data = os.popen('tshark -r ' + pca + ' -T fields -e usb.capdata').read()
        #     if 'keyboard' in sys.argv or 'k' in sys.argv:
        #         if 'keyboard' in sys.argv:
        #             p = sys.argv.index('keyboard')
        #         elif 'k' in sys.argv:
        #             p = sys.argv.index('k')
        #         if len(sys.argv) <= p + 1:
        #             print('Missing file for keyboard')
        #             exit(1)
        #         output = []
        #         f2 = open(sys.argv[p + 2], 'a')
        #         for line in data:
        #             if ':' not in line:
        #                 for i in range(0, len(line)-1, 2):
        #                     if i + 2 != len(line):
        #                         out += line[i] + line[i + 1] + ":"
        #                     else:
        #                         out += line[i] + line[i + 1]
        #             else:
        #                 out = line
        #             try:
        #                 if out[0] != '0' or (out[1] != '0' and out[1] != '2') or out[3] != '0' or out[4] != '0' or out[
        #                     9] != '0' or out[10] != '0' or out[12] != '0' or out[13] != '0' or out[15] != '0' or out[
        #                     16] != '0' or out[18] != '0' or out[19] != '0' or out[21] != '0' or out[22] != '0' or out[
        #                                                                                                           6:8] == "00":
        #                     continue
        #                 if out[6:8] in normalKeys.keys():
        #                     output += [[normalKeys[out[6:8]]], [shiftKeys[out[6:8]]]][out[1] == '2']
        #                 else:
        #                     output += ['[unknown]']
        #             except:
        #                 pass
        #         for data in output:
        #             f2.write(data)
        #         f2.close()
        #         exit(1)
    	else:
    		print('Missing pca file for pca')
            exit(1)

            if 'mouse' in sys.argv or 'm' in sys.argv:
                if 'mouse' in sys.argv:
                    p = sys.argv.index('mouse')
                else:
                    p = sys.argv.index('m')
                if len(sys.argv) <= p + 1:
                    print('Missing file for mouse')
                    exit(1)
                keys = data
                f = open(sys.argv[p + 2], 'w')
                posx = 0
                posy = 0
                for line in keys:
                    if ':' not in line:
                        out = ''
                        for i in range(0, len(line)-1, 2):
                            if i + 2 != len(line):
                                out += line[i] + line[i + 1] + ":"
                            else:
                                out += line[i] + line[i + 1]
                    else:
                        out = line
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
                    if btn_flag == 1:
                        f.write(str(posx))
                        f.write(' ')
                        f.write(str(posy))
                        f.write('\n')
                f.close()
                exit(1)


    if 'keyboard' in sys.argv or 'k' in sys.argv:
        if 'keyboard' in sys.argv:
            p = sys.argv.index('keyboard')
        elif 'k' in sys.argv:
            p = sys.argv.index('k')
        if len(sys.argv) <= p + 2:
            print('Missing file for keyboard')
            exit(1)
        output = []
        f1 = open(sys.argv[p+1],'r').readlines()
        f2 = open(sys.argv[p+2],'a')
        for line in f1:
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
                    16] != '0' or out[18] != '0' or out[19] != '0' or out[21] != '0' or out[22] != '0' or out[                                                                                      6:8] == "00":
                    continue
                if out[6:8] in normalKeys.keys():
                    output += [[normalKeys[out[6:8]]], [shiftKeys[out[6:8]]]][out[1] == '2']
                else:
                    output += ['[unknown]']
            except:
                pass
        for data in output:
            f2.write(data)
        f2.close()
        exit(1)

    if 'mouse' in sys.argv or 'm' in sys.argv:
        if 'mouse' in sys.argv:
            p = sys.argv.index('mouse')
        elif 'm' in sys.argv:
            p = sys.argv.index('m')
        if len(sys.argv) <= p + 2:
            print('Missing file for mouse')
            exit(1)
        keys = open(sys.argv[p+1],'r').readlines()
        f = open(sys.argv[p+2],'w')
        posx = 0
        posy = 0
        for line in keys:
            if ':' not in line:
                out = ''
                for i in range(0, len(line)-1, 2):
                    if i + 2 != len(line):
                        out += line[i] + line[i + 1] + ":"
                    else:
                        out += line[i] + line[i + 1]
            else:
                out = line
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
            if btn_flag == 1:
                f.write(str(posx))
                f.write(' ')
                f.write(str(posy))
                f.write('\n')
        f.close()
        exit(1)

if __name__ == '__main__':
    start()
