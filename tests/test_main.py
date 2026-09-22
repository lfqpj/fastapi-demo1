from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_hello():
    response = client.get("/hello/小明")

    assert response.status_code == 200
    assert response.json() == {
        "success": True,
        "message": "你好，小明，FastAPI 项目运行成功！",
        "version": "1.0.0",
    }