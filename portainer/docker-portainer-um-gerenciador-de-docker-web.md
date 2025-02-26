# Docker: Portainer um gerenciador de docker web

Date: 2020-06-17 15:02:30

Categories: Docker, Portainer

---

<p><img loading="lazy" decoding="async" class="aligncenter size-full wp-image-1012" src="http://solucoesms.com.br/wp-content/uploads/2020/06/portainer.png" alt="" width="393" height="128" srcset="https://solucoesms.com.br/wp-content/uploads/2020/06/portainer.png 393w, https://solucoesms.com.br/wp-content/uploads/2020/06/portainer-300x98.png 300w" sizes="auto, (max-width: 393px) 100vw, 393px" /></p>
<p style="text-align: justify;">Portainer é uma ferramenta de gestão web das funções do docker, nele é possível fazer a gestão local ou remota de quaisquer recursos disponíveis no seu ambiente. Por ser uma ferramenta web, fica muito mais fácil visualizar e acompanhar o seu ambiente. Para que você possa fazer esse tipo de gestão, faça o download do portainer seguindo os seguintes comandos:</p>
<ol>
<li>Vá no menu Iniciar e digite &#8220;Powershell&#8221; &gt; Abra o Powershell com direitos administrativos</li>
<li>Siga o procedimento abaixo para instalar o portainer:
<ul>
<li>Crie o volume do container com o seguinte comando:
<ul>
<li>
<pre>docker volume create portainer_data</pre>
</li>
</ul>
</li>
<li>Crie o container do portainer com o seguinte comando:
<ul>
<li>
<pre>docker run -d -p 9000:9000 --name portainer --restart=always -v portainer_data:/data portainer/portainer --no-auth -H tcp://docker.for.win.localhost:2375</pre>
</li>
<li>Como o portainer ainda não foi instalado localmente, ele irá iniciar o download automaticamente do que for necessário para sua instalação e configuração, aguarde a finalização do comando.</li>
</ul>
</li>
<li>Acesse o link <a href="http://localhost:9000/">http://localhost:9000/</a> para acessar o Portainer</li>
</ul>
</li>
</ol>
<p>Se você acessou corretamente o site, parabéns!</p>
<p>Enjoy!</p>
<p><strong>Fonte:</strong> <a href="https://gist.github.com/SeanSobey/344edd228922ffd4266ae7d451421ab6">https://gist.github.com/SeanSobey/344edd228922ffd4266ae7d451421ab6</a></p>
