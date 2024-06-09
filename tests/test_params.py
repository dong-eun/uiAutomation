import pytest
import uuid

def getData():
    return [
        (uuid.uuid4().hex, uuid.uuid4().hex),
        (uuid.uuid4().hex, uuid.uuid4().hex)
    ]


@pytest.mark.parametrize("userName, password", getData())
def test_user(userName, password):
    print(f"userName : {userName}, password : {password}")

