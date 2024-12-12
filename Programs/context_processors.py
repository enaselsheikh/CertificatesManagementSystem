from .models import progUserPermissions 
def ProgramesVariable(request):
    print(request.user.id)
    return {'prog':{}}
