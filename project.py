from simple_blogger import CommonBlogger
from simple_blogger.generators.OpenAIGenerator import OpenAITextGenerator
from simple_blogger.senders.TelegramSender import TelegramSender
from simple_blogger.senders.InstagramSender import InstagramSender
from simple_blogger.senders.VkSender import VkSender
from datetime import datetime

class Project(CommonBlogger):
    def _example_task_creator(self):
        return [
            {
                "author": "Author",
                "book": "Book",
                "name": "Character",
            }
        ]

    def _get_category_folder(self, task):
        return f"{task['author']}/{task['book']}"
                    
    def _get_topic_folder(self, task):
        return f"{task['entity']}"

    def _system_prompt(self, task):
        return "Ты - книгоман"

    def _task_converter(self, idea):
        return { 
                    "author": idea['author'],
                    "book": idea['book'],
                    "entity": idea['name'],
                    "topic_prompt": f"Опиши '{idea['name']}'({idea['description'] if 'description' in idea else ''}) из книги '{idea['book']}' автора {idea['author']}, используй не более {self.topic_word_limit} слов, используй смайлики",
                    "topic_image": f"Нарисуй рисунок, вдохновлённый '{idea['name']}'({idea['description'] if 'description' in idea else ''}) из книги '{idea['book']}' автора {idea['author']}",
                }

    def __init__(self, **kwargs):
        super().__init__(
            first_post_date=datetime(2025, 2, 17),
            text_generator=OpenAITextGenerator(),
            topic_word_limit=100,
            reviewer=TelegramSender(),
            senders=[TelegramSender(channel_id=f"@illustrator_the")
                     , InstagramSender(channel_token_name='ILLUSTRATOR_THE_TOKEN')
                     , VkSender(group_id='229821765')],
            **kwargs
        ) 