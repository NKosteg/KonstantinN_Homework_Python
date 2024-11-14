from address import Address
from mailing import Mailing

from_address = Address('191014', 'Saint-Petersburg', 'Nekrasova street', '36', '18')
to_address = Address('265897', 'Moscow', 'Tverskaya street', '15', '67')
my_mailing = Mailing(to_address, from_address, 600, '№456123')

print(my_mailing)
