import json
import sys

vulnerability_report = open(sys.argv[1])

data = json.load(vulnerability_report)

if len(sys.argv) > 2:
    print ("Excluded packages: " + sys.argv[2])

any_vulnerability_found = false
# Iterating through the json
for vulnerability in data['vulnerabilities']:
    if vulnerability['severity'] == 'Critical':
        location = vulnerability['location']
        packageName = location['dependency']['package']['name']

        excludedPackages = []
        if len(sys.argv) > 2:
            excludedPackages = sys.argv[2].replace(' ', '')
            excludedPackages = excludedPackages.split(",")
            # Verify that the critical vulnerability isn't part of any excluded packages
            if not any(packageName in string for string in excludedPackages):
                any_vulnerability_found = true
                print(str("Non excluded vulnerability detected: " + packageName))
        else:
            any_vulnerability_found = true
            print(str("Vulnerability detected: " + packageName))

# Closing file
vulnerability_report.close()

if any_vulnerability_found:
    exit(1)
