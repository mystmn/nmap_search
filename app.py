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
        configured = controller.userInput().hub()
#        configured = controller.userInput().override(True, ["segment", "172.31.98"])
        report, path = nmap.terminalCentral().hub(configured)

        os_discovery_needed = reports.informationDrainage().searchFilePerLine(report, path)

        if os_discovery_needed[0]:
            controller.userInput().hub(["limitation", "optional"])

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
