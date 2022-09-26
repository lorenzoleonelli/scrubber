import streamlit as st
#from pandas import DataFrame

import scrubadub
import scrubadub_spacy

st.set_page_config(
    page_title="PII Scrubadub Parser",
#    page_icon="🎈",
)

# Populate the sidebar with my stuff
with st.sidebar:
    st.sidebar.image('logo_bk.png', width=200)
    st.markdown('https://www.theinfosecvault.com')
    
    st.markdown('')
    st.markdown('Get in touch at: info@theinfosecvault.com')
#   st.markdown('daje de potenza')
    st.markdown('')
    st.markdown('Python App deployed with scrubadub (https://scrubadub.readthedocs.io/en/stable/) and streamlite (https://streamlit.io/)')

def _max_width_():
    max_width_str = f"max-width: 1400px;"
    st.markdown(
        f"""
    <style>
    .reportview-container .main .block-container{{
        {max_width_str}
    }}
    </style>    
    """,
        unsafe_allow_html=True,
    )

_max_width_()
c30, c31, c32 = st.columns([2.5, 1, 3])
with c30:
    # st.image("logo.png", width=400)
    st.subheader("PII Scrubadub Parser v 0.1")
with st.expander("ℹ️ - About", expanded=False):
    st.write(
        """     
-   Aim of the App is to get in touch with the opensource package Python Scrubadub (https://scrubadub.readthedocs.io/en/stable/index.html). This python package could remove all personal data from an input text.
-   Here we'll move the fist steps, and have the chance to try the first line of code and test some detectors without any local installation.
	    """
    )
    st.markdown("")

#Prepare text area
with st.form(key="my_form"):
    options_loc = st.selectbox(
        'Please choose your localization',
        ('<no language>','it_IT', 'de_DE', 'en_UK', 'en_US'),
        help= "By setting a locale the Detectors that need configuring based on your region or language will know what type of text to expect. This means that a Detector that needs to know how Filth (such as a phone number) is formatted in your region will be able to look for Filth in that specific format. Find out more on: https://scrubadub.readthedocs.io/en/stable/localization.html")
    options_space = st.selectbox(
        'Please choose your spacy model',
        ('<Do Not Apply SpacyEntityDetector>','it_core_news_lg', 'de_core_news_sm', 'en_core_web_trf'),
        help="Scrubadub_spacy is an extension that uses spaCy NLP models to remove personal information from text. You can find out more about Spacy here: https://spacy.io/ ")
    options_cd = st.multiselect(
            'Please select your customized detectors:',
            ['ItalianPlate', 'ItalianCF', 'ExampleBadge'],
            help="Here you can choose a couple of customized detectors which I created based on regex. Personalized regex detectors can be easily created, for further info look here: https://scrubadub.readthedocs.io/en/stable/api_scrubadub_detectors.html " )
    doc = st.text_area( 
            "Paste your text here (max 500 words) or use the example already provided end just click the PARSE THE DATA button.",
            help="Usa questa area per fare le tue prove",
            height=310,
            
            value= "[ITA] Buongiorno. Mi chiamo Mario Rossi e lavoro per Acme SpA, i miei recapiti telefonici sono 0471 657790 e 340.22567890," + "\n"
            +"rispondo agli indirizzi mario.rossi@yahoo.com e anche a m.rossi@acme.it." + "\n"
            +"Uso la CC n. 371682001927199 e navigo spesso su www.theinfosecvault.com" + "\n"
            +"sono nato il 14 settembre 1996 ed abito a Roma in via Industria, 54." + "\n"
            +"Guido una VW Polo targata FD456TT. Usando la patente n. U1H68I903B. Il mio codice fiscale è: RSSMRA80A01H501U." + "\n"
            +"Porto sempre con me il mio badge aziendale con codice BADGE067." + "\n"
            +"Spero di avervi detto tutto. Grazie e cari saluti." + "\n\n"
        
            +"[ENG] Good morning. My name is John Smith and I work for Acme SpA, my telephone numbers are 408 677 8989 and +16102347346," + "\n"
            +"I reply to the addresses john.smith@yahoo.com and also to j.smith@acme.it." + "\n"
            +"I use the CC n. 371682001927199 and I often buy on www.theinfosecvault.com." + "\n"
            +"I was born on 14 September 1996 and I live in 65 2nd Avenue, New York." + "\n"
            +"I drive a Chrisler Crossfire with license plate is 12-345S, my driver license number is G544-061-73-925-0. My SSN is 721-88-9024." + "\n"
            +"I do always have with me my Company Badge ID BADGE067." + "\n"
            +"I hope I didn't forget anything. Thanks and best regards." + "\n"
        )

    MAX_WORDS = 500
    import re
    res = len(re.findall(r"\w+", doc))
    if res > MAX_WORDS:
        st.warning(
            "⚠️ Your text contains "
            + str(res)
            + " words."
            + " Only the first 500 words will be reviewed. Stay tuned as increased allowance is coming! 😊"
        )
        doc = doc[:MAX_WORDS]
    lines= doc.split("\n")

    submit_button = st.form_submit_button(label="✨ Scrub the data!")
    if submit_button:
        st.markdown("")
    if not submit_button:
        st.stop()
