from flask import Flask, render_template, request, send_from_directory
from app_logic import translate_and_save, languages

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    translated_text = ''
    paragraph = ''
    translated_filename = ''

    if request.method == 'POST':
        file = request.files['file']
        paragraph = request.form.get('paragraph', '')
        language = request.form['language']

        translated_text, paragraph, translated_filename = translate_and_save(file, paragraph, language)

    return render_template('index.html', languages=languages, translated_text=translated_text, paragraph=paragraph,
                           translated_filename=translated_filename)

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory('translated_files', filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
