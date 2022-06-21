from src.handlers import handler, hmac_sign


def test_successful_verification(mocker, a_lambda_url_event, the_answers_queue):
    signing_key = "foo"
    body = '{"answers": {}}'
    headers = {
        "x-formsort-signature": hmac_sign(signing_key, body)
    }
    mocker.patch("src.handlers.SIGNING_KEY", signing_key)
    mocker.patch("src.handlers.SQS_QUEUE_URL", the_answers_queue.url)
    event = a_lambda_url_event(headers=headers, body=body)
    r = handler(event, None)
    assert r["statusCode"] == 200


def test_unsuccessful_verification(mocker, a_lambda_url_event, the_answers_queue):
    correct_signing_key = "foo"
    incorrect_signing_key = "bar"
    body = '{"answers": {}}'
    headers = {
        "x-formsort-signature": hmac_sign(incorrect_signing_key, body)
    }
    mocker.patch("src.handlers.SIGNING_KEY", correct_signing_key)
    mocker.patch("src.handlers.SQS_QUEUE_URL", the_answers_queue.url)
    event = a_lambda_url_event(headers=headers, body=body)
    r = handler(event, None)
    assert r["statusCode"] == 401


def test_missing_signature(mocker, a_lambda_url_event, the_answers_queue):
    body = '{"answers": {}}'
    mocker.patch("src.handlers.SIGNING_KEY", "foo")
    mocker.patch("src.handlers.SQS_QUEUE_URL", the_answers_queue.url)
    event = a_lambda_url_event(body=body)
    r = handler(event, None)
    assert r["statusCode"] == 401
