from app.domain.models import Paste


class PasteRepository:
    def create_paste(self, **kwargs):
        return Paste.objects.create(**kwargs)

    def get_paste_by_url(self, unique_url):
        return Paste.objects.filter(unique_url=unique_url).first()

    def list_pastes_for_user(self, user):
        return Paste.objects.filter(owner=user)
