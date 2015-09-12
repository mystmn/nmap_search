class filter(object):
    def __init__(self, information_box_rules):
        self.information_box_rules = information_box_rules

    def phrase(self, line):

        if line[:20] == "Nmap scan report for" and not line[22].isdigit():
            return True

        else:
            return False

    def universalFilter(self, readLine, lineNumber):

        if not self.phrase(readLine):
            shipping_package_results = self.repackage({'er': "Device found - unknown", 'octave': lineNumber})

        else:
            findLastSpace = readLine.rfind(" ")

            # remove space and parentheses from the beginning and end
            ip = readLine[findLastSpace + 2:-2]

            # If the period is not after the last space, there's no ip listed.
            marker = readLine.find(".")

            if not marker >= findLastSpace:
                shipping_package_results = self.repackage(
                    {'sk': True, 'dn': readLine[marker + 1:findLastSpace], 'dN': readLine[21:marker], 'iA': ip,
                     'octave': lineNumber})

            else:
                shipping_package_results = self.repackage({'er': "Needs researched", 'octave': lineNumber})

        return shipping_package_results

    def repackage(self, reflect_information_box_rules):

        harmony = self.information_box_rules.copy()
        harmony.update(reflect_information_box_rules)
        return harmony

        """
        ###################################################################
                                    Old Section
        ###################################################################
        """

        def searchingLine(self):

            setID = 0

            for line in self.file:
                setID += 1

                self.gatherDeviceInfo(str(setID), line)

            return [self.a, self.b]

        def gatherDeviceInfo(self, id, line):
            test = []

            # Looks for computer name xxxxxx not 000.000.000.000
            if self.ifDigit(line[21]) and line[0:20] == self.phrase:

                # Goes to the last space between Name.Domain and IP
                findLastSpace = line.rfind(" ")
                ip = line[findLastSpace + 2:-2]

                marker = line.find(".")

                if not marker >= findLastSpace:
                    self.domain = line[marker + 1:findLastSpace]
                    self.device = line[21:marker]
                    self.ip = ip
                    self.a.append([id, self.device, self.domain, self.ip])

            else:
                self.b.append([id, "open", "open", line[21:-1]])

        def ports(self):
            a = []
            noneRepeat = 1
            var = False

            if not self.file:
                print "sent as a false file"
                a.append("null")

            else:
                for line in self.file:

                    if line.startswith('21/tcp'):
                        a.append(str(21))
                        var = True

                    if line.startswith('22/tcp'):
                        a.append(str(21))
                        var = True

                    if line.startswith('23/tcp'):
                        a.append(str(23))
                        var = True

                    if line.startswith('80/tcp'):
                        a.append(str(80))
                        var = True

                    if line.startswith('135/tcp'):  # Microsoft Windows RPC
                        a.append(str(135))
                        var = True

                    if line.startswith('139/tcp'):
                        a.append(str(139))
                        var = True

                    if line.startswith('443/tcp'):  # used by Skype
                        a.append(str(443))
                        var = True

                    if line.startswith('445/tcp'):
                        a.append(str(445))
                        var = True

                    if line.startswith('49155/tcp'):  # Microsoft Windows RPC
                        a.append(str(49155))
                        var = True

                    if line.startswith('62078/tcp'):
                        a.append(str(62078))
                        var = True

                    if line.startswith('| http-title:'):
                        if noneRepeat == 1:
                            var = True
                            lastSpace = line.rfind(":")
                            deviceTitle = line[lastSpace + 2: -1]
                            a.append(deviceTitle)
                            noneRepeat += 1

                    phrase = '|   OS:'
                    if line.startswith(phrase):
                        var = True
                        a.append(self.osDiscovery(line, phrase))

                    phrase = 'OS CPE:'
                    if line.startswith(phrase):
                        var = True
                        a.append(self.osDiscovery(line, phrase))

                    if line.startswith('MAC Address:'):
                        var = True
                        a.append(self.ping(line))

                # File exist, no ports were found. Return False
                if not var:
                    a.append("no info")

            return a

        def ifDigit(self, digit):

            if not digit[0].isdigit():
                return True
            else:
                return False

        def osDiscovery(self, line, filter):
            desc = " "

            endSrc = line.find(filter)  # Goes to the last space between Name.Domain and IP
            desc = line[endSrc + 1:-2]  # IP Address

            return desc

        def ping(self, line):
            mac = " "
            mac = line[13:31]
            '''
            endSrc = line.find("(")  # Goes to the last space between Name.Domain and IP

            deviceType = line[endSrc + 1:-2]  # IP Address

            if endSrc:
                mac = line[13:31]
                #a.append(deviceType)
                a.append(mac)
            '''
            return mac
