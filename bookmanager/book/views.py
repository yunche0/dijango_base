from django.shortcuts import render

# Create your views here.


from django.http import HttpRequest
from django.http import HttpResponse

def index(request):


    #return HttpResponse('ok')
    context={
            'name':'点击有惊喜'
    }
    return render(request,'book/index.html',context=context)

from book.models import BookInfo

book=BookInfo(
    name='Django',
    pub_date='2000-1-1',
    readcount=10

        )

BookInfo.objects.create(
        name='测试开发',
        pub_date='2020-1-1',
        readcount=100
        )
