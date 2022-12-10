from flask import Flask, request, redirect

app = Flask(__name__)

docs = [
    {'id':1, 'title':'첫 게시글','content':'첫 게시글입니다.'},
    {'id':2, 'title':'HTML','content':'웹 페이지 구조입니다.'},
    {'id':3, 'title':'CSS','content':'웹을 예쁘게 꾸며줍니다.'}
]

nextId = len(docs) + 1

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
    <ul>
    <li><a href="/update/{id}/">수정</a></li>
    <li><form action="/delete/{id}/" method="POST">
        <input type="submit" value="삭제"></form>
    </li>
</ul>
    '''
    return template(html)

@app.route('/create/', methods=['GET','POST'])
def create():
    if request.method == 'GET':
        html = '''
        <form action="/create/" method="post">
        <p><input  type="text" name="title" placeholder="제목"></p>
        <p><textarea name="content" style="width: 484px; height: 232px;"></textarea></p>
        <p><input type="submit" value="쓰기"></p>
    </form>'''
        return template(html)
    elif request.method == 'POST':
        global nextId
        title = request.form['title']
        content = request.form['content']
        newDocs = {'id':nextId, 'title':title, 'content':content}
        docs.append(newDocs)
        url = f'/read/{str(nextId)}/'
        nextId += 1
        return redirect(url)

@app.route('/update/<int:id>/')
def update(id):
    title = ''
    content = ''
    for doc in docs:
        if id == doc['id']:
            title = doc['title']
            content = doc['content']
            break
    html =f'''
        <form action="/update/{id}/" method="POST">
        <p><input  type="text" name="title" value="{title}"></p>
        <p><textarea name="content">{content}</textarea></p>
        <p><input type="submit" value="수정"></p>
    </form>'''
    return template(html)

@app.route('/update/<int:id>/', methods=['POST'])
def update_post(id):
    for doc in docs:
        if id == doc['id']:
            doc['title'] = request.form['title']
            doc['content'] = request.form['content']
            break

    url = f'/read/{str(id)}/'
    return redirect(url)

@app.route('/delete/<int:id>/', methods=['POST'])
def delete(id):
    for doc in docs:
        if id == doc['id']:
            docs.remove(doc)
            break
    return redirect('/')

app.run(debug=True)
