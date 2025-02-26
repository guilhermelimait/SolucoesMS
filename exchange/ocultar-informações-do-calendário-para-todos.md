# Ocultar informações do calendário para todos

Date: 2019-08-07 10:40:12

Categories: Exchange, O365

---

<p>Olá pessoal,<br />
Caso necessite ocultar informações de um calendário para algum usuário como um presidente da empresa para todos os funcionários, é possível executá-la usando o comando abaixo:</p>
<pre>Set-MailboxFolderPermission -Identity "usuario@dominio.com:\Calendar" -User Default -AccessRights AvailabilityOnly
Set-MailboxFolderPermission -Identity "usuario@dominio.com:\Calendar" -User Anonymous -AccessRights None</pre>
<p>Para mostrar o resultado:</p>
<pre>get-mailboxfolderpermission -identity "usuario@dominio.com:\Calendar"</pre>
<p>Caso necessite adicionar uma permsissão anônima utilize o comando abaixo:</p>
<pre>add-MailboxFolderPermission -Identity "usuario@dominio.com:\Calendar" -User Anonymous -AccessRights None</pre>
<p>E não se esqueça que, se estiver trabalhando com um calendário em português a palavra &#8220;Calendar&#8221; deve ser substituída por &#8220;Calendário&#8221;.</p>
<p>Fonte: <a href="https://docs.microsoft.com/en-us/powershell/module/exchange/mailboxes/add-mailboxfolderpermission?view=exchange-ps">https://docs.microsoft.com/en-us/powershell/module/exchange/mailboxes/add-mailboxfolderpermission?view=exchange-ps</a></p>
