import datetime

from PassGen import cursor_, mysql_


class Account:
    def __init__(
        self,
        name: str,
        password: str,
        username: str = None,
        hint: str = None,
        last_updated: datetime.datetime = None,
        id: int = None,
    ):
        self.name = name
        self.password = password
        self.username = username
        self.hint = hint
        self.last_updated = last_updated
        self.id = id

    @classmethod
    def get(cls, id: int):
        cursor_.execute(
            "SELECT name, password, username, hint, last_updated, id FROM PassGen.accounts WHERE id=%s",
            (id,),
        )
        result = cursor_.fetchone()
        return Account(result[0], result[1], result[2], result[3], result[4], result[5])

    @classmethod
    def all(cls):
        cursor_.execute(
            "SELECT name, password, username, hint, last_updated, id FROM PassGen.accounts ORDER BY id DESC"
        )
        results = cursor_.fetchall()
        return [Account(i[0], i[1], i[2], i[3], i[4], i[5]) for i in results]

    def insert(self):
        cursor_.execute(
            "INSERT INTO PassGen.accounts (name, password, username, hint, last_updated) VALUES (%s, %s, %s, %s, %s)",
            (
                self.name,
                self.password,
                self.username,
                self.hint,
                self.last_updated,
            ),
        )
        mysql_.commit()

    def edit(self):
        cursor_.execute(
            "UPDATE PassGen.accounts SET name=%s, password=%s, username=%s, hint=%s, last_updated=%s WHERE id=%s",
            (
                self.name,
                self.password,
                self.username,
                self.hint,
                self.last_updated,
                self.id,
            ),
        )
        mysql_.commit()

    def delete(self):
        cursor_.execute("DELETE FROM PassGen.accounts WHERE id=%s", (self.id,))
        mysql_.commit()
