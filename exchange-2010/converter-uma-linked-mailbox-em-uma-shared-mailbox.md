# Converter uma Linked Mailbox em uma Shared Mailbox

Date: 2015-09-24 17:31:25

Categories: Exchange 2010

---

<p style="text-align: justify;">Algumas vezes, pode ser necessário converter uma caixa de correio vinculada a uma conta compartilhada. A caixa de correio vinculada é uma caixa de correio que é acessado por um usuário em uma floresta separada e confiável. O Exchange não deixará você fazer essa ação diretamente. Primeiramente você deve convertê-lo em uma caixa de correio de usuário normal e, em seguida, para uma conta compartilhada. Infelizmente não é possível convertê-lo através do Console (EMC) GUI de Gerenciamento do Exchange, portanto, abra um Shell de Gerenciamento do Exchange (EMS) e digite:</p>
<blockquote>
<pre><code>Set-User -Identity &lt;e-mail address&gt; -LinkedMasterAccount $null</code></pre>
</blockquote>
<p>e então:</p>
<blockquote>
<pre><code>Set-Mailbox &lt;Mailbox Name&gt; -Type shared</code></pre>
</blockquote>
<p>Ao final acrescente as permissões ao usuário.</p>
<blockquote>
<pre><code>Add-MailboxPermission &lt;Mailbox Name&gt; -User "&lt;domain\username&gt;" -AccessRights FullAccess</code></pre>
<pre><code>Add-ADPermission Research -User "&lt;domain\username&gt;" -ExtendedRights Send-As</code></pre>
</blockquote>
<p>Enjoy!</p>
