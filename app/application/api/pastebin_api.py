from ninja import Router
from app.application.services.paste_services import PasteService
from rest_framework.authentication import TokenAuthentication


paste_service = PasteService()
router = Router(tags=['pastebin'], auth=TokenAuthentication)


@router.post('/paste', response={200: dict})
def create_paste(request, title: str, content: str, is_private: bool = False):
    user = request.auth
    paste = paste_service.create_paste(owner=user, title=title, content=content, is_private=is_private)
    return {'url': paste.unique_url}


@router.get('/paste/{unique_url}', response={200: dict, 404: str})
def get_paste(request, unique_url: str):
    user = request.auth
    paste = paste_service.get_paste(unique_url, user)
    if paste:
        return {'title': paste.title, 'content': paste.content}
    return 404, "Not found or you don't have permission"
