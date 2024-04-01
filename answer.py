from functions import check, color
import requests
cache = {}

def kpolyakov(task_id, answer = False):
    url = f'https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId={task_id}'
    if url not in cache: 
        w = requests.get(url).text.split('<td class="answer">')[1].split('</td>')[0]
        w = w.split("""<script>document.write( changeImageFilePath('""")[1].split("') )</script>")[0]
        try: w = int(w)
        except: pass
        cache[url] = w
    else: w = cache[url]

    if not answer: print(f'{color.gray()}*{color.blue()} Answer:{color.magenta()} {w}')
    else: return check(answer, w)
