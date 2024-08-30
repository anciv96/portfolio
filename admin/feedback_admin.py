from sqladmin import ModelView

from models.feedback_model import Feedback


class FeedbackAdmin(ModelView, model=Feedback):
    column_list = [Feedback.author, Feedback.text, Feedback.url]
    form_columns = ['author', 'text', 'url']
