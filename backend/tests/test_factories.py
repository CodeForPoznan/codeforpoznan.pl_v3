from backend.factories import TechStackFactory


def test_tech_stack_factory_batch_generates_unique_technologies(_db):
    tech_stacks = TechStackFactory.create_batch(5)

    _db.session.commit()

    technologies = [tech_stack.technology for tech_stack in tech_stacks]
    assert len(technologies) == len(set(technologies))


def test_tech_stack_factory_handles_existing_technology(_db):
    TechStackFactory(technology="Python")
    duplicate = TechStackFactory(technology="Python")

    _db.session.commit()

    assert duplicate.technology != "Python"
