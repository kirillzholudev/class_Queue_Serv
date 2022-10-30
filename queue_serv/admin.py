from django.contrib import admin

from queue_serv.models import Register_on_shift, Process_worker, Register_in_queue

admin.site.register(Register_on_shift)
admin.site.register(Process_worker)
admin.site.register(Register_in_queue)
