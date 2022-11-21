from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse

from .models import Stage
from .forms import StageForm


def index(request):
    context = {'form': StageForm()}
    return render(request, 'index.html', context)


# def update_stage_view(request, pk):
#     stage = get_object_or_404(Stage, pk=pk)
#     form = StageForm(instance=stage)
#     if request.method == 'POST':
#         form = StageForm(request.POST, instance=stage)
#         if form.is_valid():
#             form.save()
#             return redirect('update_stage', pk=pk)
#     return render(request, 'lcs/home.html', {'form': form})



