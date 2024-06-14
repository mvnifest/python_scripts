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
