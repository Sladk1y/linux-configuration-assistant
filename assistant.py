import os

os.system('clear')
print('Welcome\nto\nlinux\nconfiguration\nassistant\nby SLACK1Y')
print()
while True:
    print('If you need help write "help"')
    packages = input('Write the packages you would like to install: ')
    exceptions = ['0', 'help', '"help"', 'gupdate']
    if packages not in exceptions:
        os.system(f'pacman -S {packages}')
    elif packages == 'help' or packages == '"help"':
        print('--------------------------------------------\n\nHelp installing packages in Linux.')
        print("""
        Update gnome - update.
        Install the package - write the name in the line.""")
        print('\n\n--------------------------------------')
    elif packages == 'gupdate':
        print('\n')
        print('Instructions for updating GNOME to version 42:')
        print('1.In the text editor that opens, add or replace the lines:')
        os.system('gedit /etc/pacman.conf')
        print('''
        [fcgu]
        Server = https://gnome.holmie.xyz/$repo
        Server = https://$repo.fabis.cafe/$repo
        Server = https://vmi394248.contaboserver.net/$repo''')
        print('2.When you edit the file, write yes in the line that appears.')
        yesno = input('Write yes in this line: ')
        if yesno == 'yes':
            os.system('pacman -Syu')
        else:
            print('Gnome update has been canceled')
    else:
        break
