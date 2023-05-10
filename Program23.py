from googletrans import Translator, LANGUAGES
def translate_text(text, target_language):
    translator = Translator()
    translated = translator.translate(text, src='en', dest=target_language)
    return translated.text

# Get user input
english_text = input("Enter English text: ")

# Translate the English text to Spanish, French, and Chinese
spanish_text = translate_text(english_text, 'es')
french_text = translate_text(english_text, 'fr')
chinese_text = translate_text(english_text, 'zh-CN')

print(f"Original English text: {english_text}")
print(f"Translated Spanish text: {spanish_text}")
print(f"Translated French text: {french_text}")
print(f"Translated Chinese text: {chinese_text}")
