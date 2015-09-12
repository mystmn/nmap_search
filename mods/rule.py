import sys

sys.dont_write_bytecode = True  # Don't write a .pyc file

def DT_stamp(x=None):
    import datetime
    now = datetime.datetime.now()

    if x == 1:
        return now.strftime("%Y%m%d_%H%M")
    elif x == 2:
        return now.strftime(":Y:m:d_H:M:S")
    else:
        return None


def clear():
    import subprocess
    subprocess.call("clear")


def pause(message=''):
    print "Script was stopped upon request :: %s" % message
    raise SystemExit(0)


def funnel_white_list(white_list, called_dict):
    a_list = []

    if type(white_list) is list and type(called_dict) is dict:

        for value in white_list:

            for key in called_dict.keys():

                if value is key:
                    a_list.append(called_dict[key])
        return a_list

    else:
        print "Make sure input dict and list are appropriate \n List: %s \n Dict: %s" % (white_list, called_dict)
        pause()
