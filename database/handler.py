from django.shortcuts import render

def error_403_view(request, exception):
    return render(request, 'page_403.html', status=403)

def error_404_view(request, exception):
    return render(request, 'page_404.html', status=404)

def error_500_view(request):
    return render(request, 'page_500.html', status=500)

