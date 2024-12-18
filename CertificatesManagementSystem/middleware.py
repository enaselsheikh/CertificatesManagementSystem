from django.utils import translation
from django.conf import settings

class SetLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # You can customize this condition based on your needs.
        # For example, use request headers, user profile, etc.
        language = 'ar'  # Default to Arabic
        if request.path.startswith('/admin/'): 
            # Set language to English for admin panel 
            translation.activate('en') 
        else: 
            # Set language to Arabic for the rest of the app 
            translation.activate('ar')
        # Optionally, set language based on user preference or other conditions
        # if request.user.is_authenticated:
        #     language = request.user.profile.language_preference
        response = self.get_response(request) 
        translation.deactivate() 
        return response
