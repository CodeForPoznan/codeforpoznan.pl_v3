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

    username = factory.Faker("email", locale="pl_PL")
    password = "pass123"


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


class HacknightFactory(BaseFactory):
    class Meta:
        model = Hacknight

    date = factory.Faker("date_time_between", start_date="-20y", end_date="now")

    @factory.post_generation
    def participants(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for participant in extracted:
                self.participants.append(participant)
