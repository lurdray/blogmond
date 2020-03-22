from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import Post, Breaking, Tv, Series


def index(request):
    if request.method == 'GET' and request.GET.get('query') != None:
        query = request.GET.get('query')
        posts = Post.objects.filter(
            title__icontains=query)
        #quotes = Quotes.objects.order_by('-pk')[:1]

        #for quote in quotes:
        #    quote = get_object_or_404(Quotes, pk=quote.id)
        return render(request, 'blog/index.html', {'posts': posts})

    else:
    	breaking = Breaking.objects.order_by('-pub_date')[0]
    	tv = Tv.objects.order_by('-pub_date')[:5]
    	series = Series.objects.order_by('-pub_date')[:5]
    	posts = Post.objects.order_by('-pub_date')[:5]
    	all_posts = Post.objects.order_by("-pub_date")[:12]
    	context = {'posts': posts, "all_posts":all_posts, "breaking":breaking, "tv":tv, "series":series}
    	return render(request, 'blog/index.html', context)



