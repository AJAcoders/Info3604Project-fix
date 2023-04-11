from App.models import User
from flask_mail import Message

def send_email(mail, subject, recipients, body):
    msg = Message(subject, recipients=recipients)
    msg.body = body
    mail.send(msg)

def send_task_assignment_email(mail, task, user):
    if user and user.email:
        subject = "New Task Assigned: {}".format(task.title)
        body = f"Dear {user.username},\n\nYou have been assigned a new task: {task.title}\nDue Date: {task.due_date}\n\nTask Details: {task.description}\n\nPlease make sure to complete the task before the due date."
        send_email(mail, subject, [user.email], body)


def send_due_date_reminder_email(mail, task):
    user = User.query.get(task.user_id)
    if user and user.email:
        subject = "Task Due Date Reminder: {}".format(task.title)
        body = f"Dear {user.username},\n\nThis is a reminder that the due date for your task '{task.title}' is today.\n\nTask Details: {task.description}\n\nPlease make sure to complete the task as soon as possible."
        send_email(mail, subject, [user.email], body)