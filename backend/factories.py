from random import randint

import factory
from factory import fuzzy
from sqlalchemy import or_

from backend.extensions import db
from backend.models import Hacknight, Participant, Team, TechStack, User, UserSkill


class BaseFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        abstract = True
        sqlalchemy_session = db.session


class UserFactory(BaseFactory):
    class Meta:
        model = User

    github_username = factory.Faker("email", locale="pl_PL")
    password = "pass123"
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.Faker("email")
    phone = factory.Faker("msisdn")
    slack = factory.Faker("word")
    is_admin = True

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        session = cls._meta.sqlalchemy_session
        with session.no_autoflush:
            existing = (
                session.query(model_class)
                .filter_by(github_username=kwargs["github_username"])
                .first()
            )
        if existing:
            kwargs["github_username"] = cls.github_username.generate({})

        obj = super(UserFactory, cls)._create(model_class, *args, **kwargs)

        return obj


class ParticipantFactory(BaseFactory):
    class Meta:
        model = Participant

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.LazyAttribute(
        lambda obj: "{}{}@codeforpoznan.test".format(obj.first_name, obj.last_name)
    )
    github_username = factory.LazyAttribute(
        lambda obj: f"{obj.first_name}{obj.last_name}"
    )
    phone = factory.Faker("random_int", min=100000000, max=999999999)

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        session = cls._meta.sqlalchemy_session
        with session.no_autoflush:
            existing = (
                session.query(model_class)
                .filter(
                    or_(
                        model_class.email == kwargs["email"],
                        model_class.github_username == kwargs["github_username"],
                    )
                )
                .first()
            )
        if existing:
            kwargs["email"] = cls.email.generate({})
            kwargs["github_username"] = cls.github_username.generate({})

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
            existing = session.query(model_class).filter_by(date=kwargs["date"]).first()

        if existing:
            kwargs["date"] = cls.date.generate({})

        obj = super(HacknightFactory, cls)._create(model_class, *args, **kwargs)

        return obj

    @factory.post_generation
    def participants(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for participant in extracted:
                self.participants.append(participant)


class TeamFactory(BaseFactory):
    class Meta:
        model = Team

    project_name = factory.Faker("word", locale="pl_PL")
    description = factory.Faker("paragraph", locale="pl_PL")
    project_url = factory.LazyAttribute(
        lambda obj: f"https://{obj.project_name}.codeforpoznan.test"
    )

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        session = cls._meta.sqlalchemy_session
        with session.no_autoflush:
            existing = (
                session.query(model_class)
                .filter_by(project_name=kwargs["project_name"])
                .first()
            )

        if existing:
            project_name = cls.project_name.generate({})
            kwargs["project_name"] = project_name
            kwargs["project_url"] = f"https://{project_name}.codeforpoznan.test"

        obj = super(TeamFactory, cls)._create(model_class, *args, **kwargs)

        return obj

    @factory.post_generation
    def members(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for member in extracted:
                self.members.append(member)

    @factory.post_generation
    def tech_stack(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for techstack in extracted:
                self.tech_stack.append(techstack)


class TechStackFactory(BaseFactory):
    class Meta:
        model = TechStack

    technology = factory.Faker("word")
    label = fuzzy.FuzzyChoice(["frontend", "backend", "DevOps", "UX"])

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        session = cls._meta.sqlalchemy_session
        with session.no_autoflush:
            existing = (
                session.query(model_class)
                .filter_by(technology=kwargs["technology"])
                .first()
            )

        if existing:
            kwargs["technology"] = cls.technology.generate({})

        obj = super(TechStackFactory, cls)._create(model_class, *args, **kwargs)

        return obj


class UserSkillsFactory(BaseFactory):
    class Meta:
        model = UserSkill

    skill_level = fuzzy.FuzzyChoice([level for level in range(11)])
    is_learning_goal = fuzzy.FuzzyChoice([True, False])

    @factory.post_generation
    def user_id(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            self.user = extracted

    @factory.post_generation
    def skill(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            self.skill = extracted
