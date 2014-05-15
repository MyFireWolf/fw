from django.http import HttpResponse,HttpResponseRedirect

from django.template import Template,Context
from django.shortcuts import render_to_response
from mysite.books.models import Namebook
def hello(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

def login(request,offset):    
    plist=Namebook.objects.all()[0]
    id=plist.id
    name=plist.name
    country=plist.country
    return render_to_response('index.html',{'id':id,'name':name,'country':country})
    
def search_form(request):    
    return render_to_response('search_form.html')
def search(request):   
    if 'name' in request.GET:
        j=request.GET['name']
        plist=Namebook.objects.filter(name=j)
        if len(plist):
            id=plist[0].id
            name=plist[0].name
            country=plist[0].country
            return render_to_response('index.html',{'id':id,'name':name,'country':country})
        return HttpResponseRedirect('/search-form/')
def test_form(request):
    return HttpResponse(u"<p>welcome  %s</p>" %request.path)

