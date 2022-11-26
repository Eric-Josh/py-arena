from datetime import datetime, date

user_data = []

while True:
    print('Please Enter 1 for Sign up:')
    print('Please Enter 2 for Sign in:')
    print('Please Enter 3 for Quit:')
    print('='*25)

    selected_opt = input('Choose an option: ')

    # Validate input
    opts = ('1','2','3')
    while True:
        if selected_opt in opts:
            break
        else:
            print('Invalid option, please try again!')
            selected_opt = input('Choose an option: ')


    if selected_opt == '1':
        err_msg1 = 'You have entered an invalid input'
        err_msg2 = 'Please try again'

        while True:
            name = input('Enter Full Name: ')
            # Validate
            if len(name) < 3:
                print('='*25)
                print(err_msg1)
                print(err_msg2)
            else:
                break;

        while True:
            phone = input('Enter Contact Number: ')
            # Validate
            if phone.isnumeric() == False or len(phone) != 10 or phone[0] != '0':
                print('='*25)
                print(err_msg1)
                print(err_msg2)
            else:
                break;

        while True:
            password = input('Enter Password: ')
            password_confirm = input('Enter Password Confirmation: ')
            # Validate
            pass_len = len(password)
            if pass_len > 0 and password == password_confirm\
                and password[0].isalpha() and password[pass_len -1].isnumeric()\
                and '@' in password or '&' in password:
                break
            else:
                print('='*25)
                print(err_msg1)
                print(err_msg2);

        while True:
            format = "%d/%m/%Y"
            dob = input('Enter Date of Birth # DD/MM/YYYY (No Space): ')
            if len(dob) <= 0:
                print('='*25)
                print(err_msg1)
                print(err_msg2)
            else:
                try:
                    bool(datetime.strptime(dob, format))
                    if (date.today().year - int(dob.split('/')[2])) < 21:
                        print('='*25)
                        print(err_msg1)
                        print(err_msg2)
                    else:
                        break;
                except ValueError:
                    print('='*25)
                    print(err_msg1)
                    print(err_msg2)

        # Save user details to user_data list
        user_data.append({'name': name, 'phone': phone, 'dob': dob, 'password': password})

        print('='*25)
        print('You have Successfully Signed up.')

    elif selected_opt == '2':
        login_attempts = 0
        loggedin_user = {}
        not_exist = False

        while True:
            username = input('Please enter your username (Mobile Number): ')
            password = input('Please enter your password: ')

            # Validate user
            if username !='' and password !='':
                for u in user_data:
                    if username == u['phone'] and password == u['password']:
                        print('Worker1')
                        loggedin_user = u

                if len(loggedin_user) == 0:
                    attempts = 0
                    for u in user_data:
                        if username == u['phone'] and password != u['password']:
                            login_attempts += 1
                            attempts = 1
                            print('='*25)
                            print('You have entered a wrong password.')
                            print('Please try again')
                
                    if attempts == 0:
                        for u in user_data:
                            if username != u['phone']:
                                not_exist = True
                    
            if loggedin_user or login_attempts >= 3 or not_exist or len(user_data) == 0:
                break

        if loggedin_user:
            print('='*25)
            print('You have successfully signed in')
            print('Welcome '+ loggedin_user['name'])

            while True:
                print('Please enter 1 for Resetting the Password:')
                print('Please Enter 2 for Signout:')
                print('='*25)

                opt = input('Choose an option: ')
                opts = ('1','2')
                while True:
                    if opt in opts:
                        if opt == '1':
                            while True:
                                old_password = input('Please enter your old password: ')
                                new_password = input('Please enter your new password: ')

                                # validate
                                pass_len = len(new_password)
                                if old_password == loggedin_user['password']\
                                    and new_password[0].isalpha() and new_password[pass_len -1].isnumeric()\
                                    and '@' in new_password or '&' in new_password:

                                    # update loggedin user dict and user_data list
                                    loggedin_user['password'] = new_password
                                    for u in user_data:
                                        if loggedin_user['phone'] == u['phone']:
                                            u['password'] = new_password
                                    break
                                else:
                                    print('='*25)
                                    print('Password did not match. please try again')

                            print('='*25)
                            print('You password has been reset succefully.')
                            break
                        else:
                            loggedin_user = {}
                            print('='*25)
                            print('You have signed out')
                            break
                    else:
                        print('Invalid option, please try again!')
                        opt = input('Choose an option: ')
                
                if opt == '2':
                    break
        elif login_attempts >= 3:
            print('='*25)
            print('You have used the maximum attempts of Login:')
            print('Please reset your password by entering the below details:')

            user_for_reset = {}
            while True:
                username = input('Please enter your username (Mobile Number) to confirm: ')
                dob = input('Please enter your Date of Birth in DD/MM/YYYY format, to confirm: ')

                # Validate
                for u in user_data:
                    if username == u['phone'] and dob == u['dob']:
                        user_for_reset = u
                        break

                if user_for_reset:
                    break
                else:
                    print('='*25)
                    print('Input does not match existing record(s)')

            while True:
                new_password = input('Please enter your new password: ')   
                confirm_password = input('Please re-enter your new password: ')

                pass_len = len(new_password)
                if pass_len > 0 and new_password == confirm_password\
                    and new_password[0].isalpha() and new_password[pass_len -1].isnumeric()\
                    and '@' in new_password or '&' in new_password:
                    # update user new password to user_data list
                    for u in user_data:
                        if user_for_reset['phone'] == u['phone']:
                            u['password'] = new_password
                    print('='*25)
                    print('Your password has been reset successfully.')
                    break;
                else:
                    print('='*25)
                    print('Invalid Password')
                    print('Please try again')
        else:
            print('='*25)
            print('You have not signed up with this contact number. please sign up first.')

    else:
        print('='*25)
        print('Thank You for using the Application.')
        break
