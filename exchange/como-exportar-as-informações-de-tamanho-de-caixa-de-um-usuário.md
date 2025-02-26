# Como exportar as informações de tamanho de caixa de um usuário?

Date: 2017-06-27 18:20:20

Categories: Exchange, Exchange 2007, Exchange 2010, Exchange 2013, Exchange 2016

---

<p style="text-align: justify;">Algumas vezes é necessário saber o tamanho da caixa assim como a quantidade de items, para isso use o seguinte comando:</p>
<pre>Get-MailboxStatistics [username] | ft DisplayName, TotalItemSize, ItemCount</pre>
<p style="text-align: justify;">Caso queira exportar o nome das pastas e suas quantidades de itens, use o seguinte comando:</p>
<pre>get-mailbox [username] | Get-MailboxFolderStatistics | ft name, foldersize</pre>
<p>Enjoy!</p>
