from django.shortcuts import render,redirect

from .models import Topic
from .forms import TopicForm

# Create your views here.

def index(request):
    """学习笔记的主页。"""
    return render(request,'learning_logs/index.html')

def topics(request):
    """显示所有的主题"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics':topics}
    return render(request,'learning_logs/topics.html',context)

def topic(request, topic_id):
    """显示单个主题机器所有的条目。"""
    topic = Topic.objects.get(id = topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic, 'entries':entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    """添加新主题。"""
    if request.method != 'Post':
        # 未提交数据，创建一个新表单
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')  #保存数据后，重定向url到主题列表网页

    #显示空表单或指出表单数据无效。
    context = {'form':form}
    return render(request, 'learning_logs/new_topic.html', context)



