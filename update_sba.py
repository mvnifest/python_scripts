import sys
import yaml
import re
import shutil
source_path = 'sba-tests_origin.yaml'
destination_path = 'sba-tests.yaml'


import os

def is_file_empty(file_path):
    return os.path.exists(file_path) and os.path.getsize(file_path) == 0
if is_file_empty(source_path):
    shutil.copy(destination_path,source_path)
else:
    shutil.copy(source_path, destination_path)
def comment_out_tags(file_path, test_name, tag_to_keep):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    test_section_start = re.compile(rf'^\s*{test_name}:\s*$')
    tag_line = re.compile(r'^\s*-\s*\'@(.+?)\'\s*$')
    in_test_section = False

    with open(file_path, 'w') as file:
        for line in lines:
            if test_section_start.match(line):
                in_test_section = True
                file.write(line)
                continue
            elif in_test_section and line.strip() and not line.startswith((' ', '-', '#')):
                in_test_section = False

            if in_test_section:
                tag_match = tag_line.match(line)
                if tag_match and tag_match.group(1) != tag_to_keep:
                    file.write(f"# {line}")
                else:
                    file.write(line)
            else:
                file.write(line)

    print(f"Updated {file_path}, keeping tag {tag_to_keep} in {test_name}.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python update-sba.py IntegrationTest#GrepDockerImages")
        sys.exit(1)

    arg = sys.argv[1]
    if "#" not in arg:
        print("Invalid argument format. Expected format: IntegrationTest#GrepDockerImages")
        sys.exit(1)

    test_name, tag_to_keep = arg.split("#")
    file_path = 'sba-tests.yaml'  # Update this if the file is located elsewhere

    comment_out_tags(file_path, test_name, tag_to_keep)
