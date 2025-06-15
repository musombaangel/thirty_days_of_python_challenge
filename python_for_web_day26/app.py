from flask import Flask, render_template, request
from collections import Counter
import os

app = Flask(__name__,
            static_folder='static',
            template_folder='templates')

@app.route('/')
def home():
    techs = ['HTML', 'CSS', 'Flask', 'Python']
    name = '30 Days Of Python Programming'
    return render_template('home.html', techs=techs, name=name)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/text-analyzer', methods=['GET','POST'])
def text_analyzer():
    txt=""
    chars=0
    mf_word=""
    word_count=0
    lex=""
    if request.method=='POST':
        txt=request.form.get('text-analyze')
        words=txt.split(" ")
        word_count=len(words)
        chars=len(txt)
        count=Counter(words)
        mf_word=count.most_common(1)[0][0]
        l=len(set(words))/word_count
        lex=f'{l}%'

    return render_template('text_analyzer.html',
                           txt=txt,
                           chars=chars,
                           word_count=word_count,
                           mf_word=mf_word,
                           lex=lex)


if __name__=='__main__':
    port=int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)