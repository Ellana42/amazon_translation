import boto3
import click

translate = boto3.client(service_name='translate')


@click.command()
@click.argument('direct_input', required=False)
@click.option('--file', '-f', default=None, help='Takes text file as input')
@click.option('--output', '-o', default=None, help='Outputs to the given file')
def translator(direct_input, file, output):

    if file is not None:
        with open(file) as file_to_translate:
            untranslated_text = file_to_translate.read()
        translated = translate_to_jp(untranslated_text)
    else:
        translated = translate_to_jp(untranslated_text)

    if output is None:
        click.echo(translated)
    else:
        with open(output, 'w') as output_file:
            output_file.write(translated)


def translate_to_jp(text):
    translated = translate.translate_text(
        Text=text, SourceLanguageCode="ja", TargetLanguageCode="en")['TranslatedText']
    return translated


if __name__ == '__main__':
    translator()
