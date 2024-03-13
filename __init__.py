# coding: utf-8
"""
Base for development of external modules.
To get the module / function being called:
    GetParams('module')

To obtain the variables sent from form / Rocketbot command:
    var = GetParams(variable)

The "variable" is defined in forms of the package.json file

To modify the Rocketbot variable:
    SetVar(Rocketbot_Variable, "data")

To obtain a variable from Rocketbot:
    var = GetVar(Rocketbot_Variable)

To obtain the selected option:
    opcion = GetParams("option")


To install libraries you must enter the "libs" folder in the terminal
    
   sudo pip install <package> -t .

"""
import platform

if platform.system() != "Linux":
    raise Exception("This module only works in Linux")

GetParams = GetParams # type: ignore
SetVar = SetVar # type: ignore
PrintException = PrintException # type: ignore

def unlock_screen():
    import dbus
    sessionBus = dbus.SessionBus()
    screenSaver = sessionBus.get_object("org.gnome.ScreenSaver", "/org/gnome/ScreenSaver")
    screenSaverIface = dbus.Interface(screenSaver, 'org.gnome.ScreenSaver')
    screenSaverSetActive = screenSaverIface.get_dbus_method("SetActive")
    screenSaverSetActive(False)

module = GetParams('module')


if module == "unlock_screen":
    result = GetParams('result')

    try:
        unlock_screen()
        SetVar(result, True)
    except Exception as e:
        SetVar(result, False)
        PrintException()
        raise e