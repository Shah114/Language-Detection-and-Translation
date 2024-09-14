# Import Modules
from flask import Flask, request, render_template
from langdetect import detect
from easygoogletranslate import EasyGoogleTranslate

# Language options (60 languages)
LANGUAGES = {
    'af': 'Afrikaans',
    'sq': 'Albanian',
    'am': 'Amharic',
    'ar': 'Arabic',
    'hy': 'Armenian',
    'az': 'Azerbaijani',
    'eu': 'Basque',
    'be': 'Belarusian',
    'bn': 'Bengali',
    'bs': 'Bosnian',
    'bg': 'Bulgarian',
    'ca': 'Catalan',
    'ceb': 'Cebuano',
    'ny': 'Chichewa',
    'zh-cn': 'Chinese (Simplified)',
    'zh-tw': 'Chinese (Traditional)',
    'hr': 'Croatian',
    'cs': 'Czech',
    'da': 'Danish',
    'nl': 'Dutch',
    'en': 'English',
    'eo': 'Esperanto',
    'et': 'Estonian',
    'tl': 'Filipino',
    'fi': 'Finnish',
    'fr': 'French',
    'gl': 'Galician',
    'ka': 'Georgian',
    'de': 'German',
    'el': 'Greek',
    'gu': 'Gujarati',
    'ht': 'Haitian Creole',
    'ha': 'Hausa',
    'iw': 'Hebrew',
    'hi': 'Hindi',
    'hmn': 'Hmong',
    'hu': 'Hungarian',
    'is': 'Icelandic',
    'ig': 'Igbo',
    'id': 'Indonesian',
    'ga': 'Irish',
    'it': 'Italian',
    'ja': 'Japanese',
    'jw': 'Javanese',
    'kn': 'Kannada',
    'kk': 'Kazakh',
    'km': 'Khmer',
    'ko': 'Korean',
    'ku': 'Kurdish (Kurmanji)',
    'ky': 'Kyrgyz',
    'lo': 'Lao',
    'la': 'Latin',
    'lv': 'Latvian',
    'lt': 'Lithuanian',
    'mk': 'Macedonian',
    'mg': 'Malagasy',
    'ms': 'Malay',
    'ml': 'Malayalam',
    'mt': 'Maltese',
    'mi': 'Maori',
    'mr': 'Marathi',
    'mn': 'Mongolian',
    'tr': 'Turkish',  
    'ur': 'Urdu',     
    'vi': 'Vietnamese', 
    'th': 'Thai'        
}

# Creating App
app = Flask(__name__, template_folder='C:/Projects/LanguageTranslation/Templates')

# Function
def detect_and_translate(text, target_lang):
    # detect language
    result_lang = detect(text)

    # translate language using easygoogletranslate
    translator = EasyGoogleTranslate(source_language='auto', target_language=target_lang, timeout=10)
    translate_text = translator.translate(text)

    return result_lang, translate_text

@app.route('/')
def index():
    return render_template('index.html', languages=LANGUAGES)

@app.route('/trans', methods=['GET', 'POST'])
def trans():
    translation = ""
    detected_lang = ""
    input_text = ""
    selected_lang = ""

    if request.method == "POST":
        text = request.form['text']
        target_lang = request.form['target_lang']
        input_text = text
        selected_lang = target_lang

        detected_lang, translation = detect_and_translate(text, target_lang)

    return render_template('index.html', translation=translation, detected_lang=detected_lang, languages=LANGUAGES, input_text=input_text, selected_lang=selected_lang)

# Main Part
if __name__ == '__main__':
    app.run(debug=True)