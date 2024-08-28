from models.adress import Address
from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional

@dataclass
class AddressDao(Dao[Address]):
    def create(self, address: Address) -> int:
        """Crée en BD l'entité Address correspondant à l'objet address

        :param address: Adresse à créer sous forme d'entité Address en BD
        :return: l'id de l'entité insérée en BD (0 si la création a échoué)
        """
        with Dao.connection.cursor() as cursor:
            sql = "INSERT INTO address (street, city, postal_code) VALUES (%s, %s, %s)"
            cursor.execute(sql, (address.street, address.city, address.postal_code))
            Dao.connection.commit()
            return cursor.lastrowid

    def read(self, id_address: int) -> Optional[Address]:
        """Renvoie l'adresse correspondant à l'entité dont l'id est id_address
           (ou None si elle n'a pu être trouvée)"""
        with Dao.connection.cursor() as cursor:
            sql = "SELECT id_address, street, city, postal_code FROM address WHERE id_address=%s"
            cursor.execute(sql, (id_address,))
            result = cursor.fetchone()
            if result:
                # Assurez-vous d'utiliser les noms de colonnes corrects et
                # les arguments du constructeur correspondant
                return Address(
                    id=result['id_address'],  # Assurez-vous que 'id_address' correspond à l'attribut 'id'
                    street=result['street'],
                    city=result['city'],
                    postal_code=result['postal_code']
                )
            return None

    def update(self, address: Address) -> bool:
        """Met à jour en BD l'entité Address correspondant à address

        :param address: Adresse déjà mise à jour en mémoire
        :return: True si la mise à jour a pu être réalisée
        """
        with Dao.connection.cursor() as cursor:
            sql = "UPDATE address SET street=%s, city=%s, postal_code=%s WHERE id_address=%s"
            cursor.execute(sql, (address.street, address.city, address.postal_code, address.id))
            Dao.connection.commit()
            return cursor.rowcount > 0

    def delete(self, address: Address) -> bool:
        """Supprime en BD l'entité Address correspondant à address

        :param address: Adresse dont l'entité Address correspondante est à supprimer
        :return: True si la suppression a pu être réalisée
        """
        with Dao.connection.cursor() as cursor:
            sql = "DELETE FROM address WHERE id_address=%s"
            cursor.execute(sql, (address.id,))
            Dao.connection.commit()
            return cursor.rowcount > 0
