from github import Github

secret_file = open('github.secret', 'r')
token_string = secret_file.readline().rstrip("\n\r")

g = Github(token_string)
repo = g.get_organization("brave").get_repo("browser-laptop")

print(repo.name)
#print(type(repo))
milestone_dictionary = {}
for milestone in repo.get_milestones(state="open"):
#  print(milestone.number)
#  print(milestone.title)
#  print(type(milestone))
  milestone_dictionary.update({milestone.title:milestone})

#for key in sorted(milestone_dictionary.keys()):
key = sorted(milestone_dictionary.keys())[0]
print(key)

print("Issues: ")

for issue in repo.get_issues(milestone=milestone_dictionary[key], state="open"): #all
  print(issue.title)
