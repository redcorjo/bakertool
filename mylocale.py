import gettext
import locale
import os

_ = lambda s: s

def mylocale():
    """
    Disable in the original gui module the below changes:

        #import gettext
        #_ = gettext.lgettext

    Include in the original main module the below changes:
        import mylocale
        mylocale.mylocale()

    """
    import gettext

    try:
        mylanguage = "%s" % locale.getdefaultlocale()[0][0:2]
        #mylanguage = "en"
    except:
        mylanguage = "en"

    try:
        mylocale = gettext.translation('bakertool', localedir='locale', languages=[mylanguage])
        mylocale.install()
    except:
        mylocale = gettext.translation('bakertool', localedir='locale', languages=["en"])
        mylocale.install()