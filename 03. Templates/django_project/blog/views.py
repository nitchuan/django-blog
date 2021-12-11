from django.shortcuts import render

# Create your views here.
posts = [
  {
    'author': 'Nitchuan',
    'title': 'postingan pertama',
    'content': 'ini adalah postingan pertama saya',
    'date_posted': '1 Desember 2021',
  },

  {
    'author': 'Nitchuan Tech',
    'title': 'postingan kedua',
    'content': 'ini adalah postingan kedua saya',
    'date_posted': '1 Desember 2021',
  },
]

def home(request):
  context = {'posts': posts}
  return render(request, 'blog/home.html', context)

def about(request):
  return render(request, 'blog/about.html', {'title': 'About Page'})