from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Comment_duruduru, Comment_mochamilk
from django.core.paginator import Paginator

# Create your views here.
def main(request):
  return render(request, 'main/main.html')

def duruduru(request):
  page = request.GET.get('page', '1')
  comment_list = Comment_duruduru.objects.order_by('-create_date')
  paginator = Paginator(comment_list, 4)  # 페이지당 4개씩 보여주기
  page_obj = paginator.get_page(page)
  context = {'comment_list': page_obj}
  return render(request, 'main/duruduru.html', context)

def mochamilk(request):
  page = request.GET.get('page', '1')
  comment_list = Comment_mochamilk.objects.order_by('-create_date')
  paginator = Paginator(comment_list, 4)  # 페이지당 4개씩 보여주기
  page_obj = paginator.get_page(page)
  context = {'comment_list': page_obj}
  return render(request, 'main/mochamilk.html', context)

def comment_duruduru(request):
  if request.method == 'POST':
    comment = Comment_duruduru(content=request.POST.get('content'), create_date=timezone.now())
    if len(comment.content) == 0:
      return redirect('main:duruduru')
    comment.save()
  return redirect('main:duruduru')

def comment_mochamilk(request):
  if request.method == 'POST':
    comment = Comment_mochamilk(content=request.POST.get('content'), create_date=timezone.now())
    if len(comment.content) == 0:
      return redirect('main:mochamilk')
    comment.save()
  return redirect('main:mochamilk')