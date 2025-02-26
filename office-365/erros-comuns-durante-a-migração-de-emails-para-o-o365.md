# Erros comuns durante a migração de emails para o O365

Date: 2020-02-19 09:10:28

Categories: Active Directory, Exchange, Exchange Online, Gerenciamento, O365, Office 365

---

<p><img loading="lazy" decoding="async" class="aligncenter size-large wp-image-939" src="http://solucoesms.com.br/wp-content/uploads/2020/02/71b69cf1e4fb4e905523a717e0e78113.jpeg" alt="" width="577" height="130" srcset="https://solucoesms.com.br/wp-content/uploads/2020/02/71b69cf1e4fb4e905523a717e0e78113.jpeg 577w, https://solucoesms.com.br/wp-content/uploads/2020/02/71b69cf1e4fb4e905523a717e0e78113-300x68.jpeg 300w" sizes="auto, (max-width: 577px) 100vw, 577px" /></p>
<p style="text-align: justify;">Olá pessoal tudo bem? Nesse post, vou tentar acumular o máximo de erros possíveis que podem ocorrer durante a migração de emails para o Exchange Online O365, ou seja, esse será um post constantemente atualizado. Nesse caso, estou demonstrando erros em que não são facilmente descritos pela Microsoft, mas que são em sua maioria muito simples de serem resolvidos. O processo de migração de emails, seja ele provindo do Zimbra, Gsuite, Exchange ou IMAP sempre vão utilizar dos mesmos processos de migração (exceto o conector, que precisa ser específico para cada caso), por isso, veja abaixo como resolvê-los:</p>
<h3>ERRO 1: <em>MigrationProvisioningPermanentException: Não foi possível executar a operação porque não foi possível encontrar o objeto &#8220;EMAILDOUSUARIO@DOMINIO.COM&#8221;  em ‎&#8217;SERVIDORDAMICROSOFT.PROD.OUTLOOK.COM‎&#8217;. &#8211;&gt; Não foi possível executar a operação porque não foi possível encontrar o objeto ‎&#8217;EMAILDOUSUARIO@DOMINIO.COM‎&#8217; em ‎&#8217;SERVIDORDAMICROSOFT.PROD.OUTLOOK.COM‎&#8217;‎&#8217;</em></h3>
<p><span style="color: #ff0000;"><strong>Causa:</strong></span> O email informado no lote de migração não está inserido na conta do usuário.</p>
<p><span style="color: #3366ff;"><strong>Solução:</strong></span> Adicione o email como alias/email secundário nas propriedades do usuário:</p>
<ul>
<li>Abra o <em>Exchange</em> &gt; <em>Destinatários</em> &gt; <em>Caixas de correio</em> &gt; Pesquise pelo usuário</li>
<li>Na guia <em>Endereços de Email</em> &gt; Adicione o email assim como informado no erro acima &#8220;<em>EMAILDOUSUARIO@DOMINIO.COM</em>&#8220;</li>
<li>Salve, reinicie o lote de migração</li>
</ul>
<div class="su-box su-box-style-glass" id="" style="border-color:#000000;border-radius:3px"><div class="su-box-title" style="background-color:#333333;color:#FFFFFF;border-top-left-radius:1px;border-top-right-radius:1px">Atenção</div><div class="su-box-content su-u-clearfix su-u-trim" style="border-bottom-left-radius:1px;border-bottom-right-radius:1px">Atenção: Caso você possua ADSync com o domínio do O365, as alterações de email devem ser feitas no usuário do AD nos campos ProxyAddress da guia Attributes</div></div>
<hr />
<h3>Erro 2: Erro: RequestFailedGeneralWebPermanentException/WebException: Error: The web server responded with a BadGateway error. Uri: https://www.googleapis.com/gmail/v1/users/EMAILDOUSUARIO@DOMINIO.COM /messages/16f7b6d56692e6eb?format=raw &#8211;&gt; The remote server returned an error: ‎(502)‎ Bad Gateway.</h3>
<p><span style="color: #ff0000;"><strong>Causa:</strong></span> Logicamente, esse erro é provindo da API do GSUITE, porém, podem acontecer erros parecidos para outros fabricantes se estiver utilizando de um conector via API.<br />
Devido essas particularidades, os problemas podem ser diversos, veja abaixo:</p>
<ul>
<li><strong>Se estiver movendo de um Serviço de email via API/Conector: </strong>
<ul>
<li>Podem haver itens corrompidos durante a migração</li>
<li>Usuário está com tamanho de caixa acima do limite da quota aplicada</li>
</ul>
</li>
<li><strong>Se estiver movendo de um Gsuite:</strong>
<ul>
<li>O lote de migração está tentando mover muitos usuários por vez ou uma quantidade muito grande de conteúdo por vez, o erro interno pode indicar &#8220;Transient error ProtocolErrorWebTransientException has occurred. The system will retry&#8221;, ou seja, estouro de limite de conteúdo/usuários durante a migração. Esse processo geralmente é reiniciado automaticamente mas pode vir a falhar várias vezes.</li>
</ul>
</li>
</ul>
<p><span style="color: #3366ff;"><strong>Solução:</strong></span> Verifique de acordo com o seu ambiente e causa indicada acima:</p>
<ul>
<li><strong>Se estiver movendo de um Serviço de email via API/Conector:</strong>
<ul>
<li>Altere no conector de migração do O365 o limite máximo de arquivos que podem ser ignorados em caso de falha na migração</li>
<li>Mude o usuário de database ou aplique uma quota maior para o usuário</li>
</ul>
</li>
</ul>
<div class="su-box su-box-style-glass" id="" style="border-color:#000000;border-radius:3px"><div class="su-box-title" style="background-color:#333333;color:#FFFFFF;border-top-left-radius:1px;border-top-right-radius:1px">Atenção</div><div class="su-box-content su-u-clearfix su-u-trim" style="border-bottom-left-radius:1px;border-bottom-right-radius:1px"><strong>Atenção:</strong> Caso a caixa esteja acima do limite da migração, os dados não serão migrados, altere no O365 a licença aplicada para o Usuário. Até o momento, os usuários podem ter os seguintes tamanhos de caixa para migração: F1: 2Gb, E1: 2Gb, E3: 50Gb e E5: 100Gb</div></div>
<ul>
<li style="text-align: left;"><strong>Se estiver movendo de um Gsuite:</strong>
<ul>
<li>Aguarde a conclusão do lote de migração ou espere o lote finalizar e reinicie apenas para os que apresentaram a falha. Verifique se houve alguma importação dos itens sincronizados, se houve alguma alteração, pelo menos indica que está havendo a comunicação entre os dois serviços.</li>
</ul>
</li>
</ul>
<hr />
<h3>ERRO 3: QuotaExceededException/MapiExceptionShutoffQuotaExceeded: Error: The process failed to get the correct properties. &#8211;&gt; MapiExceptionShutoffQuotaExceeded: Unable to get properties on object</h3>
<p><span style="color: #ff0000;"><strong>Causa:</strong></span> A quantidade de emails transferida foi muito alta e sobrepôs a quota da licença</p>
<p><span style="color: #3366ff;"><strong>Solução:</strong></span> Altere a licença para uma de nivel maior</p>
<ul>
<li>Abra o <i>Portal do O365</i>&gt; <em>Usuários</em> &gt; <i>Encontre o usuário</i>&gt; Altere a licença</li>
</ul>
<div class="su-box su-box-style-glass" id="" style="border-color:#000000;border-radius:3px"><div class="su-box-title" style="background-color:#333333;color:#FFFFFF;border-top-left-radius:1px;border-top-right-radius:1px">Atenção</div><div class="su-box-content su-u-clearfix su-u-trim" style="border-bottom-left-radius:1px;border-bottom-right-radius:1px"><strong>Atenção:</strong> Caso a caixa esteja acima do limite da migração, os dados não serão migrados, altere no O365 a licença aplicada para o Usuário. Até o momento, os usuários podem ter os seguintes tamanhos de caixa para migração: F1: 2Gb, E1: 2Gb, E3: 50Gb e E5: 100Gb</div></div>
<hr />
<h3>ERRO 4: Error: UserAlreadyBeingMigratedException: The user ‎&#8217;USER@DOMAIN.COM‎&#8217; already has a pending request. Please remove the existing request and resume the current batch or start a new batch for this user. &#8211;&gt; Name must be unique per owning mailbox. There‎&#8217;s already a request with the name ‎&#8217;MigrationService:LOTE-03:USER@DOMAIN.COM‎&#8217; owned by mailbox ‎&#8217;MAILBOX.PROD.OUTLOOK.COM/Microsoft Exchange Hosted Organizations/DOMAIN.onmicrosoft.com/USER‎&#8217;.</h3>
<p><span style="color: #ff0000;"><strong>Causa:</strong></span> Durante o processo de sincronização do usuário, ele foi finalizado antes da hora gerando o erro informando que o usuário já foi finalizado em outro lote, apesar de estar em apenas um.</p>
<p><span style="color: #3366ff;"><strong>Solução:</strong></span> Limpe o status de sincronização do usuário</p>
<ul>
<li>Abra o Powershell &gt; conecte-se ao O365 &gt; execute o comando abaixo para cada lote que queira corrigir</li>
</ul>
<pre class="brush: powershell; title: ; notranslate" title=""> Get-MigrationUser -BatchId LOTE-02 | Get-MigrationUserStatistics | Where-Object {$_.status -eq 'failed'} | Get-SyncRequest | Remove-SyncRequest</pre>
<ul>
<li>Inicie a sincronização novamente no painel de migração do Exchange Online e clicando no Play.</li>
</ul>
<hr />
<h3>ERRO 5: Error:<span data-control="Label" data-text="{Error, Mode=OneWay}">UserDuplicateInOtherBatchException: The user &#8220;USUARIO@DOMINIO.COM&#8221; is already included in migration batch &#8220;LOTE-09A.&#8221; Please remove the user from any other batch and try again</span>.</h3>
<p><span style="color: #ff0000;"><strong>Causa:</strong></span> O usuário foi inserido em mais de um lote simultâneamente.</p>
<p><span style="color: #3366ff;"><strong>Solução:</strong></span> Remova-o do lote atual e verifique se os dados estão trafegando normalmente no lote anterior.</p>
<hr />
<p>Espero que tenha ajudado! Novidades constantes aparecerão por aqui!<br />
Enjoy!</p>
