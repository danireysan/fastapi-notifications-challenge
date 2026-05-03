from core.auth.domain.value_objects.hashed_password import HashedPassword


def test_create_hashed_password_success():
    result = HashedPassword.create("some-hashed-value")

    assert result.is_success is True
    assert result.unwrap().value == "some-hashed-value"


def test_create_hashed_password_fails_when_none():
    result = HashedPassword.create(None)

    assert result.is_success is False
    assert result.failure().message == "Password is required"


def test_create_hashed_password_fails_when_blank():
    result = HashedPassword.create("   ")

    assert result.is_success is False
    assert result.failure().message == "Password is required"
