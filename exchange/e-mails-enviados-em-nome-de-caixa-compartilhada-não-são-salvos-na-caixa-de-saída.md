# E-mails enviados em nome de caixa compartilhada não são salvos na caixa de saída

Date: 2018-07-05 14:20:06

Categories: Exchange, Exchange 2010, Office 365

---

<p>Caso precise enviar mensagens em nome de uma caixa compartilhada e salvar as mensagens na caixa de saída dela ao invés da sua conta, utilize o seguinte comando:</p>
<p>No Exchange 2010:</p>
<pre>Set-MailboxSentItemsConfiguration "caixacompartilhada@dominio.com.br" -SendAsItemsCopiedTo SenderAndFrom -SendOnBehalfOfItemsCopiedTo senderandfrom</pre>
<p>No O365:</p>
<pre>Set-Mailbox "caixacompartilhada@dominio.com.br" -MessageCopyForSendOnBehalfEnabled $true -MessageCopyForSentAsEnabled $true</pre>
<p>Enjoy!</p>
