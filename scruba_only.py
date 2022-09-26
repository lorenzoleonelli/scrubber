import scrubadub
import scrubadub_spacy

import re

# prova classe variabile ################################
class_type="TargaAutoIT"
class_name="TargaAutoIT_class"
detect_class_name ="TargaAutoIT_detect"
regexp1="[A-Za-z]{2}[0-9]{3}[A-Za-z]{2}"

class_name = __import__("scrubadub.filth")
class class_name(scrubadub.filth.Filth):
    type = class_type

class detect_class_name(scrubadub.detectors.RegexDetector):
    name = 'red'
    regex = re.compile(regexp1, re.IGNORECASE)
    filth_cls = class_name
# fine prova classe variabile ################################

class BibFilth(scrubadub.filth.Filth):
    type = 'BiBaBu'

class BlueFilth(scrubadub.filth.Filth):
    type = '-Blue-'

#print(getattr(BibFilth, 'type'))

class BlueDetector(scrubadub.detectors.RegexDetector):
    name = 'bluetti'
    regex = re.compile("blue", re.IGNORECASE)
    filth_cls = BlueFilth

class OrangeDetector(scrubadub.detectors.RegexDetector):
    name = 'orange'
    regex = re.compile("b[aeiou]bble", re.IGNORECASE)
    filth_cls = BibFilth

scrubber = scrubadub.Scrubber(locale='it_IT')
#scrubber.add_detector(scrubadub_spacy.detectors.SpacyEntityDetector(model='en_core_web_trf'))
scrubber.add_detector(scrubadub_spacy.detectors.SpacyEntityDetector(model='it_core_news_lg'))

#scrubber = scrubadub.Scrubber(locale='it_IT')
#scrubber.add_detector(scrubadub_spacy.detectors.SpacyEntityDetector(model='it_core_news_lg'))
#scrubber.add_detector(scrubadub.detectors.DateOfBirthDetector)
#scrubber.add_detector(OrangeDetector)
#scrubber.add_detector(BlueDetector)
#scrubber.add_detector(detect_class_name)


# Other detectors


text = "Buongiorno. Mi chiamo Mario Rossi e lavoro per Acme SpA, i miei recapiti telefonico sono 0471 657790 e 340.22567890, rispondo agli indirizzi mario.rossi@yahoo.com e anche a m.rossi@acme.it. \
        Uso la CC n. 3716820019271998 e acquisto spesso su www.amazon.com ma a volte anche su zalando.com \
        sono nato il 14 settembre 1996 ed abito a Roma in via Industria, 54 \
        Guido una VW Polo targata FD456TT. Usando la patente n. U1H68I903B \
        Grazie e cari saluti. \
        -----------------------------------------------------\
        Good morning. My name is John Smith and I work for Acme SpA, my telephone numbers are 408 677 8989 and +16102347346 , I reply to the addresses john.smith@yahoo.com and also to j.smith@acme.it. \
        I use the CC n. 3716820019271998 and I often buy on www.amazon.com but sometimes also on zalando.com \
        I was born on 14 September 1996 and I live in 65 2nd Avenue, New York \
        I drive a Chrisler Crossfire with license plate is 12-345S, my driver license number is G544-061-73-925-0.\
        Thanks and best regards. \
        "
print(scrubber.clean(text))