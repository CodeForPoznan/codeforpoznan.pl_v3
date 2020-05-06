import factory
from sqlalchemy import or_

from backend.extensions import db
from backend.models import Hacknight, Participant, User


class BaseFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        abstract = True
        sqlalchemy_session = db.session


class UserFactory(BaseFactory):
    class Meta:
        model = User

    username = factory.Faker("email", locale="pl_PL")
    password = "pass123"

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        session = cls._meta.sqlalchemy_session
        with session.no_autoflush:
            obj = (
                session.query(model_class)
                .filter_by(username=kwargs["username"])
                .first()
            )
        if not obj:
            obj = super(UserFactory, cls)._create(model_class, *args, **kwargs)

        return obj


class ParticipantFactory(BaseFactory):
    class Meta:
        model = Participant

    first_name = factory.Faker("first_name", locale="pl_PL")
    last_name = factory.Faker("last_name", locale="pl_PL")
    email = factory.LazyAttribute(
        lambda obj: "{}{}@codeforpoznan.test".format(obj.first_name, obj.last_name)
    )
    github = factory.LazyAttribute(
        lambda obj: f"https://github.com/{obj.first_name}{obj.last_name}"
    )
    phone = factory.Faker("random_int", min=100000000, max=999999999)

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        session = cls._meta.sqlalchemy_session
        with session.no_autoflush:
            obj = (
                session.query(model_class)
                .filter(
                    or_(
                        model_class.email == kwargs["email"],
                        model_class.github == kwargs["github"],
                    )
                )
                .first()
            )
        if not obj:
            obj = super(ParticipantFactory, cls)._create(model_class, *args, **kwargs)

        return obj


class HacknightFactory(BaseFactory):
    class Meta:
        model = Hacknight

    date = factory.Faker("date_between", start_date="-20y", end_date="now")

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        session = cls._meta.sqlalchemy_session
        with session.no_autoflush:
            obj = session.query(model_class).filter_by(date=kwargs["date"]).first()

        if not obj:
            obj = super(HacknightFactory, cls)._create(model_class, *args, **kwargs)

        return obj

    @factory.post_generation
    def participants(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for participant in extracted:
                self.participants.append(participant)
