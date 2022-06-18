from src.handlers import handler, hmac_sign


def test_successful_verification(mocker, a_lambda_url_event):
    signing_key = "foo"
    body = '{"answers": {}}'
    headers = {
        "x-formsort-signature": hmac_sign(signing_key, body)
    }
    mocker.patch("src.handlers.SIGNING_KEY", signing_key)
    event = a_lambda_url_event(headers=headers, body=body)
    r = handler(event, None)
    assert r["statusCode"] == 200


def test_unsuccessful_verification(mocker, a_lambda_url_event):
    signing_key = "foo"
    body = '{"answers": {}}'
    headers = {
        "x-formsort-signature": hmac_sign(signing_key, body)
    }
    event = a_lambda_url_event(headers=headers, body=body)
    r = handler(event, None)
    assert r["statusCode"] == 200
