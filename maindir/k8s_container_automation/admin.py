from django.contrib import admin
from django.contrib.auth.models import User, Group


from k8s_container_automation.models import Cluster_admin

admin.site.site_header = 'Soorya_Project'

class Cluster_adminAdmin(admin.ModelAdmin):
	list_display = ['user_id', 'user_name','user_password']

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(Cluster_admin, Cluster_adminAdmin)
