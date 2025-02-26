# Adicionar permissão anônima em calendário

Date: 2018-02-15 13:48:05

Categories: Exchange, Office 365

---


<p>Hi everyone!</p>



<p>Mais uma simples dica para quem precisa corrigir as permissões no calendário de Outlook que por acaso foi removido, alterado ou simplesmente deixou de existir. Para isso, use o seguinte comando:</p>



<p>&nbsp;</p>



<pre class="wp-block-verse">$room = "email@dominio.com.br"<br /> Set-MailboxFolderPermission $room:\Calendar -User Default -AccessRights Owner <br /> Set-MailboxFolderPermission $room:\Calendar -User Anonymous -AccessRights None</pre>



<p class="wp-block-verse">Caso necessário, adicione a permissão com o comando abaixo:</p>
<pre> Add-MailboxFolderPermission $room:\Calendar -User Anonymous -AccessRights None</pre>
