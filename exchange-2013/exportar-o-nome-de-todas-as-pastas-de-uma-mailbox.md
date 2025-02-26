# Exportar o nome de todas as pastas de uma mailbox

Date: 2015-09-25 12:52:35

Categories: Exchange 2007, Exchange 2010, Exchange 2013

---

<p>Algumas vezes é necessário saber se o usuário moveu alguma pasta de sua conta para outro local antes de fazer um restore de mailbox. Para isso, use o comando abaixo trocando o usuário para o qual você precisa investigar.</p>
<blockquote>
<pre>Get-MailboxFolderStatistics -Identity MAILBOX | Select Name,FolderPath,FolderSize,FolderAndSubfolderSize</pre>
</blockquote>
<p>Enjoy! 😀</p>
