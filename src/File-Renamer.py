import src.tools.Prefixer as Prefixer
import src.tools.Console as Console

if __name__ == '__main__':
    # Get Folder Path from User
    print('WARNING!\nPlease only have files in the directory!\n\n')
    folder = input('Folder Path:\n> ')
    if not folder[-1] == '\\':
        folder += '\\'
    Console.clear()

    # Initialize Prefixer
    prefixer = Prefixer.Prefixer(folder)

    # Get Prefixer Option from User
    # And Check User Input
    valid_input = False
    while not valid_input:
        print('Please select an option:')
        print('[1] Custom String')
        print('[2] Creation Date')
        print('[3] Modified Date')
        print('[4] Track Number (Only MP3)')
        choice = int(input('Your choice:\n> '))
        if 1 <= choice <= 4:
            valid_input = True
        else:
            Console.clear()
            print('PLEASE SELECT A VALID OPTION!')

    # Process Choice
    Console.clear()
    if choice == 1:
        custom_string = input('Please enter the custom string:\n>')
        prefixer.prefix_string(custom_string)
    elif choice == 2:
        prefixer.prefix_cdate()
    elif choice == 3:
        prefixer.prefix_mdate()
    elif choice == 4:
        prefixer.prefix_track_num()

    print('\nFinished!')
    input('Press any key to close this window...')
