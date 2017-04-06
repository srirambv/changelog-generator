from github import Github

secret_file = open('github.secret', 'r')
token_string = secret_file.readline().rstrip("\n\r")

g = Github(token_string)
repo = g.get_organization("brave").get_repo("browser-laptop")

milestone_dictionary = {}
for milestone in repo.get_milestones(state="open"):
  milestone_dictionary.update({milestone.title:milestone})

key = sorted(milestone_dictionary.keys())[0]
print(key)

checklist = []
release_notes = []
exclusion_list = []
mac_checklist = []
win32_checklist = []
win64_checklist = []
linux_checklist = []

for issue in repo.get_issues(milestone=milestone_dictionary[key], state="all"):
  if('pull' not in issue.html_url):
    original_issue_title = issue.title
    issue_title = original_issue_title
    if(original_issue_title[0].islower()):
      lower = original_issue_title[0]
      upper = original_issue_title[0].upper()
      issue_title = original_issue_title.replace(lower, upper, 1)

    labels = issue.get_labels()
    label_names = []
    for label in labels:
      label_names.append(label.name)
    if('release-notes/include' in label_names):
      output_line = ' - ' + issue_title + '. ([#' + str(issue.number) + '](' + issue.html_url + '))'
      release_notes.append(output_line)

    if('QA/steps-specified' in label_names):
      output_line = ' - [ ] ' + issue_title + '. ([#' + str(issue.number) + '](' + issue.html_url + '))'
      checklist.append(output_line)
      checklist.append(issue.html_url)
      if('QA/checked-macOS' not in label_names):
        mac_checklist.append(output_line)

      if('QA/checked-Win64' not in label_names):
        win64_checklist.append(output_line)

      if('QA/checked-Win32' not in label_names):
        win32_checklist.append(output_line)

      if('QA/checked-Ubuntu' not in label_names):
        linux_checklist.append(output_line)

    else:
      output_line = ' - [ ] ' + issue_title + '. ([#' + str(issue.number) + '](' + issue.html_url + '))'
      exclusion_list.append(output_line)
      exclusion_list.append(issue.html_url)


print("Release Notes:")
for line in release_notes:
  print(line)
print("")

print("Checklist:")
for line in checklist:
  print(line)
print("")

print("Exclusion List:")
for line in exclusion_list:
  print(line)
print("")

print("Mac Checklist:")
for line in mac_checklist:
  print(line)
print("")

print("Win32 Checklist:")
for line in win32_checklist:
  print(line)
print("")

print("Win64 Checklist:")
for line in win64_checklist:
  print(line)
print("")

print("Linux Checklist:")
for line in linux_checklist:
  print(line)
print("")

'''
myrepo = g.get_user().get_repo("whatever")
title = "release notes for " + key

body = '\n'.join(release_notes)

assignee = "alexwykoff"

mymilestone_dictionary = {}
for mymilestone in myrepo.get_milestones(state="open"):
  mymilestone_dictionary.update({mymilestone.title:mymilestone})

thismilestone = mymilestone_dictionary[key]

mylabels = []
mylabels.append(myrepo.get_label("bug"))
mylabels.append(myrepo.get_label("invalid"))

print("")
print("type of thismilestone")
print(type(thismilestone))
myrepo.create_issue(title, body, assignee, thismilestone, mylabels)
'''
