# Steps to make Project
	1.django-admin startproject [projectName]  -> kreiranje na obicen proekt
	2.biranje na enivronment (ako ne ti e namesten kako so treba)
	3.python manage.py [projectName so views]
	4.python manage.py runserver
	5.python manage.py migrate -> prven ova da napravi user model i views za admin panel
	6.python manage.py createsuperuser
	7.dodaj go noviot [projectName so views] vo settings -> INSTALLED_APPS
	8.python manage.py makemigrations 
	9.python manage.py migrate
	10.GG <3 !

# Steps to make media files work
    1.in SETTINGS: MEDIA_URL = '/'  (make it save in root)
                   MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
	  2.in URLS.PY: imports: from django.conf import settings
                           from django.conf.urls.static import static
                  after urlpatterns [] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
                  
