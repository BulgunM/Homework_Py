
class PhoneBook:

    def __init__(self, path: str = 'phone_db.txt'):
        self.path = path
        self.phone_book = []

    def open_file(self):
        with open(self.path, 'r', encoding='UTF-8') as file:
            data = file.readlines()
        for contact in data:
            pb = {}
            new = contact.strip().split(';')
            new = contact.split(';')
            pb['name'] = new[0]
            pb['phone'] = new[1]
            pb['comment'] = new[2]
            self.phone_book.append(pb)
        print('\nТелефонная книга успешно загружена\n')

    def save_file(self):
        pass

    def get(self):
        return self.phone_book

    def new_contact(self, contact: dict):
        self.phone_book.append(contact)
        print(f'\nКонтакт {contact.get("name")} успешно записан\n')

    def search(self, word: str) -> list:
        serch_result = []
        for contact in self.phone_book:
            for field in contact.values():
                if word in field:
                    serch_result.append(contact)
        return serch_result

    def change(self, i: int, new_value: dict):
        self.phone_book[i] = new_value

    def delete(self, i: int):
        contact = self.phone_book.pop(i)
        print(f'Контакт {contact.get("name")} успешно удален')
