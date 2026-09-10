from app.main import app


def client():
    app.testing = True
    return app.test_client()


def test_index():
    resp = client().get("/")
    assert resp.status_code == 200
    assert resp.get_json()["status"] == "ok"


def test_health():
    resp = client().get("/health")
    assert resp.status_code == 200
    assert resp.get_json()["status"] == "healthy"


def test_hello_default():
    resp = client().get("/api/hello")
    assert resp.status_code == 200
    assert resp.get_json()["message"] == "Hello, world!"


def test_hello_with_name():
    resp = client().get("/api/hello?name=Dan")
    assert resp.status_code == 200
    assert resp.get_json()["message"] == "Hello, Dan!"
