from core.auth.domain.value_objects.email_address import EmailAddress


def test_create_email_success_and_normalizes_value():
    result = EmailAddress.create("  John.DOE+work@Example.com  ")

    assert result.is_success is True
    assert result.unwrap().value == "john.doe+work@example.com"


def test_create_email_fails_when_none():
    result = EmailAddress.create(None)

    assert result.is_success is False
    assert result.failure().message == "Email is required"


def test_create_email_fails_when_blank():
    result = EmailAddress.create("   ")

    assert result.is_success is False
    assert result.failure().message == "Email is required"


def test_create_email_fails_when_invalid_format():
    result = EmailAddress.create("invalid-email")

    assert result.is_success is False
    assert result.failure().message == "Email format is invalid"


def test_create_email_fails_for_invalid_local_part():
    result = EmailAddress.create("john..doe@example.com")

    assert result.is_success is False
    assert result.failure().message == "Email format is invalid"