#st.write('You selected:', options)
code = "# always check what you cut and where you paste it ;-) #" + "\n"
code = code + "import scrubadub" + "\n"
code = code + "import scrubadub_spacy" + "\n" + "\n"
code = code + "scrubber = scrubadub.Scrubber()" + "\n"

scrubber = scrubadub.Scrubber()

if options_loc == 'it_IT':
    scrubber = scrubadub.Scrubber(locale='it_IT')
    code = code + "scrubber = scrubadub.Scrubber(locale='it_IT')" + "\n"
if options_loc == 'de_DE':
    scrubber = scrubadub.Scrubber(locale='de_DE')
    code = code + "scrubber = scrubadub.Scrubber(locale='de_DE')" + "\n"
if options_loc == 'en_UK':
    scrubber = scrubadub.Scrubber(locale='en_UK')
    code = code + "scrubber = scrubadub.Scrubber(locale='en_UK')" + "\n"
if options_loc == 'en_US':
    scrubber = scrubadub.Scrubber(locale='en_US')
    code = code + "scrubber = scrubadub.Scrubber(locale='en_US')" + "\n"

if options_space == 'it_core_news_lg':
    scrubber.add_detector(scrubadub_spacy.detectors.SpacyEntityDetector(model='it_core_news_lg'))
    code = code + "scrubber.add_detector(scrubadub_spacy.detectors.SpacyEntityDetector(model='it_core_news_lg'))" + "\n"
if options_space == 'de_core_news_sm':
    scrubber.add_detector(scrubadub_spacy.detectors.SpacyEntityDetector(model='de_core_news_sm'))
    code = code + "scrubber.add_detector(scrubadub_spacy.detectors.SpacyEntityDetector(model='de_core_news_sm'))" + "\n"
if options_space == 'en_core_web_trf':
    scrubber.add_detector(scrubadub_spacy.detectors.SpacyEntityDetector(model='en_core_web_trf'))
    code = code + "scrubber.add_detector(scrubadub_spacy.detectors.SpacyEntityDetector(model='en_core_web_trf'))" + "\n"

