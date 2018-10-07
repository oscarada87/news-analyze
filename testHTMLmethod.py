import requests
from pprint import pprint

get1="https://cse.google.com/cse/element/v1?rsz=12&num=12&hl=zh_TW&source=gcsc&gss=.com&sig=bc136da7ba6658e11a8ffa8e38396a3a&cx=013510920051559618976:klsxyhsnf7g&q=台積電&safe=off&cse_tok=AOuiMRb0i4JCdjRrtOG5JOgreiOj:1538844955929&lr=&filter=1&sort=&googlehost=www.google.com&callback=google.search.Search.csqr15567"

get2="https://cse.google.com/cse/element/v1?rsz=12&num=12&hl=zh_TW&source=gcsc&gss=.com&sig=bc136da7ba6658e11a8ffa8e38396a3a&cx=013510920051559618976:klsxyhsnf7g&q=大立光&safe=off&cse_tok=AOuiMRZ7ATfVXsiSy5JARRWLfkqM:1538845346807&lr=&filter=1&sort=&googlehost=www.google.com&callback=google.search.Search.csqr11562"

get3="https://cse.google.com/cse/element/v1?rsz=12&num=12&hl=zh_TW&source=gcsc&gss=.com&sig=bc136da7ba6658e11a8ffa8e38396a3a&cx=013510920051559618976:klsxyhsnf7g&q=台積電&safe=off&cse_tok=AOuiMRZ7ATfVXsiSy5JARRWLfkqM:1538845346807&lr=&filter=1&sort=&googlehost=www.google.com&callback=google.search.Search.csqr11562"

return_data = requests.get(get3)

pprint(return_data.text)
