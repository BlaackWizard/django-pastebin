from django.core.files.storage import default_storage


class S3Storage:
    def save_file(self, file):
        return default_storage.save(file.name, file)

    def get_file_url(self, file_name):
        return default_storage.url(file_name)
