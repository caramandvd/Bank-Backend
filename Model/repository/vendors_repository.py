from datetime import datetime

from sqlalchemy.orm import sessionmaker

from model.domain.vendors import Vendors
from utils.db import engine, Base


class VendorsRepository:
    def __init__(self):
        self.session = sessionmaker(engine)()

    def create(self, vendor_name, email, address, phone_number):
        new_vendor = Vendors(
            vendor_name=vendor_name,
            email=email,
            address=address,
            phone_number=phone_number,
            join_date=datetime.now()
        )
        self.session.add(new_vendor)
        self.session.commit()

    def read_vendor_by_id(self, vendor_id):
        vendor = self.session.query(Vendors).filter_by(vendor_id=vendor_id).first()
        if vendor:
            return vendor
        return None

    def update(self, vendor_id, **kwargs):
        self.session.query(Vendors).filter_by(vendor_id=vendor_id).update(kwargs)
        self.session.commit()

    def delete(self, vendor_id):
        self.session.query(Vendors).filter_by(vendor_id=vendor_id).delete()
        self.session.commit()


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    repo = VendorsRepository()
    repo.create('Alianz', 'alianz@mail.com', 'Swiss', '0755512314')
    # repo.update('1000000000003', address='FattyLand')
    # print(repo.read_vendor_by_id('1000000000003'))
    # repo.delete('1000000000003')
