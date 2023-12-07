import requests 

url = "https://api.memegen.link/templates"

response = requests.get(url).json()

meme = str(input('Choice meme template: '))
search = meme.lower().strip()
template_list = []
count = 1

for template in response:
    if search in template['name'].lower().strip() or [x.lower().strip() for x in template['keywords'] if search in x.lower().strip()]:
        template_list.append([template['name'], template['keywords'], template['blank'], template['id'], template['lines']])

if template_list:
    for template in template_list:
        print(f'{count} - ', template[:3])
        count += 1

    choice = int(input('Choice your template: '))

    template_id = template_list[choice - 1][3]

    lines = template_list[choice - 1][4]
    write = f"{url.replace('/templates', '/images')}/{template_id}"

    print(f'This template has {lines} spaces to write !')

    for count in range(lines):
        text = str(input(f'text{count+1}: ')).replace(' ', '_')
        write = write + f"/{text}" 

    print(write)

else:
    print('No template found')
