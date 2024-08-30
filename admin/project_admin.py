from sqladmin import ModelView

from models.project_model import Project


class ProjectAdmin(ModelView, model=Project):
    column_list = [Project.id, Project.title, Project.url]
    form_excluded_columns = [Project.date]
