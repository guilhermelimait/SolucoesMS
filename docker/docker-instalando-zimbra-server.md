# Docker: Instalando Zimbra Server

Date: 2020-06-17 17:17:31

Categories: Docker, Zimbra

---

<p>O Zimbra server é uma ferramenta de gestão de emails corporativos, ela pode ser instalada em docker para testes de ambientes e para validar o que é necessário para seus testes locais.</p>
<p>Para que possa instalar esse servidor de e-mails, utilizaremos dos seguintes procedimentos:</p>
<ol>
<li>Vá no menu Iniciar e digite &#8220;Powershell&#8221; &gt; Abra o Powershell com direitos administrativos</li>
<li>Siga o procedimento abaixo para instalar o Zimbra server:
<ul>
<li>Digite o seguinte comando para o download das ferramentas necessárias para o servidor:
<ul>
<li>
<pre>docker pull jorgedlcruz/zimbra</pre>
</li>
</ul>
</li>
<li>Digite o comando abaixo para criar o container do Zimbra:
<ul>
<li style="text-align: justify;">
<pre>docker run -p 25:25 -p 80:80 -p 465:465 -p 587:587 -p 110:110 -p 143:143 -p 993:993 -p 995:995 -p 443:443 -p 8080:8080 -p 8443:8443 -p 7071:7071 -p 9071:9071 -h zimbra-docker.zimbra.io --dns 127.0.0.1 --dns 8.8.8.8 -i -t -e PASSWORD=Zimbra2017 jorgedlcruz/zimbra</pre>
</li>
</ul>
</li>
<li>Ao finalizar a instalação, o Zimbra vai ter iniciado mas não vai ter todos os recursos prontos ainda para uso. Para isso você deverá abrir uma outra sessão do powershell e executar os seguintes comandos:
<ul>
<li>Execute o comando abaixo para mostrar todos os containers ativos do ambiente, ele apresenterá o CONTAINER ID que será a informação necessária para os próximos passos.
<ul>
<li>
<pre>docker container ls</pre>
</li>
</ul>
</li>
<li>Digite o comando abaixo para acessar o bash linux do container do zimbra:
<ul>
<li>
<pre>docker exec -it &lt;nome do container&gt; /bin/bash</pre>
</li>
</ul>
</li>
<li>Digite o comando abaixo para confirmar que está dentro do zimbra server, deve aparecer o nome &#8220;zimbra-docker.zimbra.io&#8221;:
<ul>
<li>
<pre>hostname</pre>
</li>
</ul>
</li>
<li>Digite os comandos abaixo para atualizar o linux e o zimbra:
<ul>
<li>
<pre>apt-get update</pre>
</li>
<li>
<pre>apt-get upgrade</pre>
</li>
<li>
<pre>exit</pre>
</li>
<li>
<pre>docker stop &lt;nome do container zimbra&gt;</pre>
</li>
<li>
<pre>docker start &lt;nome do container zimbra&gt; ; docker logs -f &lt;nome do container zimbra&gt;</pre>
</li>
<li>
<pre>apt-get update</pre>
</li>
<li>
<pre>apt-get upgrade</pre>
</li>
</ul>
</li>
<li>Ao finalizar, ele dirá que os serviços do Zimbra estão prontos para ser usados, não feche e não interrompa esse console. Volte ao powershell que estava aberto e digite os seguintes comandos:
<ul>
<li>
<pre>docker exec -it &lt;nome do container&gt; /bin/bash</pre>
</li>
<li>
<pre>su - zimbra</pre>
</li>
<li>
<pre>zmcontrol status</pre>
</li>
</ul>
</li>
</ul>
</li>
<li>Os serviços devem estar todos como &#8220;running&#8221; ao ser finalizados</li>
</ul>
</li>
<li>Como o ambiente está operacional agora, acesse o portal de webmail e gerenciamento do zimbra pelos seguintes links:</li>
</ol>
<p><img loading="lazy" decoding="async" class="aligncenter size-large wp-image-1039" src="http://solucoesms.com.br/wp-content/uploads/2020/06/zimbraserver-1024x631.png" alt="" width="678" height="418" srcset="https://solucoesms.com.br/wp-content/uploads/2020/06/zimbraserver-1024x631.png 1024w, https://solucoesms.com.br/wp-content/uploads/2020/06/zimbraserver-300x185.png 300w, https://solucoesms.com.br/wp-content/uploads/2020/06/zimbraserver-768x473.png 768w, https://solucoesms.com.br/wp-content/uploads/2020/06/zimbraserver.png 1039w" sizes="auto, (max-width: 678px) 100vw, 678px" /></p>
<ul>
<li style="list-style-type: none;">
<ul>
<li><a href="https://localhost">https://localhost</a></li>
<li><a href="https://localhost:7071">https://localhost:7071</a></li>
<li>Utilize o usuário <strong>admin</strong> e a senha <strong>Zimbra2017</strong> para acessá-lo.</li>
</ul>
</li>
</ul>
<p><strong>Obs1:</strong> Atente-se que o site é https:// se tentar acessar pelo http não funcionará.</p>
<p style="text-align: justify;"><strong>Obs2:</strong> Após a instalação automatizada do Zimbra, se você fechar ou sair do console bash do container ou se reiniciar o computador, o container do docker poderá sair e permanecer no estado <strong>parado</strong>, para iniciá-los basta executar os seguintes comandos:</p>
<pre>docker ps -a
docker start &lt;nome do container zimbra&gt;
docker exec -it &lt;nome do container zimbra&gt; /bin/bash
su - zimbra
zmcontrol restart</pre>
<p>Agora seu servidor está prontos para ser usado em seus testes locais!<br />
Enjoy!</p>
<p><strong>Fonte:</strong> <a href="https://github.com/jorgedlcruz/zimbra-docker">https://github.com/jorgedlcruz/zimbra-docker</a><br />
<strong>Fonte2:</strong> <a href="https://wiki.zimbra.com/wiki/Zmcontrol">https://wiki.zimbra.com/wiki/Zmcontrol</a></p>
