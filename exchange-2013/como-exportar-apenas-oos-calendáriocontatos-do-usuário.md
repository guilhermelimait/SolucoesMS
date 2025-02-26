# Como exportar apenas o/os calendário/contatos do usuário?

Date: 2017-01-09 12:45:25

Categories: Exchange 2010, Exchange 2013, Exchange 2016

---

<p>Olá pessoal,<br />
Em uma nova solicitação, um usuário precisava que apenas seus contatos e sua agenda fossem exportados para um arquivo .pst. Para isso, usei dos seguintes comandos:</p>
<div>
<blockquote>
<pre><span style="color: #000000;">New-MailboxExportRequest -Mailbox User1 -IncludeFolders "#Contacts#" -filepath \\server\share\user1.pst</span></pre>
<pre><span style="color: #000000;">New-MailboxExportRequest -Mailbox User1 -IncludeFolders "#Calendar#" -filepath \\server\share\user1.pst
</span></pre>
</blockquote>
</div>
<p><span style="color: #000000;">Enjoy!</span></p>
