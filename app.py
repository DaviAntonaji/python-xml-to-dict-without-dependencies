from functions.xml import xml_to_dict

xml = """
<aplicacao>
    <nome>Teste</nome>
    <versao>1.0</versao>
</aplicacao>

"""


dados = xml_to_dict(xml)
print(dados)
print(type(dados))