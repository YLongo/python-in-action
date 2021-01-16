import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"

r = requests.get(url)
print("status code:", r.status_code)

response_dict = r.json()

print(response_dict.keys())

print("total repositories:", response_dict['total_count'])

repo_dicts = response_dict['items']
print("reposities returned:", len(repo_dicts))

names, stars = [], []

# repo_dict = repo_dicts[0]
# print("\nkeys:", len(repo_dict))

# for key in sorted(repo_dict.keys()):
#     print(key)

for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Most-Starred Python Projects in Github'
chart.x_labels = names
chart.add('', stars)
chart.render_to_file('python_repos.svg')

