from django.shortcuts import render


def words_list(request):
    return render(request, 'blog/words_list.html', {})