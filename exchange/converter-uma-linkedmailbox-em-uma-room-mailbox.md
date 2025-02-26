# Converter uma LinkedMailbox em uma Room mailbox

Date: 2015-10-30 12:48:05

Categories: Exchange, Exchange 2007, Exchange 2010, Exchange 2013

---

<p style="text-align: justify;">Tudo bom pessoal, agora um desafio simples, converter uma Linked Mailbox em uma Room mailbox. O Exchange não deixará você fazer essa ação diretamente. Primeiramente você deve convertê-lo em uma caixa de correio de usuário normal e, em seguida, para uma Room Mailbox. Infelizmente não é possível convertê-lo através do Console (EMC) GUI de Gerenciamento do Exchange, portanto, abra um Shell de Gerenciamento do Exchange (EMS) e digite:</p>
<blockquote>
<pre><code>Set-User -Identity &lt;e-mail address ou Alias&gt; -LinkedMasterAccount $null</code></pre>
</blockquote>
<blockquote>
<pre><code>Set-Mailbox &lt;Mailbox Name ou Alias&gt; -Type room</code></pre>
</blockquote>
<p>Ao final acrescente as permissões ao usuário.</p>
<blockquote>
<pre><code>Add-MailboxPermission &lt;Mailbox Name&gt; -User "&lt;domain\username&gt;" -AccessRights FullAccess</code></pre>
<pre><code>Add-ADPermission Research -User "&lt;domain\username&gt;" -ExtendedRights Send-As</code></pre>
</blockquote>
<p>Enjoy!</p>
