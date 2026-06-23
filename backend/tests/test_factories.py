from backend.factories import TeamFactory, TechStackFactory


def test_team_factory_batch_generates_unique_project_urls(_db):
    teams = TeamFactory.create_batch(10)

    _db.session.commit()

    project_names = [team.project_name for team in teams]
    project_urls = [team.project_url for team in teams]
    assert len(project_names) == len(set(project_names))
    assert len(project_urls) == len(set(project_urls))


def test_team_factory_handles_existing_project_name(_db):
    first_team = TeamFactory(project_name="duplicate-project")
    duplicate_team = TeamFactory(project_name="duplicate-project")

    _db.session.commit()

    assert duplicate_team.project_name != first_team.project_name
    assert duplicate_team.project_url != first_team.project_url


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
