# Como liberar o espaço de itens antigos na lixeira dos usuários no Exchange?

Date: 2014-08-11 14:37:17

Categories: Exchange 2007, Exchange 2010, Exchange 2013

---

<p>Pessoal,</p>
<p>Uma solução fantástica que pode ser utilizada para liberar o espaço dos itens antigos na lixeira dos usuários dentro do Exchange 2010 pode ser feito tanto para liberar o whitespace quanto para liberar o espaço utilizado pelo usuário final. Para isso um novo script pode ser utilizado, confira:</p>
<blockquote>
<pre>Set-AdServerSettings -ViewEntireForest $True</pre>
<pre> $mbxs = Get-Mailboxstatistics -Database SADAG2-P3-DB11 | select displayname, @{expression = {$_.TotalDeletedItemSize.Value.ToMB()}; label="TotalDeletedItemSize"} | where {$_.TotalDeletedItemSize -gt 10}</pre>
<pre>foreach ($mbx in $mbxs){
Search-Mailbox -Identity $mbx.DisplayName -searchQuery "Received:&lt; $('2014-07-14') or Sent:&lt; $('2014-07-14')" -SearchDumpsterOnly -DeleteContent -Force:$TRUE}
</pre>
</blockquote>
<p>Enjoy!</p>
