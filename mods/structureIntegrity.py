import sys, os, subprocess, shlex
from mods import rule


class segmentScript(object):
    def __init__(self, folderName):
        self.code = ""
        self.folder = folderName
        self.menuChoices = ["segment", "single", "stealth"]

    def menu(self):
        print "%s) Segment Scan list" % "1"
        print "%s) OS Indivudal Scan" % "2"
        print "%s) Stealth Segment Scan" % "3"

        menu = str(raw_input("Option > "))

        if menu == "1":
            self.code = "segment"
            return self.segTargetScan()

        elif menu == "2":
            self.code = "single"
            return self.singleTargetScan()

        elif menu == "3":
            self.code = "stealth"
            return self.stealthSingleScan()

        elif menu == "4":
            self.code = ""
            return (False, "null", False)

        else:
            self.clear()
            print "%s is an invalid choice...try again\n" % menu
            self.menu()

    def segTargetScan(self):
        self.input = ""

        self.systemNetworkInfo()
        # Asking user what segment to scan?
        if self.input == "":
            self.input = raw_input("\nWhat's the segment? > ")

        # self.input = "172.31.98"

        if self.validateAllNumbers("segment"):

            return self.dirExist(self.input)

        else:
            return self.segTargetScan()

    def singleTargetScan(self):
        self.input = ""
        self.systemNetworkInfo()

        if self.input == "":
            self.input = raw_input("\nWhat's the single IP? > ")
        else:
            print ""

        if self.validateAllNumbers("single"):

            four = self.input.rfind(".")  # find 4th octets 162.37.69.xxx

            loc = self.input[:four]

            return self.dirExist(loc)

        else:
            return self.singleTargetScan()

    def stealthSingleScan(self):
        self.input = ""
        self.systemNetworkInfo()

        if self.input == "":
            self.input = raw_input("\nWhat's the stealth single IP? > ")
        else:
            print ""

        if self.validateAllNumbers("single"):

            four = self.input.rfind(".")  # find 4th octets 162.37.69.xxx

            loc = self.input[:four]

            return self.dirExist(loc)

        else:
            return self.singleTargetScan()

    def dirExist(self, loc):
        a = []
        # Replace periods with underscores
        # Example 162.37.59 with 162_37_59
        input_replace = loc.replace(".", "_")

        # tmp/Segment/Date_time
        combinePath = self.folder + "/" + input_replace + "/" + rule.DT_stamp()

        if not os.path.exists(combinePath):
            os.makedirs(combinePath)
            print "Made directory %s" % combinePath

        else:
            print "Following folder already exist: '%s'" % combinePath

        a.append(combinePath)
        a.append(self.input)
        a.append(self.code)
        return a

    def validateAllNumbers(self, code):
        rule.clear()
        nmb = self.input.split('.', )
        msg = "...Try again.\n"

        if not nmb[-1].isdigit():
            print "Last character isn't a number" + msg
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

        elif code == "single":
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

    def systemNetworkInfo(self):
        strs = subprocess.check_output(shlex.split('ip r l'))
        gateway = strs.split('default via')[-1].split()[0]
        ip = strs.split('src')[-1].split()[0]

        cosmetic = "*" * 44
        print "/" + cosmetic + "/"
        print "/* Gateway %s | IP %s */" % (gateway, ip)
        print "/" + cosmetic + "/"
