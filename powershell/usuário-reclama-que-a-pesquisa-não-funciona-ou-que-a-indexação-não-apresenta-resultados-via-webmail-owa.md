# Usuário reclama que a pesquisa não funciona ou que a indexação não apresenta resultados via webmail OWA

Date: 2019-11-22 11:54:05

Categories: Exchange, O365, Powershell

---

<p>Olá pessoal,<br />
Tive um caso diferente onde o usuário reclamou que a pesquisa não respondia ou que a indexação via webmail não apresentava os resultados via o owa no outlook.com. Por ser um caso bem diferente, fiz algumas pesquisas e descobri que nesses casos, refazer a indexação online ou forçar a indexação depende de apenas alguns comandos, veja abaixo:</p>
<p>Primeiramente, faça um new-moverequest na conta:</p>
<blockquote>
<pre><span style="color: #000000;">New-MoveRequest -Identity user@domain.com</span></pre>
</blockquote>
<p>Verifique o status do comando utilizando:</p>
<blockquote>
<pre><span style="color: #000000;">Get-MoveRequestStatistics -Identity user@domain.com
Get-MoveRequest -Identity user@domain.com</span></pre>
</blockquote>
<p>Assim que o comando apresentar o status como &#8220;completed&#8221;, execute o comando:</p>
<blockquote>
<pre><span style="color: #000000;">Remove-MoveRequest -Identity user@domain.com</span></pre>
</blockquote>
<p>Esse procedimento pode levar algumas horas devido ao tamanho da caixa, mas assim que for concluído, poderá utilizar novamente a pesquisa e verificar o resultado.</p>
<p>Enjoy!</p>
<p>Fonte: <a href="https://techcommunity.microsoft.com/t5/Exchange/Rebuild-search-index-of-a-mailbox-in-Exchange-Online/m-p/25663">Um</a></p>
