# Como dar permissão em caixa de correio compartilhada?

Date: 2013-07-16 20:04:27

Categories: Exchange 2007, Exchange 2010

---

<p>Algumas vezes é preciso que um usuário tenha o acesso de enviar mensagens em nome de outro ou de ter total controle sobre a conta de outro usuário ou recurso. Mas para que isso seja feito é preciso que tais permissões sejam criadas, acompanhe:</p>
<p>Dar permissão de FullAccess do usuário John.Smith na conta de Guilherme.Lima:</p>
<pre>Add-MailboxPermission -Identity "Guilherme Lima" -User John.Smith -AccessRights Fullaccess</pre>
<p>Dar permissões de SendAs do usuário John.Smith na conta de Guilherme.Lima:</p>
<pre>Add-ADPermission "Guilherme Lima" -User "Domainjohn.smith" -Extendedrights "Send As"</pre>
<p>E por hoje é só. Enjoy!</p>
