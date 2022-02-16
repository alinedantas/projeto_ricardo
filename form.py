import streamlit as st
import pandas as pd
import streamlit as st
from google.cloud import firestore

# Authenticate to Firestore with the JSON account key.
db = firestore.Client.from_service_account_json("the_key.json")

# Create a reference to the Google post.
doc_ref = db.collection("inscritos").document("inscricao")

# Then get the data at that reference.
doc = doc_ref.get()

# Let's see what we got!
st.write("The id is: ", doc.nome)
st.write("The contents are: ", doc.telefone())



st.title('Registro de amigos do Professor Ricardo Dantas')
with st.form("my_form"):
    name = st.text_input('Nome Completo', max_chars=100, placeholder='Nome Completo')
    nascimento = st.date_input('Data de Nascimento ')
    endereco = st.text_input('Endereço', max_chars=100, placeholder='Endereço')

    regiao = st.selectbox('Região em que mora no DF',
                                      ['Águas Claras ',
                                        'Arniqueira ',
                                        'Brazlândia ',
                                        'Candangolândia ',
                                        'Ceilândia ',
                                        'Cruzeiro ',
                                        'Fercal ',
                                        'Gama ',
                                        'Guará ',
                                        'Itapoã ',
                                        'Jardim Botânico ',
                                        'Lago Norte ',
                                        'Lago Sul',
                                        'Núcleo Bandeirante ',
                                        'Paranoá ',
                                        'Park Way ',
                                        'Planaltina ',
                                        'Plano Piloto ',
                                        'Recanto das Emas ',
                                        'Riacho Fundo ',
                                        'Riacho Fundo II ',
                                        'Samambaia ',
                                        'Santa Maria ',
                                        'São Sebastião ',
                                        'SCIA/Estrutural ',
                                        'SIA ',
                                        'Sobradinho ',
                                        'Sobradinho II ',
                                        'Sol Nascente e Pôr do Sol ',
                                        'Sudoeste/Octogonal ',
                                        'Taguatinga ',
                                        'Varjão ',
                                        'Vicente Pires',
                                        'Não moro no DF'])

    cep = st.text_input('CEP', max_chars=8, placeholder='CEP')
    email = st.text_input('E-mail', max_chars=100, placeholder='exemplo@exemplo.com')
    facebook = st.text_input('Facebook', max_chars=100, placeholder='https://www.facebook.com/usuario')
    instagram = st.text_input('Instagram', max_chars=100, placeholder='https://www.instagram.com/usuario/')
    # Every form must have a submit button.'
    submitted = st.form_submit_button("Enviar")

if submitted:
    dados = {'name': [name], 'regiao': [regiao]}
    dados = pd.DataFrame(dados)
    st.write(f'Olá {name} de {regiao}! Obrigado por se inscrever! https: // www.facebook.com / ricardo.dantas.520357 https://www.instagram.com/professorricardodantasgomes/')

    with open('https://share.streamlit.io/alinedantas/projeto_ricardo/main/dados.csv', 'a') as fp:
        file_writer = csv.writer(fp, delimiter=",")
        for row in dados.values:
            file_writer.writerow(row)




