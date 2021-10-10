from api import db
from flask import jsonify


class ESDLs(db.Model):
    __tablename__ = 'vue-esdl-1'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    published = db.Column(db.Boolean, nullable=False, default=False)
    description = db.Column(db.String(120), nullable=False)
    esdl_file = db.Column(db.Text)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    @classmethod
    def return_all(cls):
        def to_json(x):
            return {
                "id": x.id,
                'title': x.title,
                'description': x.description,
                "published": str(x.published),
                "file": x.esdl_file
            }

        return {'ESDLs': list(map(lambda x: to_json(x), ESDLs.query.all()))}

    @classmethod
    def delete_all(cls):
        try:
            num_rows_deleted = db.session.query(cls).delete()
            db.session.commit()
            return {'message': '{} row(s) deleted'.format(num_rows_deleted)}
        except:
            return {'message': 'Something went wrong'}

    @classmethod
    def return_id(cls, id):
        ESDL = ESDLs.query.get(id)
        return {"ESDL": {
            "id": ESDL.id,
            'title': ESDL.title,
            'description': ESDL.description,
            "published": ESDL.published,
            "file":ESDL.esdl_file
        }
        }

    @classmethod
    def update_id(cls, id, title, description, published):
        updated_ESDL = ESDLs.query.filter_by(id=id).first()
        if updated_ESDL:
            db.session.delete(updated_ESDL)
            db.session.commit()
            old_file = updated_ESDL.esdl_file
            updated_ESDL = ESDLs(
                id=id,
                title=title,
                description=description,
                published=published,
                esdl_file=old_file
            )
            db.session.add(updated_ESDL)
            db.session.commit()
        else:
            return {"Sth went wrong"}

    @classmethod
    def delete_id(cls, id):
        ESDL = ESDLs.query.filter_by(id=id).first()
        db.session.delete(ESDL)
        db.session.commit()

    @classmethod
    def find_published(cls):
        def to_json(x):
            return {
                "id": x.id,
                'title': x.title,
                'description': x.description,
                "published": x.published
            }

        return {'ESDLs': list(map(lambda x: to_json(x), ESDLs.query.filter_by(published=True).all()))}
