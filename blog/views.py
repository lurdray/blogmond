from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import Post, Quotes
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy


def index(request):
    if request.method == 'GET' and request.GET.get('query') != None:
        query = request.GET.get('query')
        posts = Post.objects.filter(
            title__icontains=query)
        quotes = Quotes.objects.order_by('-pk')[:1]

        for quote in quotes:
            quote = get_object_or_404(Quotes, pk=quote.id)
        return render(request, 'blog/index.html', {'posts': posts, 'quote': quote})

    else:
        posts = Post.objects.order_by('-pub_date')[:4]
        all_posts = Post.objects.order_by("-pub_date")[5:]
        return render(request, 'blog/index.html', {'posts': posts, "all_posts":all_posts})


def detail(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	posts = Post.objects.order_by('-pub_date')[5:9]
	all_posts = Post.objects.order_by("-pub_date")[5:]
	return render(request, 'blog/detail.html', {'post': post, 'posts': posts, "all_posts":all_posts})
	
	
def postBlog(request):
	if request.method == "POST":
		title = request.POST.get("title")
		pub_date = timezone.now()
		photo = request.FILES["photo"]
		body = request.POST.get("body")
		
		post = Post.objects.create(title=title, body=body, image=photo, pub_date=pub_date)
		post.save()
		return HttpResponseRedirect(reverse("blog:postblog"))
		
	else:
		return render(request, 'blog/post_blog.html')
