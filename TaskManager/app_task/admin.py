from django.contrib import admin
from .models import Proj, Sprint, Task, TaskStep
from datetime import date  # noqa


@admin.register(Proj)
class ProjAdmin(admin.ModelAdmin):
    list_display = tuple(v.attname for v in Proj._meta.fields)
    readonly_fields = ("uweb",)

    def save_model(self, request, obj, form, change) -> None:
        # сохранение пользователя, изменившего запись
        obj.uweb_id = request.user.id
        return super().save_model(request, obj, form, change)


@admin.register(Sprint)
class SprintAdmin(admin.ModelAdmin):
    list_display = tuple(v.attname for v in Sprint._meta.fields)
    readonly_fields = ("uweb",)

    def save_model(self, request, obj, form, change) -> None:
        # сохранение пользователя, изменившего запись
        obj.uweb_id = request.user.id
        return super().save_model(request, obj, form, change)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = tuple(v.attname for v in Task._meta.fields)
    readonly_fields = ("uweb",)

    def save_model(self, request, obj, form, change) -> None:
        # сохранение пользователя, изменившего запись
        obj.uweb_id = request.user.id
        return super().save_model(request, obj, form, change)


@admin.register(TaskStep)
class TaskStepAdmin(admin.ModelAdmin):
    list_display = tuple(v.attname for v in TaskStep._meta.fields)
