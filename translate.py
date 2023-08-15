from googletrans import Translator
from json_flatten import flatten, unflatten
import json, re

with open('config.json', 'r') as f:
    config = json.load(f)

translator = Translator()

# Loads existing keys in source language file
with open(f"{config['source_language']}.json", "r+") as f:
    source_data = flatten(json.load(f))
    existing_keys = list(source_data.keys())

# Loops through target languages
for target_language in config['target_languages']:
    print(f"Translating to {target_language}...")

    # Loads target language file
    try:
        with open(f"{target_language}.json", "r+", encoding='utf-8') as f:
            if f.read(1):
                f.seek(0)
                print(f"{target_language}.json exists!")
                target_data = flatten(json.load(f))
            else:
                print(f"{target_language}.json exists but is empty!")
                target_data = {}
    except FileNotFoundError:
        with open(f"{target_language}.json", "w+", encoding='utf-8') as f:
            print(f"{target_language}.json created!")
            target_data = {}

    # Translates missing keys
    missing_keys = [key for key in existing_keys if key not in target_data.keys()]
    excluded_words = config.get('excluded_words', [])  # Load the excluded words from the config
    
    for key in missing_keys:
        source_value = source_data[key]

        words = re.findall(r'\{.*?\}|\S+|\s+', source_value)  # Find all special values, non-whitespace characters, and whitespace
        translated_words = []
        for word in words:
            if word.lower() in excluded_words or re.match(r'\{.*?\}', word):
                translated_words.append(word)
            else:
                # Preserves whitespace and translate non-special values
                if not re.match(r'\s+', word):
                    translation = translator.translate(word, dest=target_language).text
                    translated_words.append(translation)
                else:
                    translated_words.append(word)

        translation = ''.join(translated_words)
        target_data[key] = translation

    # Saves target language file
    with open(f"{target_language}.json", "w+", encoding='utf-8') as f:
        json.dump(unflatten(target_data), f, indent=4, sort_keys=False, ensure_ascii=False)

    # Prints missing keys (Just for Debug)
    if missing_keys:
        print(f"Missing keys in {target_language}.json:")
        for key in missing_keys:
            print(f"Missing: {key}")

print("Translation complete.")