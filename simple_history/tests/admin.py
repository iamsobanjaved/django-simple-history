from django.contrib import admin

from simple_history.admin import SimpleHistoryAdmin
from simple_history.tests.external.models import ExternalModelWithCustomUserIdField

from .models import (
    Book,
    Choice,
    ConcreteExternal,
    Document,
    Employee,
    FileModel,
    Paper,
    Person,
    Planet,
    Poll,
)


@admin.register(Person)
class PersonAdmin(SimpleHistoryAdmin):
    def has_change_permission(self, request, obj=None):
        return False


@admin.register(Choice)
class ChoiceAdmin(SimpleHistoryAdmin):
    history_list_display = ["votes"]


@admin.register(FileModel)
class FileModelAdmin(SimpleHistoryAdmin):
    def test_method(self, obj):
        return "test_method_value"

    history_list_display = ["title", "test_method"]


@admin.register(Planet)
class PlanetAdmin(SimpleHistoryAdmin):
    def test_method(self, obj):
        return "test_method_value"

    history_list_display = ["title", "test_method"]


admin.site.register(Poll, SimpleHistoryAdmin)
admin.site.register(Book, SimpleHistoryAdmin)
admin.site.register(Document, SimpleHistoryAdmin)
admin.site.register(Paper, SimpleHistoryAdmin)
admin.site.register(Employee, SimpleHistoryAdmin)
admin.site.register(ConcreteExternal, SimpleHistoryAdmin)
admin.site.register(ExternalModelWithCustomUserIdField, SimpleHistoryAdmin)
