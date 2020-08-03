import json

url = 'https://[YOUR_REPO]/pull-requests/[PR_ID]/overview?commentId='
jdata = json.load(open('activities.json'))
f = open('comments.csv', 'wb')

for i in jdata['values']:
    i = dict(i)

    if i['action'] == 'COMMENTED' and len(i['comment']['comments']) == 0:
        comment = i['comment']['text']
        urlcom = url + str(i['comment']['id'])
        
        if not i.has_key('diff'):
            f.write(' \t \t' + comment.replace('\n', ' ') + '\t' + urlcom + '\n')
        
        else:
            filename = i['diff']['destination']['name']
            line = str(i['commentAnchor']['line'])
            
            f.write(filename + '\t' + line + '\t' + comment.replace('\n', ' ') + '\t' + urlcom + '\n')

f.close()
