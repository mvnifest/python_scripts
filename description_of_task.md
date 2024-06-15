Need to use the folowing examples and the tag defined tag should be uncommented from yaml file

the command should be update_sba.py QosTest#SM-QoS_Sess_and_PCCRule_positive-rel15 or QosTest#SM-QoS_Sess_and_PCCRule_positive-rel15
and as result only that test should be uncommented
```
tests:
  QosTest:
    type: local
    runner: SimpleRunner
    dockerCompose: /dc-yamls/docker-compose-base-config.yml
    healthCheckTimeout: 240
    tags:
      - '@GrepDockerImages'
      - '@SM-QoS_Sess_and_PCCRule_positive-rel15'
```
Lets split to small tasks
# Parsing the input params
## split by '#' and get two item in the list for example below:
```
# parse_params shoud return dictionary[test_name,list[tags]]
 def parse_params(param):
    test_suite = param.split("#")
    output_dict = {}
    suite_key = test_suite[0]
    tests_csv= test_suite[1]
    #.... some logic here to make list[tags] and adding into output_dict
    return output_dict
```
### params[0] is your test_name
# check that file sba-tests_origin.yaml exists
## if not exists copy sba-tests.yaml into sba-tests_origin.yaml
# reading file line by line and 


You can look at the example of code below:
```python:
import os, sys, shutil
import logging, argparse

# Configure the logging module
#logging.basicConfig(level=logging.ERROR)

def logger_decorator(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Calling function {func.__name__} with arguments {args} and keyword arguments {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"Function {func.__name__} returned {result}")
        return result
    return wrapper

SBA_TEST_FILE="./target/test-classes/sba-tests.yaml"
SBA_TEST_ORIGINAL=f"{SBA_TEST_FILE}.original"


def file_exists(file_path):
    if os.path.exists(file_path):
        logging.info(f"The file {file_path} exists.")
        return True
    else:
        logging.info(f"The file {file_path} does not exist.")
        return False

def prepare_sba_test_file():
    if not file_exists(SBA_TEST_FILE):
        print(f"The following {SBA_TEST_FILE} is not found!!!")
        sys.exit(1)
    if not file_exists(SBA_TEST_ORIGINAL):
        shutil.copyfile(SBA_TEST_FILE,SBA_TEST_ORIGINAL)
    with open(SBA_TEST_FILE,"w") as file:
        pass

@logger_decorator
def write_line(line,to_comment):
    with open(SBA_TEST_FILE, 'a') as file:
        if to_comment == True:
            file.write("#" + line)
        else:
            file.write(line)

#@logger_decorator
def is_test_presented(line,list_of_tests):
    for test in list_of_tests:
        if test in line:
            return True
    return False


def update_file(suite_name,tests):
    #open file
    suite_section_enabled = False
    tests_section_enabled = False
    with open(SBA_TEST_ORIGINAL, 'r') as file:
        lines = file.readlines() 
        for line in lines:
            to_comment = False
            if suite_section_enabled and tests_section_enabled and not line.startswith("      - '@"):
                suite_section_enabled = False
                tests_section_enabled = False
            if not suite_section_enabled and (f"  {suite_name}:\n" == line):
                suite_section_enabled = True
            if not tests_section_enabled and (suite_section_enabled and line.startswith("    tags:")):
                tests_section_enabled = True
                write_line(line,False)
                continue
            if suite_section_enabled and tests_section_enabled:
                test_enabled = not is_test_presented(line,tests)
            to_comment = suite_section_enabled and tests_section_enabled and test_enabled
            write_line(line,to_comment)

def parse_params(param):
    test_suite = param.split("#")
    # Create a dictionary from the key-value pairs
    output_map = {}
    suite_key = test_suite[0]
    tests_csv= test_suite[1]
    logger.info(f"suite_key: {suite_key}")
    logger.info(f"test_csv: {tests_csv}")
    if "," in tests_csv:
        tests = tests_csv.split(',')
    else:
        tests = [tests_csv]
    output_map[suite_key] = tests
    return output_map

#print(parse_params("InterrationTest#test1,test2"))
#input_params = sys.argv[1]

parser = argparse.ArgumentParser()

parser.add_argument(
    'params', 
    type=str,
    help=(
        "Provide TestSuite parameters"
        "Example -DIntegrationTest#myTest'"),
)

parser.add_argument(
    "-log",
    "--log", 
    default="error",
    help=(
        "Provide logging level. "
        "Example --log debug', default='warning'"),
)


options = parser.parse_args()
levels = {
    'critical': logging.CRITICAL,
    'error': logging.ERROR,
    'warn': logging.WARNING,
    'warning': logging.WARNING,
    'info': logging.INFO,
    'debug': logging.DEBUG
}
level = levels.get(options.log.lower())
if level is None:
    raise ValueError(
        f"log level given: {options.log}"
        f" -- must be one of: {' | '.join(levels.keys())}")
logging.basicConfig(level=level)
logger = logging.getLogger(__name__)

input_params = options.params
print(f"input_params: {input_params}")

if not "#" in input_params:
    logging.error("the argument is invalid!!!")
    sys.exit(1)

test_map = parse_params(input_params)
prepare_sba_test_file()
for key in test_map:
    update_file(key,test_map[key])

```
