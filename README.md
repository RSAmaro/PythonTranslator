## Installation Guide
Install latest [Python](https://www.python.org/) version. (Latest tested: 3.11.4)

- sudo apt update 
- sudo apt install pip
- pip install -r requirements.txt

## Usage
Create a source_language file (e.g.: EN.json);

A default configuration file has been provided;

Edit config.json target_languages to add more languages;

Edit excluded_words for words you don't want to be translated, if not used leave it empty;

After that, you can run the script:
- python translate.py

## Config Example
```json
{
  "source_language": "EN",
  "target_languages": [
    "DE",
    "PT",
    "FR"
  ],
  "excluded_words": [
    "menu"
  ]
}
```

## Supports named formatting
```json
{
	"hello": "{msg} world",
	"name": "My name is {first_name} {last_name}"
}
```

## Supported Languages
```json
    "af": "afrikaans",
    "sq": "albanian",
    "am": "amharic",
    "ar": "arabic",
    "hy": "armenian",
    "az": "azerbaijani",
    "eu": "basque",
    "be": "belarusian",
    "bn": "bengali",
    "bs": "bosnian",
    "bg": "bulgarian",
    "ca": "catalan",
    "ceb": "cebuano",
    "ny": "chichewa",
    "zh-cn": "chinese (simplified)",
    "zh-tw": "chinese (traditional)",
    "co": "corsican",
    "hr": "croatian",
    "cs": "czech",
    "da": "danish",
    "nl": "dutch",
    "en": "english",
    "eo": "esperanto",
    "et": "estonian",
    "tl": "filipino",
    "fi": "finnish",
    "fr": "french",
    "fy": "frisian",
    "gl": "galician",
    "ka": "georgian",
    "de": "german",
    "el": "greek",
    "gu": "gujarati",
    "ht": "haitian creole",
    "ha": "hausa",
    "haw": "hawaiian",
    "iw": "hebrew",
    "he": "hebrew",
    "hi": "hindi",
    "hmn": "hmong",
    "hu": "hungarian",
    "is": "icelandic",
    "ig": "igbo",
    "id": "indonesian",
    "ga": "irish",
    "it": "italian",
    "ja": "japanese",
    "jw": "javanese",
    "kn": "kannada",
    "kk": "kazakh",
    "km": "khmer",
    "ko": "korean",
    "ku": "kurdish (kurmanji)",
    "ky": "kyrgyz",
    "lo": "lao",
    "la": "latin",
    "lv": "latvian",
    "lt": "lithuanian",
    "lb": "luxembourgish",
    "mk": "macedonian",
    "mg": "malagasy",
    "ms": "malay",
    "ml": "malayalam",
    "mt": "maltese",
    "mi": "maori",
    "mr": "marathi",
    "mn": "mongolian",
    "my": "myanmar (burmese)",
    "ne": "nepali",
    "no": "norwegian",
    "or": "odia",
    "ps": "pashto",
    "fa": "persian",
    "pl": "polish",
    "pt": "portuguese",
    "pa": "punjabi",
    "ro": "romanian",
    "ru": "russian",
    "sm": "samoan",
    "gd": "scots gaelic",
    "sr": "serbian",
    "st": "sesotho",
    "sn": "shona",
    "sd": "sindhi",
    "si": "sinhala",
    "sk": "slovak",
    "sl": "slovenian",
    "so": "somali",
    "es": "spanish",
    "su": "sundanese",
    "sw": "swahili",
    "sv": "swedish",
    "tg": "tajik",
    "ta": "tamil",
    "te": "telugu",
    "th": "thai",
    "tr": "turkish",
    "uk": "ukrainian",
    "ur": "urdu",
    "ug": "uyghur",
    "uz": "uzbek",
    "vi": "vietnamese",
    "cy": "welsh",
    "xh": "xhosa",
    "yi": "yiddish",
    "yo": "yoruba",
    "zu": "zulu"
```


## Example
*EN.json*
```json
{
    "menu": {
        "title": "Menu",
        "settings": "Settings"
    },
    "login": {
        "welcome": "Welcome",
        "signUp": "Log into your account",
        "email": "Email or Username",
        "password": "Password"
    }
}
```

*PT.json*
```json
{
    "menu": {
        "title": "Menu",
        "settings": "Configurações"
    },
    "login": {
        "welcome": "Bem-vindo",
        "signUp": "Registro em seu conta",
        "email": "E-mail ou Nome de usuário",
        "password": "Senha"
    }
}
```
