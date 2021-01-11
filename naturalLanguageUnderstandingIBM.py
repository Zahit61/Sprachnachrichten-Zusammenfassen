import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, KeywordsOptions

authenticator = IAMAuthenticator('G-RxlYL0lc0PulJ6mEg8Mm93av5Lf5z5asTa_7BWQU5j')
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2020-08-01',
    authenticator=authenticator
)

natural_language_understanding.set_service_url('https://api.eu-de.natural-language-understanding.watson.cloud.ibm.com/instances/38dd91af-7d70-4a5c-bb9b-f3f90c395bde')

response = natural_language_understanding.analyze(
    text= 'Am Vorabend zum ersten Advent präsentierte Florian Silbereisen die fast dreieinhalbstündige Show zum Start in die Weihnachtszeit. Der Showmaster zündete gemeinsam mit vielen Stars die ersten Kerzen an und stimmte die Zuschauerinnen und Zuschauer mit den schönsten Advents- und Weihnachtsliedern auf die besinnlichste Zeit des Jahres ein. Feierlicher Höhepunkt der Eurovisionsshow war das Eintreffen des Friedenslichts aus der Geburtsgrotte in Bethlehem, das wieder an den tiefen Sinn von Weihnachten erinnern soll. Florian Silbereisen präsentierte zahlreiche prominente Gäste wie Andreas Gabalier, Andrea Berg, Ute Freudenberg, Ross Antony, Howard Carpendale, Uschi Glas, David Garrett, Feuerherz, Patricia Kelly, Joey Kelly, Angelo Kelly & Family, Andy Borg, Beatrice Egli, Ramon Roselly, das Nürnberger Christkind und viele weitere.',
    features=Features(keywords=KeywordsOptions(sentiment=True,emotion=True,limit=15))).get_result()

print(json.dumps(response, indent=2))