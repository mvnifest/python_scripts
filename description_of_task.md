Need to use the folowing examples and the tag defined tag should be uncommented from yaml file

the command should be update_sba.py QosTest#SM-QoS_Sess_and_PCCRule_positive-rel15 or QosTest#SM-QoS_Sess_and_PCCRule_positive-rel15
and as result only that test should be uncommented
'''
tests:
  QosTest:
    type: local
    runner: SimpleRunner
    dockerCompose: /dc-yamls/docker-compose-base-config.yml
    healthCheckTimeout: 240
    tags:
      - '@GrepDockerImages'
      - '@SM-QoS_Sess_and_PCCRule_positive-rel15'
'''
