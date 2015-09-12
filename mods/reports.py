#!/usr/bin/env python
import sys, os
from mods import nmap, whiteList, container
from whiteList import filter

class informationDrainage(object):
    def __init__(self):
        self.information_box_rules = {
            'octave': False,
            'sk': False,  # True = Found / False = Lost
            'dn': False,  # dn = domain name
            'dN': False,  # dN = Device Name
            'iA': "open",  # iA = IP Address
            'er': ' ',  # sError Message
        }

    def searchFilePerLine(self, list_Reports_to_Search, diretory_path_to_save):

        if isinstance(list_Reports_to_Search, list):

            for individual_report in list_Reports_to_Search:

                path_per_report = diretory_path_to_save + "/" + individual_report

                list_all_file_content = file_mutation().reading(path_per_report, 2, -1)

                if list_all_file_content:
                    bigger_box = []
                    octave_number = 0

                    for each_line in list_all_file_content:
                        octave_number += 1

                        bigger_box.append(filter(self.information_box_rules).universalFilter(each_line, octave_number))

                    msg = file_mutation().writing(bigger_box, diretory_path_to_save, individual_report)
                    return [msg, bigger_box, diretory_path_to_save, individual_report]

        else:
            print "Nmapp only returned one report - no function written for such a task"


class file_mutation(object):
    def reading(self, fileName, x=None, y=None):

        try:
            with open(fileName, 'r') as f:
                eachLine = f.readlines()[x:y]
                return eachLine

        except:
            return False

    def writing(self, list_package_ready_for_delivery, package_directory, report_name):

        new_housing_development = container.build(package_directory, report_name)

        development_results = new_housing_development.foundation()

        if development_results:
            headers = ['domain', 'device name', 'something', 'octave', 'ip', 'error message']
            f = open(development_results, 'w')
            f.write(',\t'.join(headers) + '\n')

            for unpacked_from_list in list_package_ready_for_delivery:
                f.write(', '.join(str(value) for key, value in unpacked_from_list.items()))
                f.write("\n")

            f.close()
            return True
        else:
            print "Problem : reports.py line 72"
            return False
        """
        ###################################################################
                                    Old Section
        ###################################################################
        """