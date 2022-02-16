# Dictionary

Command-line dictionary based on translations from Wiktionary. Full list of supported languages can be found [here](https://github.com/Astrochamp/Dictionary/blob/main/supported_languages.txt)

## Usage:

### Installation
Run `install.py`

### Using
Either run `main.py` and follow the guidance, or open a command prompt in your user folder and run `dictionarylookup <word> -lang <language>`

## Example:
```text
$ dictionarylookup magister -lang latin

------------------------------------------------------------------------------------------------------------------------
magister m (genitive magistrī, feminine magistra); second declension:
   teacher
   master; a title of the Middle Ages, given to a person in authority or to one having a license from a university to
   teach philosophy and the liberal arts
------------------------------------------------------------------------------------------------------------------------
```

## Notes
* Currently only supported on Windows -- Linux and Mac support coming soon!
* If no language is specified, the program will search for the word in English.

### [Create an issue](https://github.com/Astrochamp/Dictionary/issues) if you have any feedback / bugs you want to report