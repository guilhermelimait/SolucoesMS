# Exportar as maiores caixas do O365

Date: 2018-02-20 19:05:08

Categories: Office 365

---


<p>Pode parecer estranho, mas sim, mesmo com um tamanho gigante para usuários no O365, de vez em quando aparecem solicitações como essa em que é preciso exportar a lista de usuários que já ultrapassou os 50Gb de uso.</p>



<p>Para isso, use o seguinte comando:</p>



<pre class="wp-block-verse"><strong>get-mailbox | Get-MailboxStatistics | where {$_.TotalItemSize -ge 50GB}</strong></pre>



<p>Enjoy!</p>
