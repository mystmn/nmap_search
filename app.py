import sys

sys.dont_write_bytecode = True  # Don't write a .pyc file

from mods import structureIntegrity as SI
from mods import controller, nmap, reports

tmpDir = "tmp"
tmp_alpha = "tmp/162_37_69/20150715_0743"


# test_a = "single"

# Ask user to select an option, scan that option, and create a location for results

# default path  = 'tmp/[year][month][day]_[time]/segment'
class main():
    def alphaStart(self, list=None):
        #
        # if "*" is [0] then start the automation process other wise, ask the user what menu selection he/she wants
        list_of_four = controller.userInput().hub([" ", "scanOutput", "segment", "162.37.69", "1"])

        # returns a lsit of three: ['type_of_scan', 'user_input_ip_address_or_segment', key, and folder_path']
        report, path = nmap.terminal_central().hub(list_of_four)

        os_discovery_needed = reports.informationDrainage().searchFilePerLine(report, path)

        if os_discovery_needed[0]:
            second_pass_list_of_four = controller.userInput().hub(["limitation", "optional"])
            report, path = nmap.terminal_central().hub(second_pass_list_of_four)


main().alphaStart()

'''
userInput = SI.segmentScript(tmpDir)
'''

# Menu provided for nmap scan details
'''
pathSent = userInput.menu()
'''

# raise SystemExit(0)
# fact.createFiles(tmp_alpha, "162.37.69", "segment")
'''
fact.createFiles(pathSent[0], pathSent[1], pathSent[2])
'''
