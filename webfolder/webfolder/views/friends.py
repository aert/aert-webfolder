from django.views.generic.base import TemplateView


class FriendsView(TemplateView):
    template_name = 'webfolder/friends.html'

    def get_context_data(self, **kwargs):
        context = super(FriendsView, self).get_context_data(**kwargs)
        return context
