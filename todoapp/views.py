from django.shortcuts import render
from django.http import HttpResponseRedirect
from.models import Todo

# Create your views here.

# HTMLファイルを表示させる
def todoapp(request):
    todo_items = Todo.objects.all()
    return render(request, 'Todo.html',{'todo_items':todo_items})

# 新しいtodoタスクが入力されたら保存
# htmlにリダイレクト
def todo_post(request):
    todo_task = Todo(content = request.POST['content'])
    todo_task.save()
    return HttpResponseRedirect('/')