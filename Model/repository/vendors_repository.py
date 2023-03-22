from datetime import datetime

from sqlalchemy.orm import sessionmaker

from model.domain.vendors import Vendors
from utils.db import engine, Base


class VendorsRepository:
    def __init__(self):
        self.session = sessionmaker(engine)()

    def create(self, vendor_name, email, address, phone_number, account):
        new_vendor = Vendors(
            vendor_name=vendor_name,
            email=email,
            address=address,
            phone_number=phone_number,
            join_date=datetime.now(),
            account=account
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

    def return_vendor_name_by_id(self, vendor_id):
        vendor = self.session.query(Vendors).filter_by(vendor_id=vendor_id).first()
        if vendor:
            return vendor.vendor_name
        return None

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    repo = VendorsRepository()
    print(repo.return_vendor_name_by_id('1000000000000'))
