# Erro: The server software doesn&#8217;t support the type of search requested. [Resolvido]

Date: 2016-09-29 14:03:46

Categories: Exchange, Exchange 2000, Exchange 2003, Exchange 2007, Exchange 2010, Exchange 2013

---

<p style="text-align: justify;">Ao tentar fazer algumas pesquisas para exportação de dados sobre um usuário pelo exchange, o erro informado abaixo estava sendo apresentado. Um erro que até então parecia ser tão bobo pois o comando era tão simples que não tinha como ter algo errado.</p>
<p style="text-align: justify;">O problema do erro era tão simples mas que aparentemente ainda não foi corrigido pelos desenvolvedores da Microsoft.</p>
<p style="text-align: justify;"><span style="color: #ff0000;"><strong>Situação problema:</strong></span> Ao executar um comando simples para exportação de dados de message tracking de um usuário a mensagem de erro era apresentada.</p>
<p style="text-align: justify;"><strong><span style="color: #ff0000;">Erro encontrado:</span></strong> A mensagem &#8220;The server software doesn&#8217;t support the type of search requested&#8221; é apresentada ao executar um comando de exportação de informações de um usuário comum.</p>
<p style="text-align: justify;"><strong><span style="color: #ff0000;">Solução encontrada:</span></strong> Segundo o site de suporte da Microsoft, quando um usuário possui mais de 49 endereços de emails entre SMTP, X400 e X500 a pesquisa é abortada e o erro é apresentado. A solução encontrada foi remover os endereços x400 e x500 antigos e que não são mais utilizados dentro do ambiente.</p>
<p style="text-align: justify;">Fonte: <a href="https://social.technet.microsoft.com/Forums/exchange/en-US/ba4b2c09-9c11-4feb-aca4-adfd22e918c0/message-tracking-fails-with-the-server-software-doesnt-support-the-type-of-search-requested-for?forum=exchangesvradminlegacy">Aqui</a></p>
<p>&nbsp;</p>
