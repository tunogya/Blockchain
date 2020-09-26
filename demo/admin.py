from django.contrib import admin
from demo.models.block import Block
from demo.models.transaction import Transaction
from demo.models.event import Event
from demo.models.node import Node


@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    list_display = ['index', 'hash', 'previous_hash', 'create_time', 'proof']


@admin.register(Transaction)
class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'type', 'content']


@admin.register(Event)
class NodeAdmin(admin.ModelAdmin):
    list_display = ['id', 'parsed_url']


@admin.register(Node)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['id', 'state', 'events', 'data']
