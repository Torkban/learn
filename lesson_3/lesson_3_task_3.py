from adress import Address
from mailing import Mailing


first_mail = Mailing(Address("363536", "Moscow", "Stolichnaya", "65", "124"), Address("666645", "St_Petersburg", "Sennaya", "66", "125"), 450, "AV48000")
print(f"Отправление {first_mail.track} из {first_mail.from_adress.index}, {first_mail.from_adress.city}, {first_mail.from_adress.road}, {first_mail.from_adress.house} - {first_mail.from_adress.room} в {first_mail.to_adress.index}, {first_mail.to_adress.city}, {first_mail.to_adress.road}, {first_mail.to_adress.house} - {first_mail.to_adress.room}. Стоимость {str(first_mail.cost)} рублей")