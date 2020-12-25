from django.shortcuts import render
from .models import Brainstorms
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView
from .forms import BSForm
from django.urls import reverse_lazy


class BrainstormHome(TemplateView):
    template_name = 'brainstorm/brainstorm_home.html'


class BSListView(ListView):
    model = Brainstorms
    template_name = 'brainstorm/list.html'

    # アイデアテーブルの全データを取得するメソッドを定義/object_listと言う名前でオブジェクトが渡される
    def queryset(self):
        return Brainstorms.objects.all()


class BSCreateView(CreateView):
    model = Brainstorms
    form_class = BSForm
    success_url = reverse_lazy('brainstorm:create_done')


def create_done(request):
    return render(request, 'brainstorm/create_done.html')


class BSUpdateView(UpdateView):
    model = Brainstorms
    form_class = BSForm
    success_url = reverse_lazy('brainstorm:update_done')


def update_done(request):
    return render(request, 'brainstorm/update_done.html')


class BSDeleteView(DeleteView):
    # 利用するモデルを指定
    model = Brainstorms
    # 削除処理が正常終了した場合の遷移先を指定
    success_url = reverse_lazy('brainstorm:delete_done')


def delete_done(request):
    return render(request, 'brainstorm/delete_done.html')
