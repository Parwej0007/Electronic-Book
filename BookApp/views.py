# from django.http import request
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count
from .models import Book1, Topic, Post

# Create your views here.
def home(request):
    # count number of book, section, topic and post
    # for each book count section , topic etc
    context = {'all_book': get_all_books()}
    return render(request, 'Book_pages/home.html', context)

#################################################################################
def get_all_books():
    book1 = Book1.objects.annotate(topic_count=Count('topic', distinct=True)) \
        .annotate(post_count=Count('topic__post', distinct=True))
    return book1

# get each topic of books
def Topic_view(request, pk):
    # get book(pk) of given topic
    book = get_object_or_404(Book1, pk=pk)
    # get topic of that book
    topic = book.topics.all().annotate(post_count = Count('post', distinct=True))
    # or get directly topic of that book
    # b1 = Topic.objects.filter(book=pk).annotate(post_count = Count('post', distinct=True))
    contex = {'all_topic':topic, 'book':book}
    return render(request, 'Book_pages/topic_page.html', contex)

def post_view(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    post = topic.posts.all()
    return render(request, 'Book_pages/post_page.html', {'post_all':post, 'topic':topic})

##############################################################################################

# create topic for specific Book
def create_topic(request, pk):
    book = Book1.objects.get(pk=pk)
    return render(request, 'forms/create_topic.html', {'book':book})


def create_post(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    return render(request, 'forms/create_post.html', {'topic':topic})

########################################################################
#insert topic and post into database
# Insert / Update / Delete TOPIC from database
def insert_topic(request, pk):
    if request.method == 'POST':
        topic_name1 = request.POST['topic']
        topic_description1 = request.POST['description']
        book = get_object_or_404(Book1, pk=pk)
        b1 = book.topics.create(topic_name=topic_name1, description=topic_description1)
        b1.save()
        return redirect('topic', book.pk)
    return redirect('home')

def delete_topic(request, pk):
    t = get_object_or_404(Topic, pk=pk)
    t.delete()
    return redirect('topic', t.book.pk)

def update_topic(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    if request.POST == {} :
        # topic = get_object_or_404(Topic, pk=pk)
        return render(request, 'forms/update_topic.html', {'topic':topic})

    else:
        topic_name1 = request.POST['topic']
        topic_description = request.POST['description']
        t = Topic.objects.filter(pk=pk).update(topic_name=topic_name1, description = topic_description)
        return redirect('topic', topic.book.pk )

# Insert / Update / Delete TOPIC from database
def insert_post(request, pk):
    if request.method == "POST":
        title1 = request.POST['heading']
        content1 = request.POST['content']
        topic = get_object_or_404(Topic, pk=pk)
        p = topic.posts.create(heading=title1, content=content1)
        p.save()
        return redirect('post', topic.pk)

def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post', post.topic.pk)

def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.POST == {}:
        return render(request, 'forms/update_post.html', {'post':post})
    else:
        heading1 = request.POST['heading']
        content1 = request.POST['content']
        p = Post.objects.filter(pk=pk).update(heading=heading1, content=content1)
        return redirect('post', post.topic.pk)


# for searching book
def search(request):
    search_val = request.GET.get('search')

    if search_val is '':
        return redirect('home')
    else:
        book = Book1.objects.filter(book_name__contains= search_val).annotate(topic_count=Count('topic', distinct=True)) \
            .annotate(post_count= Count('topic__post', distinct=True))
        if book:
            return render(request, 'forms/search_book.html', {'book1':book})
        else:
            return render(request, 'forms/search_book.html', {'not_found': search_val})


def about(request):
    return render(request, 'Book_pages/about.html')


# create book
def create_book(request):
    if request.method == "POST":
        book_name1 = request.POST['book_name']
        book_desc = request.POST['book_desc']
        if book_name1 and book_desc is not ' ':
            b = Book1.objects.create(book_name=book_name1, description=book_desc)
            b.save()
            return redirect('home')
        else:
            return render(request, 'forms/create_book.html')
    return render(request, 'forms/create_book.html')

def delete_book(request, pk):
    d = Book1.objects.get(pk=pk)
    d.delete()
    return redirect('home')

