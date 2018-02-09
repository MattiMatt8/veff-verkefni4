from bottle import *
import os, json

with open('./v4/bekkur.json','r',encoding='UTF-8') as f:
    bekkur = json.load(f)

@route('/')
def index():
    return template('v4/index',bekkur=bekkur)

@route('/nemandi/<kt>')
def nemandi(kt):
    for nemandi in bekkur['nemendur']:
        if nemandi['kt'] == kt:
            return template('v4/nemandi',nemandi)
    else:
        return fannstEkki()
def fannstEkki():
    return '''
    <h2>Nemandi fannst ekki</h2>
    <a href="/">Til Baka</a>
    '''

@route('/css/<skjal>')
def server_static(skjal):
    return static_file(skjal, root='./v4/css')

@error(404)
def villa404():
    return '''
    <h2>Error 404</h2>
    <h3>Síða finnst ekki</h3>
    <a href="/">Til Baka</a>
    '''

@error(500)
def villa500():
    return '''
    <h2>Error 500</h2>
    <h3>Villa í forritinu</h3>
    <a href="/">Til Baka</a>
    '''

run(host="0.0.0.0", port=os.environ.get('PORT'))
