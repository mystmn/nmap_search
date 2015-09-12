from collections import defaultdict

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print bcolors.WARNING + "Warning: No active frommets remain. Continue?" + bcolors.ENDC
print bcolors.OKGREEN + "Warning: No active frommets remain. Continue?" + bcolors.ENDC
print bcolors.OKBLUE + "Warning: No active frommets remain. Continue?" + bcolors.ENDC
print bcolors.HEADER + "Warning: No active frommets remain. Continue?" + bcolors.ENDC

class a(object):
    def foo(self):
        y = 1
        g = 2
        if b().too():
            return y + g + s
        else:
            False

class b(object):
    def too(self):
        global s
        s = 3
        return True

class c(object):
    def boo(self, limit=20):
        f = open("csv", 'w')

        list = ["animals"], ["pug", "cats", "pigs"], ["cars"], ["ford", "jeep", "chev"], ["drinks"], ["coffee", "gat"]
        truple = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

        c = 0

        for section in list:
            n = len(section)
            print n
            f.writelines("\n")

            for animals in section[:n]:

                c += 1

                if c >= limit:
                    break

                else:
                    f.writelines(animals)
                    f.writelines(",")
                    print animals

        f.close()

    def who(self):
        listA = ["id", "name", "city", "state"]
        listB = ["1", "Paul", "Columbus", "ohio", "43232"]

        if not len(listA) == len(listB):
                print "List don't match"

        d = defaultdict(list)
        for x, y in zip(listA, listB):
            d[x].append(y)
        d = dict(d)

        return d

    def forEach(self,x="" ,y=""):
        for x in y.keys():
            print "the key name is '%s' and its value is %s" % (x, ', '.join(y[x]))

#d = c().who()
#c().forEach("", d)

#print a().foo()
#print c().boo()

def splittingList():
	s = []
	s.extend(['bob', 'george', 'sally'])
	return ','.join(s)

#print splittingList()

def appendList():
	y = []	
	x = []
	x = ['Please',['Sir','May','I','Have'], ['Another','Thing','Of','Soup', '?']]
	
	for eachC in x:
		y.extend(eachC)
	return y

print appendList()
