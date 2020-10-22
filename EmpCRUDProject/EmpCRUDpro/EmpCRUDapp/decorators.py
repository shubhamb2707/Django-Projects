from django.core.exceptions import PermissionDenied
from EmpCRUDpro.EmpCRUDapp.models import EmployeeData

def user_is_entry_author(function):
    def wrap(request, *args, **kwargs):
        entry = EmployeeData.objects.get(pk=kwargs['employeedata_id'])
        if entry.created_by == request.user:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap