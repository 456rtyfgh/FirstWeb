from flask import Flask

app = Flask(__name__)

docs = [
    {'id':1, 'title':'첫 게시글','content':'첫 게시글입니다.'},
    {'id':2, 'title':'HTML','content':'웹 페이지 구조입니다.'},
    {'id':3, 'title':'CSS','content':'웹을 예쁘게 꾸며줍니다.'}
]

def template(html):
    olTag = '<ol>'
    for doc in docs:
        olTag += '<li><a href="/read/{}/">{}</a></li>'.format(doc['id'], doc['title'])
    olTag += '</ol>'

    return f'''<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>게시판</title>
</head>
<body>
    <h1><a href="/">나의 웹페이지 이름</a></h1>
    {olTag}
    {html}
</body>
</html>'''

@app.route('/')
def index():
    html = '''<ul><li><a href="/create/">글쓰기</a></li></ul>'''
    return template (html)


@app.route('/reads/<int:id>/')
def reads(id):
    result = id + 1
    return str(result)

@app.route('/read/<int:id>/')
def read(id):
    title = ''
    content = ''
    for doc in docs:
        if doc['id'] == id:
            title = doc['title']
            content = doc['content']

    html = f'''<h1>{title}</h1>
    <p>{content}</p>
    '''
    return template(html)

app.run(debug=True)

