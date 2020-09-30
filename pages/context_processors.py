from .models import APIPostDoc, APIUserDoc

def main_all(request):
    post_menu = APIPostDoc.objects.filter(published=True).order_by('serial')
    user_menu = APIUserDoc.objects.filter(published=True).order_by('serial')
    return {'post_menu' : post_menu, 'user_menu' : user_menu}