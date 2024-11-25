import uuid
from app.infrastructure.repository import PasteRepository
from app.infrastructure.storages import S3Storage

paste_repo = PasteRepository()
s3_storage = S3Storage()


class PasteService:

    def create_paste(self, owner, title, content, is_private, file=None):
        unique_url = uuid.uuid4().hex[:8]
        paste = paste_repo.create_paste(
            owner=owner,
            title=title,
            content=content,
            unique_url=unique_url,
            is_private=is_private
        )

        if file:
            s3_storage.save_file(file)

        return paste

    def get_paste(self, unique_url, user):
        paste = paste_repo.get_paste_by_url(unique_url)
        if paste and (not paste.is_private or paste.owner == user):
            return paste
        return None
