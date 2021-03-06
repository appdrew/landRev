# IMPORT THE YANDEX TRANSLATE API ENGINE TO OUR PYTHON APP SCRIPT 
from yandex.Translater import Translater

# APP SET NAME AND VERSION | INSERT YOUR APP DETAILS, SUCH AS NAME AND VERSION

print('Welcome to landRev | appDrew Development')

# APP INITIALIZE THE YANDEX ENGINE TRANSLATOR
tr = Translater()

# APP INITIALIZE THHE API KEY FOR YANDEX ENGINE TRANSLATOR | INSERT YOUR API KEY BELLOW PLEASE.
tr.set_key('YOUR YANDEX API KEY HERE')

# APP SET THE MAIN LANGUAGE | INSERT YOUR MAIN LANGUAGE "FROM WHAT LANGUAGE TO TRANSLATE"
tr.set_from_lang('en')

# APP SET the TRANSLATION LANGUAGE | INSERT YOUR TRANSLATION LANGUAGE WITH LANG CODE
tr.set_to_lang('es')

INPUT_TEXT_DATA = input('What do you would like to translate ? : ')

#SET THE INPUT_TEXT_DATA FOR TANSLATOR ENGINE TO TRANSLATE THE STRINGS 
tr.set_text(INPUT_TEXT_DATA)

#PRINT OUT THE TRANSLATED DATA RESULTS 
results = tr.translate()
print(results)
