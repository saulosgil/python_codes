import plotly.express as px
import pycountry

# Função para validar o nome do país
def validar_pais(nome):
    try:
        pycountry.countries.lookup(nome)
        return True
    except LookupError:
        return False

# Loop até o usuário digitar um país válido
while True:
    country = input("Digite o nome do país: ").strip()
    if validar_pais(country):
        break
    else:
        print("País não encontrado. Tente novamente (ex: 'Brazil', 'France', 'Japan').")

# Dados para o mapa
data = {
    'Country': [country],
    'Values': [100]
}

# Criar o mapa
fig = px.choropleth(
    data,
    locations='Country',
    locationmode='country names',
    color='Values',
    color_continuous_scale='Inferno',
    title=f'País destacado: {country}'
)

fig.show()
