# -*- coding: utf-8 -*-

"""
Classe Dao[Address]
"""

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
            sql = "SELECT * FROM address WHERE id_address=%s"
            cursor.execute(sql, (id_address,))
            result = cursor.fetchone()
            if result:
                return Address(*result)
            return None

    def update(self, address: Address) -> bool:
        """Met à jour en BD l'entité Address correspondant à address

        :param address: Adresse déjà mise à jour en mémoire
        :return: True si la mise à jour a pu être réalisée
        """
        with Dao.connection.cursor() as cursor:
            sql = "UPDATE address SET street=%s, city=%s, postal_code=%s WHERE id_address=%s"
            cursor.execute(sql, (address.street, address.city, address.postal_code, address.id_address))
            Dao.connection.commit()
            return cursor.rowcount > 0

    def delete(self, address: Address) -> bool:
        """Supprime en BD l'entité Address correspondant à address

        :param address: Adresse dont l'entité Address correspondante est à supprimer
        :return: True si la suppression a pu être réalisée
        """
        with Dao.connection.cursor() as cursor:
            sql = "DELETE FROM address WHERE id_address=%s"
            cursor.execute(sql, (address.id_address,))
            Dao.connection.commit()
            return cursor.rowcount > 0
