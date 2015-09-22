import subprocess
from mods import rule

class terminal_central(object):
    
    def hub(self, splitList):
        closingReports = []

        code, userInput, key, feedPath = splitList
        print "Wait wait...running _ping"
        ''' Let's find feed back on pingable Devices '''
        closingReports.append(self.executingTerminal(self.foreRunner(userInput, feedPath)))

        closingReports.append(self.executingTerminal(self.splitTracks(key, userInput, feedPath)))

        return self.packageReturn([closingReports, feedPath])

    def executingTerminal(self, settings):

        if settings[0] is False:
            return settings[2]

        feedingCommands, echoResults, msg = settings

        if echoResults is False:
            try:
                subprocess.call(feedingCommands, stdout=subprocess.PIPE)
                return msg
            except:
                return [False, "Scan failed"]

        else:
            try:
                subprocess.call(feedingCommands)
                return msg
            except:
                return [False, "Scan failed"]

    def splitTracks(self, key, userInput, feedPath):

        ''' Hide's terminal Output '''

        if str(key) == "1":
            networkBinary = userInput + ".0/24"
            return [["nmap", "-sL", "-sn", networkBinary, "-oN", feedPath + "/_cacheReport"], False, "_cacheReport"]

        elif str(key) == "2":
            ''' --script smb-os-discovery.nse -p445 (checks for Windows OS), -oN (save file) '''
            print "Wait...running _osDiscovery"
            return [
                ["sudo", "nmap", "--script", "smb-os-discovery.nse", "-p445", userInput, "-oN", feedPath + "segment"],
                False, "_osDiscovery"]

        elif str(key) == "3":
            ''' --script smb-os-discovery.nse -p445 (checks for Windows OS), -oN (save file) '''
            print "Wait...running _stealth SearchFound"
            return [["sudo", "nmap", "-V", "-sS", "-P0", "-p445", userInput, "-oN", feedPath + "stealth"], False,
                    "_stealth"]
        else:
            return [[False], False, "Backend validation found an error"]

    def packageReturn(self, fileLocation):
        return fileLocation

    def foreRunner(self, userInput, feedPath):
        networkBinary = userInput + ".0/24"
        return [["nmap", "-sP", networkBinary, "-oN", feedPath + "/" + "_pingable"], False, "_pingable"]

        """
        ###################################################################
                                    Old Section
        ###################################################################
        """


class nmapScript(object):
    def __init__(self, savePath, segment, code):
        self.octavePath = savePath
        self.octavePath01 = savePath + "/" + segment

        self.binary = segment + ".0/24"
        self.segment = segment
        self.code = code
        self.cmd()

    def cmd(self):
        a = []
        if self.code == "segment":

            try:
                ''' -sl (simple list), -sn (disable port scan), -oN (save file) '''
                subprocess.call(["sudo", "nmap", "-sL", "-sn", self.binary, "-oN", self.octavePath])
                subprocess.call(["nmap", "-sP", self.binary, "-oN", self.octavePath + "_pingable"])
                return True
            except:
                return False

        elif self.code == "single":
            try:
                ''' --script smb-os-discovery.nse -p445 (checks for Windows OS), -oN (save file) '''
                subprocess.call(["sudo", "nmap", "--script", "smb-os-discovery.nse", "-p445", self.segment, "-oN",
                                 self.octavePath01])
                return True
            except:
                return False

        elif self.code == "stealth":
            try:
                ''' --script smb-os-discovery.nse -p445 (checks for Windows OS), -oN (save file) '''
                subprocess.call(["sudo", "nmap", "-V", "-sS", "-P0", "-p445", self.segment, "-oN", self.octavePath01])
                return True
            except:
                return False

        elif self.code == "deep":
            try:
                ''' nmap -v -A -T4 162.37.69.2 -oN (save file) '''
                filePath = self.octavePath01 + "_deep"
                subprocess.call(["sudo", "nmap", "-v", "-A", "-T4", self.segment, "-oN", filePath])
                return True
            except:
                return False, False

        else:
            print "Please contact your local Shepard of rubber ducky's"
            rule.pause()
