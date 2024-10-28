import json
import jsonpath

def read_locator_from_json(locatorname):
    f=open('C:/Users/a315707/OneDrive - Deutsche Telekom AG/Schulungen/Programmierung/Python/PythonLearning/20_Advanced_Robot/Elements.json')
    response = json.loads(f.read())
    value = jsonpath.jsonpath(response,locatorname)
    return value[0]
    