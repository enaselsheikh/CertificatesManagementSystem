from .models import progUserPermissions 

def ProgramesVariable(request):
    userId = request.user.id
    print(userId)
    progs = {}
    if userId and progUserPermissions.objects.filter(user_id = userId).exists():
        progs = list(progUserPermissions.objects.filter(user_id = userId))
    return {'progs':progs}
    
