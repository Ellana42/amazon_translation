import boto3
from sys import argv

try:
    to_translate = argv[1]
except IndexError:
    print('You forgot the text to translate')

translate = boto3.client(service_name='translate')

translated = translate.translate_text(
    Text=to_translate, SourceLanguageCode="ja", TargetLanguageCode="en")['TranslatedText']

print(translated)
