# Adicionar Auto-resposta (aviso de fora do escritório/out of office) para vários usuários informando a alteração de endereço de email com texto em HTML

Date: 2018-04-26 18:57:49

Categories: Exchange 2013, Exchange 2016, Office 365

---


<p>Sim, uma demanda bem simples e bem específica, mas muito interessante. No caso, teremos que criar auto-assinaturas para vários usuários simultaneamente e o texto utilizado será feito em HTML. Como sabem, o powershell não utiliza do HTML como uma linguagem padrão, e por isso teremos que trocar todas as letras acentuadas como á é í ó ú ç ã para caracteres em codificação HTML. Nosso arquivo de entrada será um arquivo CSV com duas colunas, sendo elas uma para endereço origem (velho) e endereço de destino (novo).</p>



<p>O arquivo de entrada deve ser criado como users.csv e deve conter informações como a seguir:</p>



<pre class="wp-block-verse">mailOrigem,mailDestino<br />usuario1@dominio.com.br,usuario1novo@dominio.com.br<br />usuario2@dominio.com.br,usuario2novo@dominio.com.br</pre>



<p>O nosso código de execução será o seguinte:</p>



<p>$Input = &#8220;.\users.csv&#8221; <br />import-csv $Input | foreach { <br />$mailOrigem = $_.mailOrigem $mailDestino = $_.mailDestino <br />$OOFMsg = @&#8221; </p>



<p>O e-mail <a href="$mailOrigem">$mailOrigem</a> não é mais válido, tendo sido substituído pelo <a href="$mailDestino">$mailDestino</a> <br /><br />&#8220;@ <br />Write-host -ForegroundColor yellow &#8220;Starting on &#8221; $mailOrigem <br />Set-MailboxAutoReplyConfiguration $mailOrigem -AutoReplyState enabled -ExternalAudience all -InternalMessage $OOFMsg -ExternalMessage $OOFMsg <br />write-host -ForegroundColor Green &#8220;Autosignature set on&#8221; $mailDestino <br />}<br /><br /></p>



<p>Caso precise trocar o texto para o código html, segue uma ajuda: <a href="https://www.ascii.cl/htmlcodes.htm">https://www.ascii.cl/htmlcodes.htm</a></p>



<p>Enjoy!</p>
