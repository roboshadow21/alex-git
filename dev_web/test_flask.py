from flask import Flask
from flask import request, render_template, current_app, make_response, redirect, abort, g
from jinja2 import Template
# from flask_script import Manager

app = Flask(__name__)
# manager = Manager(app)


# @app.route('/')
# def index():
#     return f'<h1>Hello! Your IP is {request.remote_addr} and you are using {request.user_agent} ' \
#            f'and {current_app.name}</h1>'

def func():
    return 'This is func() called'

@app.route('/')
def index():
    name, age, hobby = 'Alex', 51, 'programmer'
    context = dict(name=name, age=age, hobby=hobby)
    items = {'color': 'black', 'table': 'patients'}
    return render_template('index.html', var=items, func=func, **context)

# Задать заголовки с помощью кортежей
# @app.route('/')
# def render_markdown():
#     return "## Heading", 200, {'Content-Type': 'text/markdown'}

# Вернуть ошибку 404
# @app.route('/')
# def http_404_handler():
#     return make_response("<h2>404 Error</h2>", 400)

# @app.route('/user/<name>')
# def user(name):
#     return f'<h1>Hello, {name}!</h1>'

# @app.route('/')
# def index():
#     return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.route('/feedback/')
@app.route('/contact/')
def contact():
    return '<h1>This is contact page</h1>'


@app.route('/id/<int:user_id>')
def user_id(user_id):
    return f'<h1>This is page of user #{user_id}</h1>'


@app.route('/books/<genre>')
def books(genre):
    return f'<h1>Book of {genre} category</h1>'


# Ответ с помощью метода make_response()
@app.route('/music/<style>')
def music(style):
    res = make_response(f'<h1>All disks in {style} category</h1>')
    res.headers['Content-Type'] = 'text'
    res.headers['Server'] = 'localhost'
    return res


# Перенаправление
@app.route('/testum/')
def transfer():
    return redirect('http://examples.com', code=301)    #"https://localhost:5000/login" http://examples.com


# Перехват запросов
@app.before_first_request
def before_first_request():
    print('before_first_request() called')


@app.before_request
def before_request():
    print('before_request() called')


@app.after_request
def after_request(response):
    print('after_request() called')
    return response


@app.route('/bad/')
def bad_route():
    abort(403)


@app.errorhandler(403)
def http_403_handler(error):
    return f'<p>HTTP 403 error has occurred</p>', 403

# @app.route('/transfer')
# def transfer():
#     return "", 302, {'location': 'https://localhost:5000/login'}

# Карта URL адресов
# print(app.url_map)


# Шаблонизатор Jinja (любые действия в скобках)
print(Template("{{10 + 3}}").render())
print(Template("{{20 * 2}}").render())
print(Template("{{8 % 2 == 0}}").render())
# Вывод переменных
print(Template("{{ var }}").render(var=12))
print(Template("{{ var }}").render(var='Alex'))
# Список
print(Template("{{ var[:] }}").render(var=[1, 2, 3]))
# Словарь
print(Template("{{ var  }}").render(var={'name': 'tom', 'age': 51, 'prof': 'manager'}))
print(Template("{{ var['name'] }}").render(var={'name': 'tom', 'age': 51, 'prof': 'manager'}))


# Класс
class Foo:
    def __init__(self, i):
        self.i = i

    def some_method(self):
        return 'This is some_method() for class FOO called'

    def __str__(self):
        return 'This is an instance of Foo class'


print(Template("{{ var }}").render(var=Foo(5)))
print(Template("{{ obj.i }}").render(obj=Foo(5)))
print(Template("{{ obj.some_method() }}").render(obj=Foo(5)))


# Функция
def foo():
    return 'Call foo() function'


print(Template("{{ foo() }}").render(foo=foo))


# Без декоратора
# def index():
#     return 'Hello World'
#
# app.add_url_rule('/', 'index', index)


# Созданием объект ответа и устанавливаем cookies
# @app.route('/set-cookie')
# def set_cookie():
#     response = make_response('<h1>This document carries a cookie!</h1>')
#     response.set_cookie('answer', '42')
#     response.set_cookie('favorite-color', 'skyblue')
#     response.set_cookie('favorite-font', 'sans-serif')
#     return response


# Abort
# @app.route('/user/<id>')
# def get_user(id):
#     user = get_user(id)
#     if not user:
#         abort(404)
#     return f'<h1>Hello {id}</h1>'


# Вывод кода ответа
# @app.route('/')
# def index():
#     return '<h1>Bad Request!</h1>', 400

# @ app.route('/')
# def index():
#     user_agent = request.headers.get('User-Agent')
#     return f'<p>Your browser is {user_agent}</p>'


if __name__ == '__main__':
    app.run(debug=True)

# if __name__ == '__main__':
#     manager.run()


# Активация контекста приложения
# app_ctx = app.app_context()
# app_ctx.push()
# print(current_app.name)
# app_ctx.pop()
# Или через менеджер контекста
# with app.app_context():
#     print(current_app.name)
# with app.test_request_context('/product'):
#     print(request.path)
#     print(request.method)
#     print(current_app.name)
