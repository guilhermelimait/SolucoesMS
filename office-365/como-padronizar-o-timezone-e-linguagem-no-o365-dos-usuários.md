# Como padronizar o timezone e linguagem no O365 dos usuários?

Date: 2020-07-09 13:49:46

Categories: Exchange, Exchange Online, Gerenciamento, O365, Office 365, Powershell

---

<p>Olá pessoal,<br />
Seguindo uma solução simples e que pode ser aplicada para seu ambiente caso precise fazer a alteração da linguagem padrão do Office 365 dos seus usuários. Caso precise, é possível fazer por usuário ou em toda a organização, veja abaixo:</p>
<p>Para apenas um usuário:</p>
<div>
<div>
<pre class="brush: powershell; title: ; notranslate" title="">Get-mailbox usuario@dominio.com -ResultSize unlimited | Set-MailboxRegionalConfiguration -Language 1046 -TimeZone &quot;E. South America Standard Time&quot; -LocalizeDefaultFolderName -DateFormat &quot;dd/MM/yyyy&quot; -TimeFormat &quot;HH:mm&quot;</pre>
</div>
</div>
<div></div>
<div>Para todos os usuários:</div>
<div></div>
<div>
<div>
<div>
<pre class="brush: powershell; title: ; notranslate" title="">Get-mailbox -ResultSize unlimited | Set-MailboxRegionalConfiguration -Language 1046 -TimeZone &quot;E. South America Standard Time&quot; -LocalizeDefaultFolderName -DateFormat &quot;dd/MM/yyyy&quot; -TimeFormat &quot;HH:mm&quot;</pre>
</div>
</div>
</div>
<div></div>
<div>Enjoy!</div>
