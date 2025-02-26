# Adicionar permissão Full ou SendAs em caixa compartilhada no O365

Date: 2017-12-27 16:50:18

Categories: Exchange, Office 365

---

<p style="text-align: justify;">Caso precise dar acesso com permissão de Full Access ou Send As para seus usuários em caixas que já estejam no O365, utilize o seguinte comando:</p>
<pre><span style="color: #ff0000;">$mailbox = "caixa compartilhada"
$User = "mailbox que precisa de acesso"
Add-MailboxPermission $mailbox -User $user -AccessRights FullAccess
Add-RecipientPermission $mailbox -AccessRights SendAs -Trustee $user</span></pre>
