class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def update_phone(self, new_phone):
        self.phone = new_phone

    def show_info(self):
        print(
            f"Ism: {self.name}\n" \
            f"Telefon: {self.phone}"
        )


name = "Malika"
phone = "901234567"
contact = Contact(name, phone)

tanlov = input("Contactni yangilashni xohlaysizmi y/n: ")

if tanlov == "y":
    phone = input("Yangi raqamni kiritng: ")
    contact.update_phone(phone)
    print("Raqam yangilandi")
    contact.show_info()
else:
    print("Raqam yangilanmadi")
    contact.show_info()