for i in options_cd:
    if i == 'ItalianPlate':
        class ItalianPlateFilth(scrubadub.filth.Filth):
            type = 'ITALIAN PLATE'
        class ItalianPlateDetector(scrubadub.detectors.RegexDetector):
            name = 'ItalianPlate'
            regex = re.compile("[A-Za-z]{2}[0-9]{3}[A-Za-z]{2}", re.IGNORECASE)
            filth_cls = ItalianPlateFilth
        scrubber.add_detector(ItalianPlateDetector)

        code = code + "\n" + "class ItalianPlateFilth(scrubadub.filth.Filth):" + "\n" 
        code = code + "\t" + "type = 'ITALIAN PLATE'" + "\n"
        code = code + "class ItalianPlateDetector(scrubadub.detectors.RegexDetector):" + "\n"  
        code = code + "\t" + "name = 'ItalianPlate'" + "\n"  
        code = code + "\t" + "regex = re.compile('[A-Za-z]{2}[0-9]{3}[A-Za-z]{2}', re.IGNORECASE)" + "\n"
        code = code + "\t" + "filth_cls = ItalianPlateFilth" + "\n"
        code = code + "scrubber.add_detector(ItalianPlateDetector)" + "\n"
    if i == 'ItalianCF':
        class ItalianCFFilth(scrubadub.filth.Filth):
            type = 'ITALIAN CF'
        class ItalianCFDetector(scrubadub.detectors.RegexDetector):
            name = 'ItalianCF'
            regex = re.compile("(?:[A-Z][AEIOU][AEIOUX]|[B-DF-HJ-NP-TV-Z]{2}[A-Z]){2}(?:[\dLMNP-V]{2}(?:[A-EHLMPR-T](?:[04LQ][1-9MNP-V]|[15MR][\dLMNP-V]|[26NS][0-8LMNP-U])|[DHPS][37PT][0L]|[ACELMRT][37PT][01LM]|[AC-EHLMPR-T][26NS][9V])|(?:[02468LNQSU][048LQU]|[13579MPRTV][26NS])B[26NS][9V])(?:[A-MZ][1-9MNP-V][\dLMNP-V]{2}|[A-M][0L](?:[1-9MNP-V][\dLMNP-V]|[0L][1-9MNP-V]))[A-Z]", re.IGNORECASE)
            filth_cls = ItalianCFFilth
        scrubber.add_detector(ItalianCFDetector)
        
        code = code + "\n" + "class ItalianCFFilth(scrubadub.filth.Filth):" + "\n" 
        code = code + "\t" + "type = 'ITALIAN CF'" + "\n"
        code = code + "class ItalianCFDetector(scrubadub.detectors.RegexDetector):" + "\n"  
        code = code + "\t" + "name = 'ItalianCF'" + "\n"  
        code = code + "\t" + "regex = re.compile('(?:[A-Z][AEIOU][AEIOUX]|[B-DF-HJ-NP-TV-Z]{2}[A-Z]){2}(?:[\dLMNP-V]{2}(?:[A-EHLMPR-T](?:[04LQ][1-9MNP-V]|[15MR][\dLMNP-V]|[26NS][0-8LMNP-U])|[DHPS][37PT][0L]|[ACELMRT][37PT][01LM]|[AC-EHLMPR-T][26NS][9V])|(?:[02468LNQSU][048LQU]|[13579MPRTV][26NS])B[26NS][9V])(?:[A-MZ][1-9MNP-V][\dLMNP-V]{2}|[A-M][0L](?:[1-9MNP-V][\dLMNP-V]|[0L][1-9MNP-V]))[A-Z]', re.IGNORECASE)" + "\n"
        code = code + "\t" + "filth_cls = ItalianCFFilth" + "\n"
        code = code + "scrubber.add_detector(ItalianCFDetector)" + "\n"


    if i == 'ExampleBadge':
        class ExampleBadgeFilth(scrubadub.filth.Filth):
            type = 'BADGE ID'
        class ExambpleBadgeDetector(scrubadub.detectors.RegexDetector):
            name = 'ExampleBadge'
            regex = re.compile("BADGE[0-9]{3}", re.IGNORECASE)
            filth_cls = ExampleBadgeFilth
        scrubber.add_detector(ExambpleBadgeDetector)
        
        code = code + "\n" + "class ExampleBadgeFilth(scrubadub.filth.Filth):" + "\n" 
        code = code + "\t" + "type = 'BADGE ID'" + "\n"
        code = code + "class ExampleBadgeDetector(scrubadub.detectors.RegexDetector):" + "\n"  
        code = code + "\t" + "name = 'ExampleBadge'" + "\n"  
        code = code + "\t" + "regex = re.compile('BADGE[0-9]{3}', re.IGNORECASE)" + "\n"
        code = code + "\t" + "filth_cls = ExampleBadgeFilth" + "\n"
        code = code + "scrubber.add_detector(ExampleBadgeDetector)" + "\n"

code = code + "scrubber.clean(<your text to scrab goes here>)"
st.markdown("")

st.markdown("Following python code is running:")
st.code(code, language='python')
st.markdown("----------------------")
#st.markdown("E questo il suo output:")
col1, col2 = st.columns(2)

with col1:
    st.subheader('Your Original Text:')
    for line in lines:
        st.markdown(line)

with col2:
    st.subheader('Your Scrabbed Text:')
    for line in lines:
        st.markdown(scrubber.clean(line))




