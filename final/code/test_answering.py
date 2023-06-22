import pytest
from fastapi.testclient import TestClient
from api_answering import app
import json
import os


def load_json_file(file_path):
    with open(file_path) as test_file:
        json_txt = test_file.read()
    parsed_json = json.loads(json_txt)
    return parsed_json


def request_answer(answer_json):
    response_answer = client.post("/answer/", json={'context': answer_json['context'],
                                  'question': answer_json['question']})
    return response_answer

@pytest.fixture
def script_path():
    return os.path.dirname(os.path.abspath(__file__))


client = TestClient(app)


def test_root():
    response_root = client.get("/")
    assert response_root.status_code == 200
    assert response_root.json() == {"message": 'Hello adsfasd'}


def test_nswer():
    response_answer = client.post("/answer/", json={'context': '''Twelve months
    ago Robin Parker left his job at an insurance company. He now runs
    a restaurant which is doing very well since it opened four months ago.
    Opening a restaurant was a big change for Robin. He loves travelling and
    all his favourite television programmes are about cooking. One day, he
    read in a newspaper about a doctor who left her job and moved to Italy
    to start a restaurant. He thought, “I can do that!” His wife wasn’t very
    happy about the idea, and neither was his father. But his brother, a bank
    manager, gave him lots of good ideas. Robin lived in Oxford and had a job
    in London. He thought both places would be difficult to open a restaurant
    in, so he chose Manchester because he knew the city from his years at
    university. He found an empty building in a beautiful old street. It was
    old and needed a lot of repairs, but all the other buildings were
    expensive and he didn’t have much money. Robin loves his new work. It’s
    difficult being the boss, but he has found an excellent chef. He says he
    enjoys talking to customers and some of them have become his good friends.
    He gets up at 6pm and often goes to bed after midnight. It’s a long day
    but he only starts to feel really tired when he takes time off at the
    weekends. Robin’s restaurant is doing so well that he could take a long
    holiday. But he’s busy with his new idea to open a supermarket selling
    food from around the world. He’s already found a building near his
    restaurant.'''.replace('\n', ' ').replace('     ', ' '),
        'question': 'Who helped Robin open his restaurant?'})
    json_data = response_answer.json()

    assert response_answer.status_code == 200
    assert json_data['answer'] == 'his brother, a bank manager'


def test_answer_1(script_path):
    test_file_path = script_path+'/../datasets/answer_response_1.json'
    parsed_json = load_json_file(test_file_path)
    response_answer = request_answer(parsed_json)

    assert response_answer.status_code == 200
    assert parsed_json['answer'] == response_answer.json()['answer']


def test_answer_2(script_path):
    test_file_path = script_path+'/../datasets/answer_response_2.json'
    parsed_json = load_json_file(test_file_path)
    response_answer = request_answer(parsed_json)

    assert response_answer.status_code == 200
    assert parsed_json['answer'] == response_answer.json()['answer']


def test_answer_3(script_path):
    test_file_path = script_path+'/../datasets/answer_response_3.json'
    parsed_json = load_json_file(test_file_path)
    response_answer = request_answer(parsed_json)

    assert response_answer.status_code == 200
    assert parsed_json['answer'] == response_answer.json()['answer']


def test_answer_4(script_path):
    test_file_path = script_path+'/../datasets/answer_response_4.json'
    parsed_json = load_json_file(test_file_path)
    response_answer = request_answer(parsed_json)

    assert response_answer.status_code == 200
    assert parsed_json['answer'] == response_answer.json()['answer']


def test_answer_5(script_path):
    test_file_path = script_path+'/../datasets/answer_response_5.json'
    parsed_json = load_json_file(test_file_path)
    response_answer = request_answer(parsed_json)

    assert response_answer.status_code == 200
    assert parsed_json['answer'] == response_answer.json()['answer']
