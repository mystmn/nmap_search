import os, subprocess, shlex, rule


class folderValidation(object):
    def __init__(self, called_directory):
        self.dir = called_directory

    def convertUserInput(self, user_input):

        set_path = self.dir + "/" + user_input.replace(".", "_") + "/" + rule.DT_stamp(1)

        if not os.path.exists(set_path):

            os.makedirs(set_path)

            return set_path

        else:
            rule.pause("Error creating directory...make sure it has write permissions :: %s" % set_path)


class userInput(object):
    def __init__(self):
        self.back_door_segment = False

    def menuValidationList(self):

        menuList = [
            # Default
            {
                "keycode": 1,
                "title": "Segment Scan list",
                "inputQuestion": "What's the segment?",
                "scanOutput": "segment",
                "limitation": "default",
                "expected_type": ["yes", "no"]
            },
            {
                "keycode": 2,
                "title": "Stealth Segment Scan",
                "inputQuestion": "What's the stealth single IP?",
                "scanOutput": "stealth",
                "limitation": "default",
                "expected_type": 3
            },
            # Automation
            {
                "keycode": 1,
                "title": "File OS Discovery",
                "inputQuestion": "What's the path?",
                "scanOutput": "single",
                "limitation": "automation",
                "expected_type": "file_path"
            },
            # Optional
            {
                "keycode": 1,
                "title": "OS Discovery Scan",
                "inputQuestion": "Shall we search the OS Finger print?",
                "scanOutput": "osDis",
                "limitation": "optional",
                "expected_type": ["yes", "no"]
            },
            {
                "keycode": 2,
                "title": "Save Scan Results",
                "inputQuestion": "Continue?",
                "scanOutput": "saveResults",
                "limitation": "optional",
                "expected_type": "file_path"
            }
        ]
        return menuList

    def displayQuestion(self, key, needle):
        a = []
        i = 0
        for display in self.menuValidationList():

            if str(display[key]) == needle:
                i += 1
                print "%s) %s" % (i, display['title'])
                a.append(display)

        return a

    def back_door(self, list_commands):

        if type(list_commands) is list and len(list_commands) == 5 and list_commands[0] is "*":
            return True
        else:
            return False

    def second_pass_menu(self, list_commands):

        if type(list_commands) is list and len(list_commands) == 2 and list_commands[0] is not "*":
            return True
        else:
            return False

    def hub(self, set_menu_choice=None):

        # Needing to set a menu choice
        if self.second_pass_menu(set_menu_choice):
            x, y = set_menu_choice
            dict_selection = self.displayQuestion(x, y)
            user_input = raw_input("Answer > ")

        elif self.back_door(set_menu_choice):
            # set_menu_choice[activate_back_door, menu_key, menu_value, auto_ip_address, over_ride_second_question]
            dict_selection = self.displayQuestion(set_menu_choice[1], set_menu_choice[2])
            self.back_door_segment = set_menu_choice[3]
            user_input = str(set_menu_choice[4])

        else:
            dict_selection = self.displayQuestion("limitation", "default")
            user_input = raw_input("Answer > ")

        return self.packageReturn(self.join_answer_and_menu_prefix(dict_selection, user_input))

    def join_answer_and_menu_prefix(self, x, y):

        for g in x:

            if y == str(g['keycode']):
                n = g

                if not self.back_door_segment:
                    n['userInput'] = raw_input("\n" + g['inputQuestion'] + "> ")
                else:
                    n['userInput'] = self.back_door_segment

        n['segmentPath'] = folderValidation("tmpTest").convertUserInput(n['userInput'])

        '''
            Need to add a validation to the type of answer that was given.
            1) numerical
            2) yes or no
            3) file or folder path
            
        '''
        if self.validation(n['expected_type'], n['userInput']):
            rule.pause("Validation passed")
            # if self.validateAllNumbers(n['scanOutput'], n['userInput']):
            #
            # We need to simplify the returned list...not everything is needed
            output_filter = ['scanOutput', 'userInput', 'keycode', 'segmentPath']

            return rule.funnel_white_list(output_filter, self.return_first_key_in_List(n))

        else:
            rule.pause("Validation failed")
            #            return self.hub(["limitation", "default", 1])

    def validation(self, key, user):

        # Let's filter the ranges if input is numerical or int. This should only look inside IP Addresses
        if str(key).replace('.', '', 1).isdigit():
            arry = user.split('.')
            count_user = len(arry)

            for octave in arry:

                if user[-1] == "." or count_user > key:
                    print "Too many periods, please remove '%s'. Should look like '%s'" % (user, (".").join(filter(None, arry)))
                    return False
                elif int(octave) >= 256:
                    print type(octave)
                    print "Highest value allowed is 255, not %s" % octave
                    return False
                elif int(octave) < 0:
                    print "Lowest value allowed is 0, not %s" % octave
                    return False
            return True

        ''' Multiple choice '''
        if isinstance(key, list):
            for answer in key:
                print (answer, user)
                if answer == user.lower():
                    print "We did it!!"
                    return True
            return False

    def packageReturn(self, value):
        print "controller :: %s" % value
        return value

    def return_first_key_in_List(self, container):

        if isinstance(container, list) and len(container) >= 1:
            return container[0]
        else:
            return container

    def validateAllNumbers(self, code, user_input_answer):
        msg = "...Try again.\n"

        char_input = len(user_input_answer)

        if code == "segment":
            if char_input == 3 and user_input_answer[-1].isdigit():
                return True
            elif char_input > 3:
                print "More than 3 octaves were found in your answer" + msg
                return False
            else:
                print "Less than 3 octaves were found in your answer" + msg
                return False

        elif code == "single" or code == "stealth":

            if char_input == 4 and user_input_answer[-1].isdigit():
                return True
            elif char_input > 4:
                print "More than 4 octaves were found in your answer" + msg
                return False
            else:
                print "Less than 4 octaves were found in your answer" + msg
                return False

        elif code == "osDis":
            print "test :: %s " % user_input_answer.lower()
            if user_input_answer.lower() == "yes":
                return True
            else:
                print "Yes or No, not case sensitive"
                return False

        else:
            return False

    """
    ###################################################################
                                Old Section
    ###################################################################
    """
