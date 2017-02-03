#! python3
# pLocker.py - An INSECURE password locker program.

import sys
import pyperclip
import time
import shelve
import os

if len(sys.argv) < 2:
    print('''Usage:
pLocker.py [account] - copy account password
pLocker.py remove [account] - remove account from list
pLocker.py change [account] - change saved password for account''')
    input('Hit any key to exit ')
    sys.exit()
    
if len(sys.argv) == 2:
    account = sys.argv[1]
    if 'mydata.dat' not in os.listdir():
        print('Program opened for the first time. Creating necessary data...')
        shelveFile = shelve.open('mydata')
        accountsDict = {}
        shelveFile['accountsDict'] = accountsDict
        shelveFile.close()

    shelveFile = shelve.open('mydata')
    accountsDict = shelveFile['accountsDict']
    if account in accountsDict:
        pyperclip.copy(accountsDict[account])
        print('Password for ' + account + ' copied to clipboard.')
        time.sleep(1)
    else:
        password = input('There is no account named ' + account + \
                         '. What password should I add to this account? (or hit Enter to quit) ')
        if password == '':
            shelveFile.close()
            sys.exit()
        else:
            accountsDict[account] = password
            shelveFile['accountsDict'] = accountsDict
            pyperclip.copy(accountsDict[account])
            shelveFile.close()
            print('Password for ' + account + ' saved and copied to clipboard.')
            time.sleep(1)

if len(sys.argv) >= 3:
    account = sys.argv[2]
    if 'mydata.dat' not in os.listdir():
        print('Program opened for the first time. Given instruction is not possible.')
        time.sleep(1)
        sys.exit()
    shelveFile = shelve.open('mydata')
    accountsDict = shelveFile['accountsDict']
    if account in accountsDict:
        if sys.argv[1] == 'remove':
            print('Removing ' + account + ' from a list...')
            del accountsDict[account]
            shelveFile['accountsDict'] = accountsDict
        elif sys.argv[1] == 'change':
            password = input('What password should I add to ' + account + '? ')
            print('Changing password for ' + account + ' to ' + password + ' ...')
            accountsDict[account] = password
            shelveFile['accountsDict'] = accountsDict
        else:
            print('Instruction not understood. Closing...')
        shelveFile.close()
        time.sleep(1)
        sys.exit()
