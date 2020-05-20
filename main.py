import boto3
import click

translate = boto3.client(service_name='translate')


@click.command()
@click.argument('untranslated_text')
def translator(untranslated_text):
    translated = translate.translate_text(
        Text=untranslated_text, SourceLanguageCode="ja", TargetLanguageCode="en")['TranslatedText']
    click.echo('Here is your translated text :')
    click.echo(translated)


if __name__ == '__main__':
    translator()
