# Docker: Como atualizar o Portainer?

Date: 2020-07-09 11:13:36

Categories: Docker, Portainer

---

<p>Como estamos evoluindo com a gestão de ambientes em docker é preciso também manter a nossa gestão web em suas últimas versões para garantir a compatibilidade e correção de erros. Para isso, faremos o seguinte procedimento para atualizar o Portainer:</p>
<p>1 &#8211; Abra o powershell</p>
<p>2- Digite o seguinte comando:</p>
<pre class="brush: python; title: ; notranslate" title="">docker pull portainer/portainer
docker stop portainer
docker rm portainer
docker run --name portainer --restart=unless-stopped -d -p 8000:8000 -p 9000:9000 -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer
</pre>
<p>No exemplo acima estou usando outros dois parâmetros novos, um para que ele sempre seja <strong>reiniciado</strong> automaticamente e outro dando o <strong>nome</strong> dele como portainer para facilitar nos comandos futuros.</p>
<p>Lembre-se que nesse exemplo estamos usando o docker pelo Windows ok? 😀</p>
