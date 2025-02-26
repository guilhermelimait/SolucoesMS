# Como pesquisar e-mails enviados no meu ambiente?

Date: 2015-11-09 13:36:37

Categories: Exchange, Exchange 2007, Exchange 2010, Exchange 2013

---

<p style="text-align: justify;">Olá pessoal,<br />
No post de hoje vou explicar brevemente sobre como fazer uma pesquisa de uma mensagem que foi enviada no seu ambiente de Exchange. Para isso usaremos alguns comandos simples e bem interessantes. No caso, podemos fazer pesquisas utilizando palavras chaves no título usando o parâmetro &#8220;MessageSubject&#8221;, ou por data usando o &#8220;Start&#8221; e&#8221;End&#8221; para limitar a pesquisa, assim como vários outros que podem ser utilizados.</p>
<blockquote>
<pre>Get-MessageTrackingLog -MessageSubject "TextoBLABLABLA" -start 2018/01/01 | select timestamp, Sender, MessageSubject, {$_.Recipients}, TotalBytes, RecipientCount | Export-Csv c:\reports\ArquivoSaída.csv</pre>
</blockquote>
<p style="text-align: justify;">Caso seu ambiente seja com vários datacenters, é possível perguntar para apenas alguns CAS/HUB servers. Para isso use o seguinte comando:</p>
<blockquote>
<pre>Get-TransportServer CAS-* | Get-MessageTrackingLog -MessageSubject "TextoBLABLABLA" -start 2015/11/01 | select timestamp, Sender, MessageSubject, {$_.Recipients}, TotalBytes, RecipientCount | Export-Csv c:\reports\ArquivoSaída.csv</pre>
</blockquote>
<p>Caso precise procurar pelo domínio e não apenas pelo endereço de um remetente/destinatário é preciso fazer um pouco diferente:</p>
<blockquote>
<pre>Get-TransportServer CAS-* | Get-MessageTrackingLog -ResultSize Unlimited -Start 2018/01/01 | where{$_.sender –like "*@dominio.com.br"} | select-object eventid, timestamp, sender, {$_.Recipients}, recipientcount, messagesubject | Export-Csv .log1-sender.csv</pre>
</blockquote>
<p>Espero que tenha ajudado!<br />
Enjoy!</p>
<p><em>PS.: CAS-* deve ser substítuido pelo nome do seu servidor CAS</em></p>
