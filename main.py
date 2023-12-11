from httpx import get
from parsel import Selector
from random import randint

# Selecionar a pagina de palavras mais procuradas e selecionar as tags
# https://www.dicio.com.br/palavras-mais-buscadas/
URL_SITE = "https://www.dicio.com.br"
URL_PROCURADAS = "/palavras-mais-buscadas/"
url = URL_SITE + URL_PROCURADAS
pagina_mais_procurados = get(url).content
selector = Selector(text = pagina_mais_procurados.decode())

# Selecionar a classe de lista de palavras e coletar o link das palavras mais procuradas
sub_link = selector.xpath('//ul[@class="list"]').css('a::attr(href)').getall()

# Sortear uma das palavras da lista de palavras. Aleatoreamente até a quantidade de palavras identificadas.
# A funçao randint já melhora a escolha e gera numeros aleatorios distantes um do outro
quantidade_de_palavras = len(sub_link)
# url_palavra = "/prescindir/"  # teste
url_palavra = sub_link[randint(0, quantidade_de_palavras - 1)]
print(url_palavra)

# Captura a pagina da palavras sorteada
pag_palavra = get(URL_SITE + url_palavra).content
pag_palavra_decode = Selector(text = pag_palavra.decode())

# Identifica e normaliza a palavra
palavra_nova = pag_palavra_decode.xpath('//h1/text()').get().lstrip().rstrip().lower()
# print(palavra_nova)

# Formata a palavra selecionada
palavra_atual = palavra_nova.capitalize()
tamanho_palavra = len(palavra_atual)

print(tamanho_palavra)
print(palavra_atual)

# Capturar o plural
try:
    plural = pag_palavra_decode.xpath('//div[@class="wrap-section"]').xpath('p[@class="adicional"]').css(
        'a::text').get().lower().strip()
    print(plural)
except:
    pass

# Captura os significados das palavras
pag_span = pag_palavra_decode.xpath('//p[@class="significado textonovo"]').xpath('span').getall()
for k, a in enumerate(pag_span):
    # Formata se for sobre classificação da palavra
    if '<span class="cl">' in a:
        classificacao = a.replace('<span class="cl">', '').replace('</span>', '').capitalize()
        print(f'Classificação: {classificacao}')

    # Formata se for um signicado normal
    elif '<span>' in a:
        palavra = (a.replace('<span class="cl">', '').replace('</span>', '')
                   .replace('<span><span class="tag">', '').replace('<span>', '')
                   .replace(palavra_nova, '****')
                   .replace(palavra_atual, '****')
                   .replace(':', '. Exemplo:')
                   )
        print(f'Significado {k}: {palavra}')

    # Formata se for um signicado dentro de uma área de conhecimento
    elif '<span><span class="tag">' in a:
        termo = (a.replace('<span class="cl">', '').replace('</span>', '')
                 .replace('<span><span class="tag">', '')
                 .replace(palavra_nova, '****')
                 .replace(palavra_atual, '****')
                 .replace(':', '. Exemplo:')
                 )
        print(f'Significado {k}: {termo}')

# TODO: Criar uma classe para formatar e substituir textos das tags dos signifocados
# TODO: Criar dicionario para guardar os significados 'extras' e apresentar somente quando necessário / solicitado
# TODO: Capitalize a primeira palavra do exemplo
# TODO: Aplicar o plural quando houver
