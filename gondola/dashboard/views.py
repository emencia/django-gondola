from django.urls.base import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.list import ListView

from ..models import GondoleRow, Gondola
from ..tables import GondoleRowTable


class GondolaDashboardView(TemplateView):
    """
    Dashboard view for Gondole management. This view should be
    password protected.
    """

    template_name = 'gondola/dashboard/index.html'


dashboard_view = GondolaDashboardView.as_view()


class GondoleListView(ListView):
    """
    Dashboard view for Gondole management. This view should be
    password protected.
    """

    template_name = 'gondola/dashboard/gondolerow-list.html'
    model = GondoleRow

    def get_queryset(self):
        return self.model.objects.filter(active=False)

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['active_gondole_table'] = GondoleRowTable(
            self.model.objects.filter(active=True))
        context['gondole_table'] = GondoleRowTable(context['object_list'])
        return context


gondole_list_view = GondoleListView.as_view()


# Gondole row editing


class GondoleRowUpdateView(UpdateView):
    model = GondoleRow
    template_name = 'gondola/dashboard/gondolerow_form.html'
    fields = ('label', 'active', 'position', 'images')

    def get(self, request, *args, **kwargs):
        import ipdb; ipdb.set_trace()
        return super().get(request, *args, **kwargs)


gondole_update_view = GondoleRowUpdateView.as_view()


class GondoleRowCreateView(CreateView):
    model = GondoleRow
    template_name = 'gondola/dashboard/gondolerow_form.html'
    fields = ('label', 'active', 'position', 'images')


gondole_create_view = GondoleRowCreateView.as_view()


class GondoleRowDeleteView(DeleteView):
    model = GondoleRow
    template_name = 'gondola/dashboard/gondolerow_form.html'
    success_url = reverse_lazy('gondola:gondole-list')


gondole_delete_view = GondoleRowDeleteView.as_view()


# Gondola editing


class GondolaRowUpdateView(UpdateView):
    model = Gondola
    fields = ('label', 'description', 'link_to', 'position', 'image')
    template_name = 'gondola/dashboard/gondolerow_form.html'


gondola_update_view = GondolaRowUpdateView.as_view()


class GondolaRowCreateView(CreateView):
    model = Gondola
    template_name = 'gondola/dashboard/gondolerow_form.html'
    fields = ('label', 'description', 'link_to', 'position', 'image')


gondola_create_view = GondolaRowCreateView.as_view()


class GondolaRowDeleteView(DeleteView):
    model = Gondola
    success_url = reverse_lazy('gondola:gondole-list')
    template_name = 'gondola/dashboard/gondolerow_form.html'


gondola_delete_view = GondolaRowDeleteView.as_view()
