from flask import Flask, render_template, request, jsonify
from collections import Counter
import os


app = Flask(__name__,
            static_folder='static',
            template_folder='templates')

@app.route('/')
def home():
    return render_template('home.html')

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

all_data=[]
@app.route('/join', methods=['GET', 'POST'])
def join():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        country=request.form.get('country')
        city=request.form.get('city')
        skills=request.form.get('skills')
        bio=request.form.get('bio')
        data={'name': name,
            'email': email,
            'country': country,
            'city': city,
            'skills': skills,
            'bio': bio
        }
        all_data.append(data)
    return render_template('join.html', all_data=all_data)


@app.route('/students')
def students():
    info=all_data
    return render_template('students.html', info=info)

@app.route('/api')
def api():
    json_data=jsonify(all_data)
    content=json_data.get_data(as_text=True)
    return render_template('api.html', content=content)

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')


if __name__=='__main__':
    port=int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)