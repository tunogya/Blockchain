from django.contrib import admin


class BlockAdmin(admin.ModelAdmin):
    list_display = ['index', 'hash', 'previous_hash', 'create_time', 'proof']


class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'type', 'content']


class NodeAdmin(admin.ModelAdmin):
    list_display = ['id', 'parsed_url']


class TransactionAdmin(admin.ModelAdmin):
    list_display = ['id', 'state', 'events', 'data']
