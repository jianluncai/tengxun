# coding: utf-8

from django.core.wsgi import get_wsgi_application
from leancloud import Engine
from leancloud import LeanEngineError


engine = Engine(get_wsgi_application())

@engine.define
def hello(**params):
    if 'name' in params:
        print('Hello, {}!'.format(params['name']))
    else:
        print('Hello, LeanCloud!')
        
@engine.define
def shuchu(**params):
    print('Hello, allun!')

@engine.before_save('Todo')
def before_todo_save(todo):
    content = todo.get('content')
    if not content:
        raise LeanEngineError('内容不能为空')
    if len(content) >= 240:
        todo.set('content', content[:240] + ' ...')

