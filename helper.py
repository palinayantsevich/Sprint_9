import random
import string
from data.data import RecipeData


class Helper:

    @staticmethod
    def generate_first_name():
        length = 5
        first_name = ''.join(random.choices(string.ascii_letters, k=length))
        return first_name

    @staticmethod
    def generate_last_name():
        length = 5
        last_name = ''.join(random.choices(string.ascii_letters, k=length))
        return last_name

    @staticmethod
    def generate_username():
        length = 6
        username = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        return username

    @staticmethod
    def generate_user_email():
        length = 6
        random_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
        email_for_registration = 'palina_yant_18_' + random_part + '@' + 'test.com'
        return email_for_registration

    @staticmethod
    def generate_user_password():
        length = 8
        password_for_registration = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        return password_for_registration

    @staticmethod
    def generate_recipe_name():
        length = 6
        random_part = ''.join(random.choices(string.digits, k=length))
        recipe_name = RecipeData.RECIPE_NAME + '_' + random_part
        return recipe_name
