# Exportar senhas de wifi salvas no Windows

Date: 2019-08-07 13:43:48

Categories: Comando local/PC, Gerenciamento

---

<p>Digamos que durante uma viagem à trabalho você precisou se conectar à uma rede wifi e que você agora precisa descobrir qual foi a senha utilizada no momento de sua criação. Para isso, o NetSh, um componente do Windows pode ser utilizado para descobrir a informação. Veja abaixo:</p>
<p>Verificar as redes wifi configuradas no computador:</p>
<pre>netsh wlan show profile</pre>
<p>Verificar as informações completas de uma configuração:</p>
<pre>netsh wlan show profile REDEWIFI key=clear</pre>
<p>Caso queira mostrar somente a senha da configuração:</p>
<pre>netsh wlan show profile REDEWIFI key=clear | select-string "key content"</pre>
<p>Se estiver usando um sistema operacional em português, utilize o comando abaixo:</p>
<pre>netsh wlan show profile REDEWIFI key=clear | select-string "conteúdo da chave"</pre>
<p>Qualquer dúvida, me avise!<br />
Até a próxima!</p>
