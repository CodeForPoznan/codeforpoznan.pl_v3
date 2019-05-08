import factory

from backend.extensions import db
from backend.models import Hacknight, Participant, User


class BaseFactory(factory.alchemy.SQLAlchemyModelFactory):

    class Meta:
        abstract = True
        sqlalchemy_session = db.session


class UserFactory(BaseFactory):

    class Meta:
        model = User

    username = factory.Faker("first_name", locale="pl_PL")
    password = "pass123"


class ParticipantFactory(BaseFactory):

    class Meta:
        model = Participant

    name = factory.Faker("first_name", locale="pl_PL")
    lastname = factory.Faker("last_name", locale="pl_PL")
    email = factory.LazyAttribute(
        lambda obj: "{}@cfp.com".format(obj.lastname)
    )
    github = factory.LazyAttribute(
        lambda obj: "https://github.com/{}{}".format(obj.name, obj.lastname)
    )
    phone = factory.Faker("random_int", min=100000000, max=999999999)


class HacknightFactory(BaseFactory):

    class Meta:
        model = Hacknight

    date = factory.Faker("date_time_between", start_date="-2y", end_date="now")
