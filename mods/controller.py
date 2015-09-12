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
    def menuValidationList(self):

        menuList = [
            # Default
            {
                "keycode": 1,
                "title": "Segment Scan list",
                "inputQuestion": "What's the segment?",
                "scanOutput": "segment",
                "limitation": "default"
            },
            {
                "keycode": 2,
                "title": "Stealth Segment Scan",
                "inputQuestion": "What's the stealth single IP?",
                "scanOutput": "stealth",
                "limitation": "default"
            },
            # Automation
            {
                "keycode": 1,
                "title": "File OS Discovery",
                "inputQuestion": "What's the path?",
                "scanOutput": "single",
                "limitation": "automation"
            },
            # Optional
            {
                "keycode": 1,
                "title": "OS Discovery Scan",
                "inputQuestion": "Shall we search the OS Finger print?",
                "scanOutput": "osDis",
                "limitation": "optional"
            },
            {
                "keycode": 2,
                "title": "Save Scan Results",
                "inputQuestion": "Continue?",
                "scanOutput": "saveResults",
                "limitation": "optional"
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

    def backDoor(self, admin, list_commands):

        if admin is not False and type(list_commands) is list:


    def hub(self, set_menu_choice=None):

        if isinstance(set_menu_choice, list):
            x, y = set_menu_choice
            dict_selection = self.displayQuestion(x, y)

        elif self.backDoor():
            print ''

        else:
            dict_selection = self.displayQuestion("limitation", "default")

        user_input = raw_input("Answer > ")

        return self.packageReturn(self.join_answer_and_menu_prefix(dict_selection, user_input))

    def join_answer_and_menu_prefix(self, x, y):

        for g in x:

            if y == str(g['keycode']):
                n = g
                n['userInput'] = raw_input("\n" + g['inputQuestion'] + "> ")

        n['segmentPath'] = folderValidation("tmpTest").convertUserInput(n['userInput'])

        if self.validateAllNumbers(n['scanOutput'], n['userInput'].split('.')):
            # We need to simplify the returned list...not everything is needed
            filter = ['scanOutput', 'userInput', 'keycode', 'segmentPath']

            return rule.funnel_white_list(filter, self.return_first_key_in_List(n))
        else:
            return self.hub(["limitation", "default", 1])

    def packageReturn(self, value):
        print "done...return[controller]"
        return value

    def return_first_key_in_List(self, container):

        if isinstance(container, list) and len(container) >= 1:
            return container[0]
        else:
            return container

    def validateAllNumbers(self, code, nmb):
        msg = "...Try again.\n"

        if not nmb[-1].isdigit():
            print "Last character isn't a number, possibly a period" + msg
            return False
        nmb = len(nmb)

        if code == "segment":
            if nmb == 3:
                return True
            elif nmb > 3:
                print "More than 3 octaves were found in your answer" + msg
                return False
            else:
                print "Less than 3 octaves were found in your answer" + msg
                return False

        elif code == "single" or code == "stealth":
            if nmb == 4:
                return True
            elif nmb > 4:
                print "More than 4 octaves were found in your answer" + msg
                return False
            else:
                print "Less than 4 octaves were found in your answer" + msg
                return False
        else:
            return False

        """
        ###################################################################
                                    Old Section
        ###################################################################
        """
