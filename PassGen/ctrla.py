from random import randint, Random

from sqlalchemy import text

from PassGen import db


class Database:
    def __init__(self):
        pass

    @staticmethod
    def create(object_):
        db.session.add(object_)
        db.session.commit()

    @staticmethod
    def get(type_, id_: int):
        return db.session.query(type_).get(id_)

    @staticmethod
    def update():
        db.session.commit()

    @staticmethod
    def delete(object_):
        db.session.delete(object_)
        db.session.commit()

    @staticmethod
    def execute_stmt(stmt: str):
        db.session.execute(stmt)
        db.session.commit()

    @staticmethod
    def search(type_, order_by: str = "", filter_: str = ""):
        return db.session.query(type_).filter(text(filter_)).order_by(text(order_by))


class PassGenerator:
    def __init__(self, acc_name: str, phrase: str):
        """
        Create new Password object

        Args:
            acc_name(str): name of the account
            phrase(str): phrase to be abbreviated
        """
        self.acc_name = acc_name
        self.phrase = phrase

    def get_account_name(self) -> str:
        """
        Abbreviates the name of the account

        Returns:
            str: abbreviation of the account name
        """
        words = self.acc_name.split()
        letters = [word[0] for word in words]
        return "".join(letters).upper()

    def get_phrase(self) -> str:
        """
        Abbreviates the phrase given

        Returns:
            str: abbreviation of the phrase
        """
        words = self.phrase.split()
        letters = [word[0] for word in words]
        return "".join(letters)

    @staticmethod
    def get_number() -> str:
        """
        Gets random int between 100 and 999

        Returns:
            str: the random int
        """
        return str(randint(100, 999))

    @staticmethod
    def get_chars() -> str:
        """
        Get random special character

        Returns:
            str: the random character
        """
        chars = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]
        return Random().choice(chars)

    def generate(self) -> str:
        """
        Generate Password using info given

        Returns:
            str: the generated Password
        """
        a = self.get_account_name()
        b = self.get_phrase()
        c = self.get_number()
        d = self.get_chars()

        e = a + b + c + d
        print("Password generated.")
        return e
